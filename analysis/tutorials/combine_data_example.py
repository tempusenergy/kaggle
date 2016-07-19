
# coding: utf-8

# ## Combining Data...
# This notebook is an example showing how to combine the various datasets into a comprehensive train/test dataframe.
# 
# Train and test are linked to the three intermediate tables by the following key columns:
# 
# - cliente_tabla -> Cliente_ID
# - producto_tabla -> Producto_ID
# - town_state -> Agencia_ID

# In[1]:

from tools.load_data import GrupoBimboData
gb = GrupoBimboData('/home/gus/Repos/kaggle/data')
gb.load_data('cliente_tabla')
gb.load_data('producto_tabla')
gb.load_data('town_state')
gb.load_data('test')
gb.load_data('train', nrows=2000)


# In[2]:

train = gb.combine_data('train', keep_index_cols=False)
train.head()


# In[3]:

test = gb.combine_data('test')
test.head()


# In[ ]:



