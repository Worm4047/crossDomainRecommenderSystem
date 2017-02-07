import csv
from sklearn.model_selection import train_test_split
from functions import *
#hello
if __name__=='__main__':

	file = open('../movielens/u.data', 'rb')
	data = csv.reader(file, delimiter='\t')

	t = [row for row in data]

	fDomainDict,sDomainDict={},{}
	fDomainDict=loadMovieLens('../movielens','/u1.base')
	sDomainDict=loadMovieLens('../movielens','/u2.base')
	fDomainTest =loadMovieLens('../movielens','/u1.test')
	
	sumAccuracy=0
	lenCount=0
	for user in fDomainTest:
		pred = getRecommendations(fDomainDict,sDomainDict,user)
		count=-1
		preds={}
		for rating,item in pred:
			preds[item]=rating
			# print movies[item],rating,item
		accuracies=[]
		for movie in fDomainTest[user]:
			if not movie in preds:continue 
			actualRating = fDomainTest[user][movie]
			predcitedRating = preds[movie]
			accu = fabs((predcitedRating - actualRating)/actualRating)
			if accu > 1:
				continue
			accuracies.append(1 - accu)
		lenCount+=1
		print (sum(accuracies)/len(accuracies))*100
		sumAccuracy+=(sum(accuracies)/len(accuracies))*100
		
	print 'Average Accuracy'
	print float(sumAccuracy)/lenCount
