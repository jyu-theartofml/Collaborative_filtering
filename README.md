# Collaborative_filtering

<p> This repository demonstrates the usage of Collaborative Filtering (CF) on a dataset of ratings for musical instrument (source: http://jmcauley.ucsd.edu/data/amazon/)
The dataset contains 4 columns, user, item, rating, timestamp. </p>
<p><b>UPDATE: I have added the code for Alternating Least Square (ALS) recommender using Spark MLlib's API. This was written to be ran on Amazon's EMR cluster. The performance of ALS did not match that of the matrix factorization by Stochastic Gradient Descend.</b></p>
<p>The python notebook provides a quick comparison of algorithms for <i> Memory based CF</i>, <i>Model based CF (rank factorization via SVD)</i>, as well as <i>Stochastic Gradient Descent</i> for solving the rank factorization.
The script is based on the algorithms presented on these two blogs: http://online.cambridgecoding.com/notebooks/mhaller/implementing-your-own-recommender-systems-in-python-using-stochastic-gradient-descent-4, 
http://blog.ethanrosenthal.com/2015/11/02/intro-to-collaborative-filtering/, but some details were modified to accomodate the dataset and streamline the process. </p>


<b>Memory based CF  </b>
<p>In Collaborative Filtering, Memory based CF algorithm look for similarity between users or between items. In user-user filter, cosine similarity is calculated between every pair of users within the data set resulting in a similarity matrix that's n_users X n_users. Similary for item-item, the cosine similarity is calculated between items. 
The similiarity matrix is the weight that will yield model prediction. </p>

<b>Model based CF (SVD) </b>
<p>Memory based CF algorithm can be very computationally expensive and is known to have issue with scalability, plus it doesn't learn well with highly sparse matrix like the one used in this python example.
A useful alternative is model based CF using SVD for matrix decomposition. This method breaks down the user-item matrix into small matrices with latent-feature vectors,
representing implicit characteristics for the user and items. However, SVD can also become computationally expensive with large matrix. </p>
<p align='center'><a href="https://www.slideshare.net/DKALab/collaborativefilteringfactorization"><img src= 'svd.jpg', width=50%, height=50%></a><br> Source: DKAlab (Slideshare)</p>

<b>Model based CF (Stochastic Gradient Descend) </b>
<p>Another way to solve the matrix factorization is by using Stochastic Gradient Descend(SGD) to estimate the low-rank matrices corresponding to user and item. This method will save on memory thus more computationally efficient because it incrementally updates the model to find a better fit that minimizes the regularized squared error loss function.

<p align='center'><a href="https://databricks-training.s3.amazonaws.com/movie-recommendation-with-mllib.html"><img src= 'matrix_factorization.png', width=50%, height=50%></a> <br>Source: databricks training</p>

<p>After comparing the three algorithms, SGD matrix factorization yielded the best result with 100 iterations, learning rate of 0.01 to calculate the optimal latent feature matrices (see ipynb file). It would be interesting to use the same data set and run it with Alternative Least Squre (ALS) on Spark since it's an API within the current spark.ml package. 

<b>References</b>
<br>1)<i>Koren et al. (2009) Koren, Y., Bell, R.M., Volinsky, C.: Matrix factorization techniques for recommender systems. IEEE Computer 42(8), 30–37 (2009) 32 Francesco Ricci, Lior Rokach and Bracha Shapira<br></i>
2)<i> Yu, H.F., Hsieh, C. J., Si, S., Dhillon, I.: Scalable coordinate descent approaches to parallel matrix factorization for recommender systems. In IEEE 12th International Conference on Data Mining, pp. 765–774 (2012)</i>
