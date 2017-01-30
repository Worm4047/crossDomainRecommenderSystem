import csv
from sklearn.model_selection import train_test_split
from functions import *

file = open('../movielens/u1.base', 'rb')
data = csv.reader(file, delimiter='\t')
# print data
table = [row for row in data]
fDomainData, sDomainData = train_test_split(table, test_size = 0.5)
fDomainTrain,fDomainTest= train_test_split(fDomainData,test_size=0.5)
sDomainTrain,sDomainTest =train_test_split(sDomainData,test_size=0.5)

print len(fDomainTrain),len(fDomainTest),len(sDomainTrain),len(sDomainTest)
# print len(train),len(test)
fDomainUsers,sDomainUsers=[],[]
fDomainDict,sDomainDict={},{}
print("Filling first domain training set")
for item in fDomainTrain:
	# print item
	if not item[0] in fDomainUsers:
		fDomainUsers.append(item)
	if not item[0] in fDomainUsers:
		fDomainDict[item[0]]={}
	fDomainDict[item[0]][item[1]]=item[2]
print len(fDomainDict),len(fDomainUsers)
print("Filling second domain testing set")
for item in sDomainTrain:
	# print item
	if not item[0] in sDomainUsers:
		sDomainUsers.append(item)
	if not item[0] in sDomainUsers:
		sDomainDict[item[0]]={}
	sDomainDict[item[0]][item[1]]=item[2]
print len(sDomainDict),len(sDomainUsers)
