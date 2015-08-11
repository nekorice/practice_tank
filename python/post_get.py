#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import os


import urllib  
import urllib2  
def http_post(url, data):  
    req = urllib2.Request(url)  
    #对数组参数的支持
    temp = [] 
    for k,vs in data.items():
        if isinstance(vs, list):
            for v in vs:
                temp.append((k, v))           
        else:
            temp.append((k,vs))
    data = urllib.urlencode(temp)         
     
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())  
    response = opener.open(req, data)  
    return  response.read()


def http_get(host, data):
 
    data = urllib.urlencode(temp) 
    url = '%s?%s' % (host, data)
    
    try:
        res_data = urllib2.urlopen(url, timeout=5)
        res = res_data.read()    
        return res
    except Exception,args:
        log.error(traceback.format_exc())
        return ''
    

if __name__ = '__main__':
    pass