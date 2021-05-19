import numpy as np
from decision_tree import *
import classify as clf


X = np.array([
  [110, 1, 1, 2.8],     
  [95,  2, 1, 2.2],     
  [135, 1, 1, 2.9],     
  [115, 1, 0, 2.0],     
  [100, 2, 0, 2.9],    
  [90,  1, 0, 3.5],     
  [75,  1, 1, 3.1],    
  [85,  2, 1, 3.1],     
  [65,  0, 1, 2.1],     
  [70,  1, 0, 3.0]])    


Y = np.array([FIT, FIT, FIT, FIT, NOT_FIT, FIT, FIT, NOT_FIT, NOT_FIT, NOT_FIT])


scale = np.array([NUMERICAL, CATEGORICAL, CATEGORICAL, NUMERICAL])


decision_tree(X, Y, scale)


y = np.array([clf.classify(X[i, :]) for i in range(len(X))])


if np.all(y == Y):
    print('\nclassification success!\n')
else:
    print('\nclassification fail... :(\n')


print('Test yourself!')
iq = int(input('iq: '))
articles = int(input('articles: '))
obr = int(input('obr: '))
ratio = float(input('ratio: '))

if clf.classify(np.array([iq, articles, obr, ratio])) == FIT:
   print('You are passed!')
else:
   print('You are not passed, sorry...')
