
# coding: utf-8

# In[9]:

import pandas as pd


# In[1]:

from tools.load_data import GrupoBimboData
gb = GrupoBimboData('/home/gus/Repos/kaggle/data')
gb.load_data('cliente_tabla')
gb.load_data('producto_tabla')
gb.load_data('town_state')
gb.load_data('test')
gb.load_data('train', nrows=2000)


# In[2]:

gb.cliente_tabla.head()


# In[3]:

gb.producto_tabla.head()


# In[4]:

gb.town_state.head()


# In[5]:

gb.test.head()


# In[6]:

gb.train.head()


# ### Data Structure
# Train and test are linked to the three intermediate tables by the following key columns:
# 
# - cliente_tabla -> Cliente_ID
# - producto_tabla -> Producto_ID
# - town_state -> Agencia_ID
# 
# We can merge all the descriptive data into the main dataframes with the pandas merge functionality:

# In[16]:

test = gb.test
test = pd.merge(test, gb.cliente_tabla, on='Cliente_ID')
test.head()


# In[18]:

test = pd.merge(test, gb.producto_tabla, on='Producto_ID')
test.head()


# In[19]:

test = pd.merge(test, gb.town_state, on='Agencia_ID')
test.head()


# In[20]:

# We can now drop Agencia_ID, Producto_ID, and Cliente_ID if we want
test = test.drop(['Agencia_ID', 'Producto_ID', 'Cliente_ID'], axis=1)
test.head()


# In[21]:

# And now the same with train
train = gb.train
train = pd.merge(train, gb.cliente_tabla, on='Cliente_ID')
train = pd.merge(train, gb.producto_tabla, on='Producto_ID')
train = pd.merge(train, gb.town_state, on='Agencia_ID')
train = train.drop(['Agencia_ID', 'Producto_ID', 'Cliente_ID'], axis=1)
train.head()


# In[ ]:



