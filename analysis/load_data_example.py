
# coding: utf-8

# ## Loading Data...
# This notebook is an example showing how to load the data with a custom loading class

# In[1]:

# Import GrupoBimboData
from tools.load_data import GrupoBimboData


# In[2]:

# Initialise with file containing downloaded datafiles (from https://www.kaggle.com/c/grupo-bimbo-inventory-demand/data)
# NOTE: no need to unzip files
gp = GrupoBimboData('/home/gus/Repos/kaggle/data')
print(dir(gp))


# In[3]:

# Load data
gp.load_data('cliente_tabla')
gp.cliente_tabla.head()


# In[4]:

gp.load_data('producto_tabla')
gp.producto_tabla.head()


# In[5]:

gp.load_data('town_state')
gp.town_state.head()


# In[6]:

gp.load_data('test')
gp.test.head()


# In[7]:

# And with additional args...
gp.load_data('train', nrows=1000)
print(gp.train.shape)
gp.train.head()


# In[ ]:



