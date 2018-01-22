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
 
	raw_data=sqlContext.read.load("s3://music-recommender/ratings_Musical_Instruments.csv", format='csv').rdd
	parts = raw_data.map(lambda row: row.value.split("/t"))
	ratingsRDD = parts.map(lambda p: Row(userId=int(p[0]), Item=int(p[1]),
                                     ratings=float(p[2]), timestamp=long(p[3])))
	df=sqlContext.createDataFrame(ratingsRDD)

	#split the data into training and testing
	(training, test) = df.randomSplit([0.7, 0.3])

	# Build the recommendation model using ALS on the training data
	als = ALS(maxIter=5, regParam=0.01, userCol="userID", itemCol="Item", ratingCol="ratings", coldStartStrategy="drop")
	model = als.fit(training)


	# Evaluate the model by computing the RMSE on the test data
	predictions = model.transform(test)
	evaluator = RegressionEvaluator(metricName="rmse", labelCol="ratings",
                                predictionCol="prediction")
	rmse = evaluator.evaluate(predictions)
	print("Root-mean-square error = " + str(rmse))


spark.stop()
