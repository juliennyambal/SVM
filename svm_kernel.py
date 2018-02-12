#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 17:11:16 2018

@author: julien_nyambal
"""

import matplotlib.pyplot as plt

import numpy as np

#Generate some points
x_plus = [1,2,3,3,4,4,4,5,5]

y_plus = [0,1,1,2,1,2,3,1,2]

x_minus = [1,1,1,2,2,3,3]

y_minus = [3,4,5,4,5,4,5]


#weight vector which is the normal vector to the hyperplane
w = [-1,1]

#norm of the vector w
w_norm = np.sqrt(np.square(w[0])+np.square(w[1]))

#unit vector
u = np.array([(w[0]/w_norm),(w[1]/w_norm)])

#norms keeps the distances from all the points to the hyperplane
norms = []

for i in range(len(x_plus)):
    p_dot = np.dot(u,np.array([x_plus[i],y_plus[i]]))
    p = p_dot * u
    p_norm = np.sqrt(np.square(p[0])+np.square(p[1]))
    
    print 'Distance to margin of (',x_plus[i],',',y_plus[i],') is: ',p_norm

    norms.append(p_norm)

for i in range(len(x_minus)):
    p_dot = np.dot(u,np.array([x_minus[i],y_minus[i]]))
    p = p_dot * u
    p_norm = np.sqrt(np.square(p[0])+np.square(p[1]))
    
    print 'Distance to margin of (',x_minus[i],',',y_minus[i],') is: ',p_norm
    
    norms.append(p_norm)

print 'The max margin is: ', norms[np.argmin(norms)]*2

x = np.linspace(1,5)
y = x

y_pos = x + 1
y_neg = x +-1

plt.plot(x,y,c='green')
plt.plot(x,y_pos,c='red')
plt.plot(x,y_neg,c='blue')

plt.scatter(x_plus,y_plus,marker='+',c='red',s=80)
plt.scatter(x_minus,y_minus,marker='o',c='blue',s=80)
plt.show()