#!/usr/bin/env python
# coding: utf-8

# In[11]:


import requests
import os
import json
import re
import warnings
import ast
token='UBIQ_TEAM159_MYk09vgECKnB'


# In[2]:


def login():
    str_login="python G:/UBIQuant/Code/API/main.py UBIQ_TEAM159 MYk09vgECKnB"
    f=os.popen(str_login,"r")
    return f.read()
      


# In[ ]:


def relogin():
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
    down_dict=eval(down_data)
    if down_dict.get('status')=='Invalid User':
        relogin()
        return 0
    else:
        ret_data=down_dict.pop('status')
        return ret_data


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
    down_dict=eval(down_data)
    return down_dict


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
    down_dict=eval(down_data)
    return down_dict


# In[6]:


def GetActiveOrder():
    url=f"http://8.147.116.35:30020/TradeAPI/GetActiveOrder"
    up_data={
        'token_ub':'UBIQ_TEAM159_MYk09vgECKnB'
    }
    response=requests.post(url,data=json.dumps(up_data))
    down_data=response.json()
    down_dict=eval(down_data)
    return down_dict
    


# In[4]:


def GetTrade(instrument_name):
    url=f"http://8.147.116.35:30020/TradeAPI/GetTrade"
    up_data={
        'token_ub':'UBIQ_TEAM159_MYk09vgECKnB',
        'instrument_name':instrument_name
    }
    response=requests.post(url,data=json.dumps(up_data))
    down_data=response.json()
    down_dict=eval(down_data)
    return down_dict


# In[6]:


def GetLimitOrderBook(instrument_name):
    url=f"http://8.147.116.35:30020/TradeAPI/GetLimitOrderBook"
    up_data={
        'token_ub':'UBIQ_TEAM159_MYk09vgECKnB',
        'instrument_name':instrument_name
    }
    response=requests.post(url,data=json.dumps(up_data))
    down_data=response.json()
    down_dict=eval(down_data)
    def getbid_queue():
        bid_queue=down_dict.get('bidprice')
        return bid_queue
    
    def getask_queue():
        ask_queue=down_dict.get('askprice')
        return ask_queue
    
    ret_data=down_dict.pop('bidprice')
    ret_data=ret_data.pop('askprice')
    return ret_data


# In[7]:


def GetUserInfo():
    url=f"http://8.147.116.35:30020/TradeAPI/GetUserInfo"
    up_data={
        'token_ub':'UBIQ_TEAM159_MYk09vgECKnB'
    }
    response=requests.post(url,data=json.dumps(up_data))
    down_data=response.json()
    down_dict=eval(down_data)
    return down_dict


# In[9]:


def GetInstrumentInfo():
    url=f"http://8.147.116.35:30020/TradeAPI/GetInstrumentInfo"
    up_data={
        'token_ub':'UBIQ_TEAM159_MYk09vgECKnB'
    }
    response=requests.post(url,data=json.dumps(up_data))
    down_data=response.json()
    down_dict=eval(down_data)
    return down_dict


# In[12]:


def zero_divide(x,y):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        res=np.divide(x,y)
    if hasattr(y,"__len__"):
        res[y==0]=0
    elif y==0:
        res=0
        
    return res


# In[13]:


def score(instrument):
    LOB_dict=GetLimitOrderBook(token,instrument)
    userInfo_dict=GetUserInfo()
    info_list=userInfo_dict.get('rows')
    str=instrument
    pattern=r'\d+'
    n=re.findall(pattern,str)
    target_dict=info_list[n]
    target_volume=target_dict.get('target_volume')
    remain_volume=target_dict.get('remain_volume')
    trade_value=target_dict.get('trade_volume')
    trade_volume=target_volume-remain_volume
    vwap=zero_divide(trade_value,trade_volume)
    twap=LOB_dict.get('lob')['twap']
    return 1-vwap/twap
    

