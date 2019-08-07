#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


print(np.__version__)
np.show_config()


# In[3]:


Z=np.zero(10)
print（Z）


# In[4]:


Z = np.zeros((10,10))
print("%d bytes" % (Z.size * Z.itemsize))


# In[8]:


numpy.info(numpy.add)


# In[9]:


Z = np.zeros(10)
Z[4] = 1
print(Z)


# In[10]:


Z = np.arange(10,50)
print(Z)


# In[11]:


Z = np.arange(50)
Z = Z[::-1]
print(Z)


# In[12]:


Z = np.arange(9).reshape(3,3)
print(Z)


# In[13]:


nz = np.nonzero([1,2,0,0,4,0])
print(nz)


# In[14]:


Z = np.eye(3)
print(Z)


# In[15]:


Z = np.random.random((3,3,3))
print(Z)


# In[16]:


Z = np.random.random((10,10))
Zmin, Zmax = Z.min(), Z.max()
print(Zmin, Zmax)


# In[17]:


Z = np.random.random(30)
m = Z.mean()
print(m)


# In[18]:


Z = np.ones((10,10))
Z[1:-1,1:-1] = 0
print(Z)


# In[19]:


Z = np.ones((5,5))
Z = np.pad(Z, pad_width=1, mode='constant', constant_values=0)
print(Z)


# In[22]:


print(0 * np.nan)


# In[23]:


print(np.nan == np.nan)


# In[24]:


print(np.nan - np.nan)


# In[25]:


print(0.3 == 3 * 0.1)


# In[26]:


Z = np.diag(1+np.arange(4),k=-1)
print(Z)


# In[27]:


Z = np.zeros((8,8),dtype=int)
Z[1::2,::2] = 1
Z[::2,1::2] = 1
print(Z)


# In[28]:


print(np.unravel_index(100,(6,7,8)))


# In[29]:


Z = np.tile( np.array([[0,1],[1,0]]), (4,4))
print(Z)


# In[30]:


Z = np.random.random((5,5))
Zmax, Zmin = Z.max(), Z.min()
Z = (Z - Zmin)/(Zmax - Zmin)
print(Z)


# In[31]:


olor = np.dtype([("r", np.ubyte, 1),
                  ("g", np.ubyte, 1),
                  ("b", np.ubyte, 1),
                  ("a", np.ubyte, 1)])
color


# In[32]:


Z = np.dot(np.ones((5,3)), np.ones((3,2)))
print(Z)


# In[33]:


Z = np.arange(11)
Z[(3 < Z) & (Z <= 8)] *= -1
print(Z)


# In[34]:


print(sum(range(5),-1))


# In[35]:


print(sum(range(5),-1))


# In[ ]:




