# Recommender System
   
Basic recommendation System faces problems of cold start and data sparsity. For overcoming the shortcomings of the basic recommendation system, cross domain recommendations are used. In cross domain recommendation System, the information from other domains(source domain) is used to predict the user’s behavior in the target domain.
 
We have implemented both, the single domain recommendation system as well as the the cross domain recommendation system using collaborative filtering(memory based) and matrix factorization techniques and we have analyzed the accuracy of the recommendations in each case in terms of MAE(Mean Absolute Error), RMSD (Root Mean Squared Deviation), Precision and Recall measures.
# Introduction

A recommendation system is information filtering system that provides us some data prediction based on user’s data associated with the item.Recommendation system are heavily utilised by Tech giants like Amazon to improve user experience.
Single Domain recommendations are limited by the data present in that domain only.To further improve the accuracy of the system we can utilise the data from other domains as well . We can also collect social media data related to the user to obtain a virtual user profile and then give him suitable recommendations.Such techniques come under Cross domain recommendation system.
A cross domain rss aims to generate or enhance recommendations in a target domain by exploiting knowledge from source domains. We implemented cross domain by using matrix factorization.
Matrix factorization techniques are more effective because they allow us to discover the latent features underlying the interactions between users and items. Given that each user has rated some items in the system, we would like to predict how the user will rate the items that they have not yet rated, such that we can make recommendations to the users.

# PROPOSED WORK
## Basic recommendation System - Memory Based Collaborative Filtering(User Based) :-
 
The goal of a recommendation System is to generate meaningful recommendations to a collection of users for items or products that might interest them. Suggestions for books on Amazon, or movies on Netflix, are real world examples of the operation of industry-strength recommendation systems.
 
 
### Finding Nearest Neighbors from Rating Pattern
The first step is computation of nearest neighbors of each user using their rating patterns. To perform this, the ratings expressed by each user are extracted from the user-rating matrix. This is called the rating pattern of user in the system. Each user might have rated only few items in the system or he/she may have rated comparatively large number of items. The user under current consideration is referred as the active user. Rating pattern of the active users of the system will be compared against that of all other users in the system. This comparison is done with a goal to identify the like-minded people in the system. Pearson correlation coefficient is used to find the degree of similarity. 
We calculate the similarity between only those set of users whose co-rated value exceeds the preset threshold.. Similarity threshold can vary according to the level of accuracy. If similarity threshold is very high, near to one, then the nearest neighborhood will be very small. If it's very small, say very close to zero, then there are chances to get inaccurate result. So in order to get optimum result we need to set a similarity threshold in between 0 and 1.

### Problems with the basic recommendation system:-
1.Cold Start:- If the user is new in a certain domain then sufficient amount of data about the user such as his preferences , likes/dislikes etc is not available hence the basic recommendation system which works by finding like-minded people will not work.
 
2.Data Sparsity Problem:- When the information reported (like items rated) by a user is very less compared to the available data (items in the system), then it is very difficult to get the similarity between the like-minded people accurately.

# Experimental Setup and Result Analysis
## Dataset Used:-
1 million ratings dataset from movielens.The data  files contain 1,000,209 anonymous ratings of approximately 3,900 movies made by 6,040 MovieLens users who joined MovieLens in 2000.

Data fields are:- UserID,MovieID,Rating,Timestamp
- User IDs range between 1 and 6040.
- Movie IDs range between 1 and 3952.
- Ratings are made on a 5-star scale (whole-star ratings only).
- Timestamp is represented in seconds since the epoch as returned by time(2).
### Dividing data for cross domain:-
Data has been  divided into four parts D1,D2,D3 and D4.
 - D1 and D2 have users common.
 - D1 and D3 have items common.
 - D1 and D4 have no user and no item in common.

