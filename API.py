#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import os
import json
import ast


# In[2]:


def login():
    str_login="python G:/UBIQuant/Code/API/main.py UBIQ_TEAM159 MYk09vgECKnB"
    f=os.popen(str_login,"r")
    return f.read()
      


# In[3]:


def GetGameInfo():
    url=f"http://8.147.116.35:30020/TradeAPI/GetGameInfo"
    up_data={
        'token_ub':'UBIQ_TEAM159_MYk09vgECKnB'
    }
    response=requests.post(url,data=json.dumps(up_data))
    down_data=response.json()
    return down_data


# In[4]:


def Order(instrument,localtime,direction,price,volume):
    url=f"http://8.147.116.35:30020/TradeAPI/Order"
    up_data={
        'token_ub':'UBIQ_TEAM159_MYk09vgECKnB',
        'user_info':"",
        'instrument':instrument,
        'localtime':localtime,
        'direction':direction,
        'price':price,
        'volume':volume
    }
    response=requests.post(url,data=json.dumps(up_data))
    down_data=response.json()
    return down_data


# In[5]:


def Cancel(instrument,localtime,index):
    url=f"http://8.147.116.35:30020/TradeAPI/Cancel"
    up_data={
        'token_ub':'UBIQ_TEAM159_MYk09vgECKnB',
        'user_info':"",
        'instrument':instrument,
        'localtime':localtime,
        'index':index
    }
    response=requests.post(url,data=json.dumps(up_data))
    down_data=response.json()
    return down_data


# In[6]:


def GetActiveOrder():
    url=f"http://8.147.116.35:30020/TradeAPI/GetActiveOrder"
    up_data={
        'token_ub':'UBIQ_TEAM159_MYk09vgECKnB'
    }
    response=requests.post(url,data=json.dumps(up_data))
    down_data=response.json()
    return down_data
    


# In[8]:


def GetTrade(instrument_name):
    url=f"http://8.147.116.35:30020/TradeAPI/GetTrade"
    up_data={
        'token_ub':'UBIQ_TEAM159_MYk09vgECKnB',
        'instrument_name':instrument_name
    }
    response=requests.post(url,data=json.dumps(up_data))
    down_data=response.json()
    return down_data


# In[9]:


def GetLimitOrderBook(instrument_name):
    url=f"http://8.147.116.35:30020/TradeAPI/GetLimitOrderBook"
    up_data={
        'token_ub':'UBIQ_TEAM159_MYk09vgECKnB',
        'instrument_name':instrument_name
    }
    response=requests.post(url,data=json.dumps(up_data))
    down_data=response.json()
    return down_data


# In[11]:


def GetUserInfo():
    url=f"http://8.147.116.35:30020/TradeAPI/GetUserInfo"
    up_data={
        'token_ub':'UBIQ_TEAM159_MYk09vgECKnB'
    }
    response=requests.post(url,data=json.dumps(up_data))
    down_data=response.json()
    return down_data


# In[12]:


def GetInstrumentInfo():
    url=f"http://8.147.116.35:30020/TradeAPI/GetInstrumentInfo"
    up_data={
        'token_ub':'UBIQ_TEAM159_MYk09vgECKnB'
    }
    response=requests.post(url,data=json.dumps(up_data))
    down_data=response.json()
    return down_data

