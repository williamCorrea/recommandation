# -*- coding: utf-8 -*-
"""
Created on Tue May 26 10:15:48 2015

@author: correabe
"""

import numpy as np
import pylab as pl
import scipy.stats as spy
import scipy.spatial as spa
from sklearn.decomposition import PCA

#centroids = [[5,5], [10.8,5]]
#centroids = [[5,5], [10,10], [5,10]]
#centroids = [[0.1,0.1], [0.45,0.1], [0.8,0.1], [0.75,0.35], [0.55,0.55], [0.15,0.65],[0.75,0.65],
#             [0.1,0.9], [0.45,0.9], [0.85,0.9]]




def remplirdataset(taille, ratio, distri=None,mu=0,sigma=0,shape=0,scale=0):
    global centroids
    dataset = np.empty((taille,15))
    cont=0
    if distri is None:    
        for i in centroids:
            #print i
            max_x = i[0]+ratio
            min_x = i[0]-ratio
            max_y = i[1]+ratio
            min_y = i[1]-ratio

            for j in range(0,taille/len(centroids)):
                #print j
                #x = np.random([0.0,1.0])
                #print x            
                dataset[cont]= ((max_x-min_x)*np.random.random()+min_x, (max_y-min_y)*np.random.random()+min_y)
            
                cont=cont+1
    elif distri =='Normal':
        dataset[:,0] = np.random.normal(mu,sigma,taille)
        dataset[:,1] = np.random.normal(mu,sigma,taille)
        dataset[:,2] = np.random.normal(mu,sigma,taille)
        dataset[:,3] = np.random.normal(mu,sigma,taille)
        dataset[:,4] = np.random.normal(mu,sigma,taille)
        dataset[:,5] = np.random.normal(mu,sigma,taille)
        dataset[:,6] = np.random.normal(mu,sigma,taille)
        dataset[:,7] = np.random.normal(mu,sigma,taille)
        dataset[:,8] = np.random.normal(mu,sigma,taille)
        dataset[:,9] = np.random.normal(mu,sigma,taille)
        dataset[:,10] = np.random.normal(mu,sigma,taille)
        dataset[:,11] = np.random.normal(mu,sigma,taille)
        dataset[:,12] = np.random.normal(mu,sigma,taille)
        dataset[:,13] = np.random.normal(mu,sigma,taille)
        dataset[:,14] = np.random.normal(mu,sigma,taille)
    elif distri=='gamma':
        dataset[:,0] = np.random.gamma(shape,scale,taille)
        dataset[:,1] = np.random.gamma(shape,scale,taille) 
    elif distri=='pareto':
        dataset[:,0] = np.random.pareto(1,taille)
    return dataset

def getVectorsFromDataset(dataset,dist='cosine'):
    z,w = dataset.shape
    print z,w
    #vectors = np.zeros((((z*(z-1))/2),w))
    vectors = np.empty((z*z,2))
    cont=0
    for i in range(0,z):
        for j in range(0,z):
        #for j in range((i+1),z):
            if dist == 'cosine':
                
                vectors[cont]=spa.distance.cosine(dataset[j],dataset[i])
            else:
                #print np.correlate(dataset[j],dataset[i])
                vectors[cont]=spy.pearsonr(dataset[j],dataset[i])
                
            cont=cont+1
            #print dataset[j]-dataset[i]
    return vectors


#x = remplirdataset(taille=150,ratio=0,distri='Normal',mu=2,sigma=10)
#x = remplirdataset(100,0.15,distri='pareto',mu=0,sigma=2,shape=1,scale=10)
#x = remplirdataset(150,1.5)

shape=3
lower=0.01
size=1000
upper=1

x = s = np.random.pareto(shape,1000)


pl.figure(3)
pl.subplot(211)
n, bins, patches = pl.hist(x, 50, normed=1,alpha=0.5)
y = pl.matplotlib.mlab.normpdf(bins,mu,sigma)
pl.plot(bins,y,'r--')

print pow((3*pow(0.01,3)),3)/pow(1,4)

#==============================================================================
# mu = np.mean(x[:,0])
# sigma = np.std(x[:,0])
# 
# pl.figure(3)
# pl.subplot(211)
# n, bins, patches = pl.hist(x[:,0], 50, normed=1,alpha=0.5)
# y = pl.matplotlib.mlab.normpdf(bins,mu,sigma)
# pl.plot(bins,y,'r--')
#==============================================================================


#==============================================================================
# pl.figure(1)
# pl.subplot(211)
# pl.scatter(x[:,0],x[:,1])
# pl.show()
# 
# pl.figure(2)
# pl.subplot(211)
# pl.scatter(vector[:,0],vector[:,1])
#==============================================================================
pl.show()


#==============================================================================
# mu = np.mean(x[:,0])
# sigma = np.std(x[:,0])
# 
# pl.figure(3)
# pl.subplot(211)
# n, bins, patches = pl.hist(x[:,0], 50, normed=1,alpha=0.5)
# y = pl.matplotlib.mlab.normpdf(bins,mu,sigma)
# pl.plot(bins,y,'r--')
#==============================================================================
pl.show()


#==============================================================================
# mu = np.mean(vector[:,0])
# sigma = np.std(vector[:,0])
# bins=100
# pl.figure(4)
# pl.subplot(211)
# n, bins, patches = pl.hist(vector[:,0],bins,normed=False,alpha=0.5)
# y = pl.matplotlib.mlab.normpdf(bins,mu,sigma)
# pl.plot(bins,y,'r--')
# pl.show()
# 
# print mu
#==============================================================================
print sigma


#pl.setp(patches, 'facecolor', 'g', 'alpha', 0.75)



    
        