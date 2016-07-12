
# coding: utf-8

# ## Loading Data...
# This notebook is an example showing how to load the data with a custom loading class

# In[5]:

# Add repo directory to path so that we can do the relative import below
# Probably a better way to do this!
import sys
sys.path.append('/home/gus/Repos/kaggle')

# Import GrupoBimboData
from tools.load_data import GrupoBimboData


# In[10]:

# Initialise with file containing downloaded datafiles (from https://www.kaggle.com/c/grupo-bimbo-inventory-demand/data)
# NOTE: no need to unzip files
gp = GrupoBimboData('/home/gus/Repos/kaggle/data')
print(gp.data)


# In[12]:

# Load data
gp.load_all()


# In[13]:

gp.data['cliente_tabla'].head()


# In[14]:

gp.data['producto_tabla'].head()


# In[15]:

gp.data['town_state'].head()


# In[16]:

gp.data['test'].head()


# In[17]:

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

# In[18]:

extra_args = data_load_args = {                                                          
    'train': {'nrows': 2000},
    'cliente_tabla': {'index_col': 0},
}
gp.load_all(load_arg_override = data_load_args)


# In[19]:

gp.data['train'].shape


# In[20]:

gp.data['cliente_tabla'].head()


# In[ ]:



