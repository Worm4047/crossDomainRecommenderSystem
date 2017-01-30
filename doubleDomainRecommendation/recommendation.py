import csv
from sklearn.model_selection import train_test_split

file = open('../movielens/u1.base', 'rb')
data = csv.reader(file, delimiter='\t')
# print data
table = [row for row in data]
train, test = train_test_split(df, test_size = 0.5)
print len(train),len(test)