Now we divided D1 into ten parts for 10%,20%,...,100% with respect to the items.
Each set has further been divided randomly into 30%-70% for testing and training respectively.
Cross Domain Recommendations using Matrix Factorization:-
Consider a data set , say it be 10% dataset of D1(Target Domain) and the complete 100% dataset from D4(Source Domain).
A (user X item) matrix was formed using D4 dataset and matrix from D1 was appended to it.Matrix factorization algorithm was then applied on this  matrix, as a result of which the unknown ratings get filled up.
Now as the model has got developed. We test the model on the testing part of the dataset i.e., testing set from 10% dataset of D1 and calculated the MAE, RMSD, Precision and Recall values. Same is repeated with every dataset.  
Note 
Case 1 :-  cross domain recommendation D1 is Target Domain and D4 is Source Domain.
Case 2 :-  cross domain recommendation D2 is Target Domain and D3 is Source Domain.
Case 3 :-  cross domain recommendation D3 is Target Domain and D2 is Source Domain.
Case 4 :-  cross domain recommendation D4 is Target Domain and D1 is Source Domain.

# Results:-
## MAE Results for D1:-
![MAE RESULTS FOR D1|250x250](https://github.com/Worm4047/crossDomainRecommenderSystem/blob/master/mae_d1_1.PNG)
![MAE RESULTS FOR D1](https://github.com/Worm4047/crossDomainRecommenderSystem/blob/master/mae_d1_2.png)
## RMSD Results for D1:-
![RMSD RESULTS FOR D1](https://github.com/Worm4047/crossDomainRecommenderSystem/blob/master/rmsd_d1_1.PNG)
![RMSD RESULTS FOR D1](https://github.com/Worm4047/crossDomainRecommenderSystem/blob/master/rmsd_d1_2.png)

## MAE Results for D2:-
![MAE RESULTS FOR D2](https://github.com/Worm4047/crossDomainRecommenderSystem/blob/master/mae_d2_1.PNG)
![MAE RESULTS FOR D2](https://github.com/Worm4047/crossDomainRecommenderSystem/blob/master/mae_d2_2.png)
## RMSD Results for D2:-
![RMSD RESULTS FOR D2](https://github.com/Worm4047/crossDomainRecommenderSystem/blob/master/rmsd_d2_1.PNG)
![RMSD RESULTS FOR D2](https://github.com/Worm4047/crossDomainRecommenderSystem/blob/master/rmsd_d2_2.png)

## MAE Results for D3:-
![MAE RESULTS FOR D3](https://github.com/Worm4047/crossDomainRecommenderSystem/blob/master/mae_d1_1.PNG)
![MAE RESULTS FOR D3](https://github.com/Worm4047/crossDomainRecommenderSystem/blob/master/mae_d1_2.png)
## RMSD Results for D3:-
![RMSD RESULTS FOR D3](https://github.com/Worm4047/crossDomainRecommenderSystem/blob/master/rmsd_d3_1.PNG)
![RMSD RESULTS FOR D3](https://github.com/Worm4047/crossDomainRecommenderSystem/blob/master/rmsd_d3_2.png)

## MAE Results for D4:-
![MAE RESULTS FOR D4](https://github.com/Worm4047/crossDomainRecommenderSystem/blob/master/mae_d4_1.PNG)
![MAE RESULTS FOR D4](https://github.com/Worm4047/crossDomainRecommenderSystem/blob/master/mae_d4_2.png)
## RMSD Results for D4:-
![RMSD RESULTS FOR D4](https://github.com/Worm4047/crossDomainRecommenderSystem/blob/master/rmsd_d4_1.PNG)
![RMSD RESULTS FOR D4](https://github.com/Worm4047/crossDomainRecommenderSystem/blob/master/rmsd_d4_2.png)

# Conclusion

After observing MAE,RMSD,Precision and Recall values of single domain system and cross domain system, we have concluded that accuracy of cross domain recommendations is better as compared to that of the single domain recommendations.Average MAE in single domain is 0.777798 and Average MAE in Cross Domain is 0.766668 .After adding biases in cross domain, average MAE is 0.766204 which is comparable to the MAE observed in cases of without biases.
