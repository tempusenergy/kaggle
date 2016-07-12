
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
print(gp.data)


# In[3]:

# Load data
gp.load_all()


# In[4]:

gp.data['cliente_tabla'].head()


# In[5]:

gp.data['producto_tabla'].head()


# In[6]:

gp.data['town_state'].head()


# In[7]:

gp.data['test'].head()


# In[8]:

# NOTE: By default train is limited to 1000 rows
gp.data['train'].head()


# ### Param Override
# Currently, the only extra params that get sent to `pandas.read_csv` are:
# ```python
# data_load_args = {                                                          
#     'train': {'nrows': 1000},                                               
# }  
# ```
# 
# To override the default for 'train' or to pass through additional params, use `load_arg_override` in `load_all()`, e.g:

# In[9]:

extra_args = data_load_args = {                                                          
    'train': {'nrows': 2000},
    'cliente_tabla': {'index_col': 0},
}
gp.load_all(load_arg_override = data_load_args)


# In[10]:

gp.data['train'].shape


# In[11]:

gp.data['cliente_tabla'].head()


# In[ ]:



