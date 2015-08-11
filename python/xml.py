#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys
import shutil


#替换图片
def change_img(path):
    img = 'init.png'
    child = ['/res/drawable-hdpi/','/res/drawable-ldpi/','/res/drawable-mdpi/','/res/drawable-xhdpi/']        
    #os.cp()
    for c in child:
        shutil.copy(img, path+c)
    
from xml.etree import ElementTree as ET  
#修改manifest
def manifest(path):
    fname = '/AndroidManifest.xml'
    tree = ET.parse(path+fname) #打开xml文档  
    #set write namespace 
    ET.register_namespace("android", "http://schemas.android.com/apk/res/android")
    #ns attri
    name = "{http://schemas.android.com/apk/res/android}"
    #read namespace
    ns = {"android":"http://schemas.android.com/apk/res/android"}
    
    root = tree.getroot()
    activity = root.find("application").findall("activity")
    #print activity
    for a in activity:
        if(a.get('%sname' % name) == 'com.unionpay.uppay.PayActivity'):
            a.set('%sscreenOrientation' % name, 'landscape')
    
    tree.write(path+fname)

    
def unpack(filename):
    print 'unpacking'
    os.system("java -jar apktool_2.0.0b9.jar d %s" % filename)

def packback(path):
    print 'packing'
    os.system("java -jar apktool_2.0.0b9.jar b %s" % path)
    
    apk_name = 'resign_%s.apk' % path
    shutil.copy('%s/dist/%s.apk' % (path,path), apk_name)

    print 'signing'   
    #jarsigner -verbose -keystore mydemo.keystore -signedjar -Note.apk Notes.apk mydemo.keystore
    #jarsigner -sigalg SHA1withRSA -digestalg SHA1 -keystore debug.keystore apkname.apk keyname -storepass password
    

if __name__ == "__main__":
    #do something
    if len(sys.argv) > 1:
        f = sys.argv[1]
        path = f.split('.')[0]
    else:
        print "you must input apk filename"
        sys.exit(1)
    
    unpack(f)
    change_img(path)
    manifest(path)
    packback(path)
 

 
