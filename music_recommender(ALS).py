from pyspark import SparkConf
from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql import Row
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.recommendation import ALS
#### aws s3 cp s3://bucket_name/file ./

if __name__ == "__main__":
	#leave config blank for EMR cluster
	conf=SparkConf()
	sc=SparkContext(conf=conf)
	sqlContext=SQLContext(sc)
	sc.setLogLevel("WARN")
 
	raw_data=sqlContext.read.csv("music_instrument_ratings.csv", header="true", inferSchema="true",mode="DROPMALFORMED")
	raw_data.show(5)
	raw_data.printSchema()

	#split the data into training and testing
	(training, test) = raw_data.randomSplit([0.7, 0.3])

	# Build the recommendation model using ALS on the training data
	als = ALS(maxIter=20, regParam=0.5, userCol="userID", itemCol="Item", ratingCol="ratings", coldStartStrategy="drop")
	model = als.fit(training)


	# Evaluate the model by computing the RMSE on the test data
	predictions = model.transform(test)
	evaluator = RegressionEvaluator(metricName="rmse", labelCol="ratings",
                                predictionCol="prediction")
	rmse = evaluator.evaluate(predictions)
	print("Root-mean-square error = " + str(rmse))


spark.stop()
