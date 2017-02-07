from math import *

def sim_distance(prefs,person1,person2):
  si={}
  for item in prefs[person1]: 
    if item in prefs[person2]: si[item]=1
  if len(si)==0: return 0
  sum_of_squares=sum([pow(prefs[person1][item]-prefs[person2][item],2) for item in prefs[person1] if item in prefs[person2]])
  return 1/(1+sum_of_squares)

  
def sim_pearson(prefs,p1,p2):
  si={}
  for item in prefs[p1]: 
    if item in prefs[p2]: si[item]=1
  if len(si)==0: return 0

  # Sum calculations
  n=len(si)
  
  # Sums of all the preferences
  sum1=sum([prefs[p1][it] for it in si])
  sum2=sum([prefs[p2][it] for it in si])
  
  # Sums of the squares
  sum1Sq=sum([pow(prefs[p1][it],2) for it in si])
  sum2Sq=sum([pow(prefs[p2][it],2) for it in si])	
  
  # Sum of the products
  pSum=sum([prefs[p1][it]*prefs[p2][it] for it in si])
  
  # Calculate r (Pearson score)
  num=pSum-(sum1*sum2/n)
  den=sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
  if den==0: return 0

  r=num/den

  return r

# Returns the best matches for person from the prefs dictionary. 
# Number of results and similarity function are optional params.
def topMatches(prefs,person,n=5,similarity=sim_pearson):
  scores=[(similarity(prefs,person,other),other) 
                  for other in prefs if other!=person]
  scores.sort()
  scores.reverse()
  return scores[0:n]

# Gets recommendations for a person by using a weighted average
# of every other user's rankings
def getRecommendations(domain1,domain2,person,similarity=sim_pearson):
  totals={}
  simSums={}
  for other in domain2:
    # don't compare me to myself
    if other==person: continue
    sim=similarity(domain2,person,other)

    # ignore scores of zero or lower
    if sim<=0: continue
    # print other,sim
    for item in domain1[other]:
	    
      # only score movies I haven't seen yet
      if item not in domain1[person] or domain1[person][item]==0:
        # Similarity * Score
        totals.setdefault(item,0)
        totals[item]+=domain1[other][item]*sim
        # Sum of similarities
        simSums.setdefault(item,0)
        simSums[item]+=sim

  # Create the normalized list
  rankings=[(total/simSums[item],item) for item,total in totals.items()]

  # Return the sorted list
  rankings.sort()
  rankings.reverse()
  return rankings

def loadMovieLens(path='../movielens',file='../u1.base'):
  # Get movie titles
  movies={}
  for line in open(path+'/u.item'):
    (id,title)=line.split('|')[0:2]
    movies[id]=title
  
  # Load data
  prefs={}
  for line in open(path+file):
    (user,movieid,rating,ts)=line.split('\t')
    prefs.setdefault(user,{})
    prefs[user][movieid]=float(rating)
  return prefs

