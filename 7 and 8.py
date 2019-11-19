#!/usr/bin/env python
# coding: utf-8

# In[11]:


import matplotlib.pyplot as plt
plt.style.use('classic')
import numpy as np
import pandas as pd
import seaborn as sns
sns.set()

data = np.random.multivariate_normal([0, 0], [[5, 2], [2, 2]], size=2000)
data = pd.DataFrame(data, columns=['x', 'y'])

for col in 'xy':
    plt.hist(data[col], density=True, alpha=0.5)

plt.title('Histogram')
plt.show()




for col in 'xy':
    sns.kdeplot(data[col], shade=True)

plt.title('Kernel Density Estimation')
plt.show()

sns.distplot(data['x'])
sns.distplot(data['y']);
plt.title('Histogram and KDE Combined')
plt.show()

sns.kdeplot(data);
plt.title('Two-Dimensional KDE Plot')
plt.show()


# In[12]:


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

# importing scikit learn with make_blobs 
from sklearn.datasets.samples_generator import make_blobs 
  
# creating datasets X containing n_samples 
# Y containing two classes 
X, Y = make_blobs(n_samples=500, centers=2, 
                  random_state=0, cluster_std=0.40) 
  
# plotting scatters  
plt.scatter(X[:, 0], X[:, 1], c=Y, s=50, cmap='spring'); 
plt.show()


# creating line space between -1 to 3.5  
xfit = np.linspace(-1, 3.5) 
  
# plotting scatter 
plt.scatter(X[:, 0], X[:, 1], c=Y, s=50, cmap='spring') 
  
# plot a line between the different sets of data 
for m, b, d in [(1, 0.65, 0.33), (0.5, 1.6, 0.55), (-0.2, 2.9, 0.2)]: 
    yfit = m * xfit + b 
    plt.plot(xfit, yfit, '-k') 
    plt.fill_between(xfit, yfit - d, yfit + d, edgecolor='none',  
    color='#AAAAAA', alpha=0.4) 
  
plt.xlim(-1, 3.5); 
plt.show() 

# import support vector classifier 
from sklearn.svm import SVC # "Support Vector Classifier" 
clf = SVC(kernel='linear') 

# fitting x samples and y classes 
clf.fit(x, y) 

clf.predict([[120, 990]]) 

clf.predict([[85, 550]]) 


# In[ ]:




