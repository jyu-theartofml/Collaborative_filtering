# Collaborative_filtering

<p> This repository demonstrates the usage of Collaborative Filtering (CF) on a dataset of ratings for musical instrument (source: http://jmcauley.ucsd.edu/data/amazon/)
The dataset contains 4 columns, user, item, rating, timestamp. </p>

<p>The python notebook provides a quick comparison of algorithms for <i> Memory based CF</i>, <i>Model based CF (rank factorization via SVD)</i>, as well as <i>Stochastic Gradient Descent</i> for solving the rank factorization.
Note that the script is based on the algorithms presented from these two blogs: http://online.cambridgecoding.com/notebooks/mhaller/implementing-your-own-recommender-systems-in-python-using-stochastic-gradient-descent-4, 
http://blog.ethanrosenthal.com/2015/11/02/intro-to-collaborative-filtering/, but some details were modified to accomodate the dataset and streamline the process. 


<b>Memory based CF  </b>
<p>In Collaborative Filtering. Memory based CF algorithm look for similarity between users or between items. In user-user filter, cosine similarity is calculated between every pair of users within the data set result in a similarity matrix that's n_users X n_users. Similary for item-item, the cosine similarity is calculated between items. 
The similiarity matrix is the weight that will yield model prediction. </p>

<b>Model based CF (SVD) </b>
<p>Memory based CF algorithm can be very computationally expensive when there's a large volume of data, and it doesn't work well with highly sparse matrix like the one used in this python example.
A useful alternative is model based CF using SVD for matrix decomposition. This method breaks down the user-item matrix into small matrices with latent-feature vectors,
represent implicit characteristics for the user and items</p>
<im src="
