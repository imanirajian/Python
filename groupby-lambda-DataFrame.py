#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


products_raw = {"Apple": {"price":1000, "weight":10},
                "Camera": {"price":80000, "weight":100},
                "Laptop": {"price":901000, "weight":4500},
                "Watch": {"price":70100, "weight":90},
                "Bag": {"price":4000, "weight":50}}

transaction_raw = {0: {"product":"Apple", "count":3, "discount":500, "date":"01-21-2021"},
                   1: {"product":"Camera", "count":1, "discount":500, "date":"11-20-2020"},
                   2: {"product":"Apple", "count":20, "discount":1000, "date":"01-03-2021"},
                   3: {"product":"Bag", "count":2, "discount":0, "date":"01-04-2020"},
                   4: {"product":"Bag", "count":2, "discount":100, "date":"01-05-2021"},
                   5: {"product":"Bag", "count":6, "discount":1000, "date":"01-10-2021"},
                   6: {"product":"Watch", "count":1, "discount":100, "date":"05-18-2020"},
                   7: {"product":"Laptop", "count":1, "discount":0, "date":"01-16-2021"},
                   8: {"product":"Camera", "count":4, "discount":9000, "date":"08-08-2020"}}


# In[3]:


products = pd.DataFrame(products_raw).T
print( products )


# In[4]:


transactions = pd.DataFrame(transaction_raw).T
print( transactions )


# In[5]:



# sort products by price
# Notes: 
#       1- By default ascending=True
#       2- Sort is outplace, i.e., after sorting products remain unchanged
#          You can set inplace=True if you want
print( products.sort_values(by="price") )


# In[6]:



# sort products by price descendingly
print( products.sort_values(by="price", ascending=False) )


# In[7]:



# Lets sort by print(index
print( products.sort_index() )


# In[8]:


print( transactions )


# In[9]:



# How many distinct transactions are according to the names of products?
print( len( transactions.groupby("product") ) ) 
print( transactions.groupby("product").ngroups )


# In[10]:



# How many times each products have been sold?
print( transactions.groupby("product").sum()["count"] )


# In[11]:



# Maximum discount for each products?
print( transactions.groupby("product").max()["discount"] )


# In[12]:



# Minimum of each feature with respect to distinct product names
print( transactions.groupby("product").min() )
# or
print( transactions.groupby("product").agg(np.min) ) # or min
# or
print( transactions.groupby("product").agg("min") )
# or
print( transactions.groupby("product").aggregate("min") )


# In[13]:



# Total price of each product
# We need to join products to see the price of each product
trans_prods = transactions.join(products, on="product")
print(trans_prods)

# Then times each product count with price subtract discount
trans_prods.groupby("product").apply(lambda g: print( g["product"].values[0] + ":\t", (g["count"]*g["price"]-g["discount"]).sum() ))


# In[14]:


print( transactions.join(products, on="product") )


# In[15]:



# Pass custom function to calculate total weight for each transaction
def get_total_weight(group):
    return np.sum(group["count"])*group["weight"].iloc[0]
    
print( transactions.join(products, on="product").groupby("product").apply(get_total_weight) )


# In[16]:



# Maximum discount for each products?
print( transactions.groupby("product").max()["discount"] )


# In[17]:



# Think about the output
def f(column):
    print(column.name)
    return len(column.name)
    
print( transactions.groupby("product").agg(f) )


# In[18]:



# Putting all together
# Sort transaction by name, then (same names) by count, then (same names and count) by discount (ascendingly)

# We want this result:
target = transactions.sort_values(by=["product", "count", "discount"])
print( target )

print("-"*5)

# Note: DataFrame().groupby() returns a "DataFrameGroupBy" object which is a list of tuples
group_by_names = transactions.groupby("product", group_keys=False) # By name, Search for group_keys=False effect
print( group_by_names )

print("-"*5)

# Lets see what is "DataFrameGroupBy" is
for group_name, group_dataframe in group_by_names:
    print(group_name, ":")
    print(group_dataframe)
    
def print_groupby(group):
    for group_name, group_dataframe in group:
        print(group_name, ":")
        print(group_dataframe)
# or
print()
group_by_names.apply(lambda group_by_name: print(group_by_name))

# or 
print()
group_by_names.apply(print)

# Note: DataFrame().groupby() by default sort the values, so Apple comes first and Watch goes the last

print("-"*5)

# Now we must sort each group seperately by count, then discount
groups_by_names_counts_discount = group_by_names.apply(
    lambda group_by_name: group_by_name.groupby("count", group_keys=False).apply(
        lambda group_by_name_count: group_by_name_count.groupby("discount", group_keys=False).apply(
            lambda g:g
        )
    ) 
)
# Lets see 
print(groups_by_names_counts_discount)
        
# Compare to target:
print( target )

