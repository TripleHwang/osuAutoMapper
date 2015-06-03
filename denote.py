# -*- coding: utf-8 -*-
"""
Created on Mon May 11 08:53:14 2015

@author: Kergadon
"""
import json
import numpy as np
import matplotlib.pyplot as plt
import os
global tname
global fname
tname=''
fname=''
def getListNames():
  global tname
  global fname
  flist=[]
  for f in os.listdir(os.getcwd()):
    if 'In my room' in f:
      if f.endswith('.list'):
        flist.append(f)
      if f.endswith('.times'):
        tname=f
      if f.endswith('.freqs'):
        fname=f
  return flist
def plotLevel(level,name):
  plt.close()  
  plt.plot(level)
  plt.title(name)
  
  
def extLevelData(levelName):
  fp=open(levelName,'r')  
  LevelData=json.load(fp)
  fp.close()
  del(fp)
  return LevelData
def match2freq(name,fdat):
  for f in fdat:
    if str(int(f)) ==  name[13:-10]:
      return [int(name[13:-10]),f]
def getFreq(nFreq,matchArray):
  for p in matchArray:
    if p[0] == int(nFreq[13:-10]):
      return p[1]
def getDA(names,xvals,yvals,ld):
  da=[]
  for l in ld:
    for n in names:
      if str(int(l[0]))==n[13:-10]:
        da.append(extLevelData(n))
    #print len(da)
  da=np.array(da)
  da=da/np.max(da)
  return(xvals,yvals,da)  
if __name__=='__main__':
  names=getListNames()
  print tname
  xvals=np.fromfile(tname,sep=',')
  print len(xvals)
  d0=extLevelData(names[0])
  print len(d0)
  ld=[]
  yvals=np.fromfile(fname,sep=',')
  for n in names:
    ld.append(match2freq(n,yvals))
  ld=np.array(ld)
  ld=np.sort(ld,0)
  #print ld[2]
  #print ld.transpose()[1]
  import matplotlib.cm as cm
  print 'trying to plot'
  DAt=getDA(names,xvals,yvals,ld)
  fig, ax = plt.subplots()
  DA=DAt[2]
  print type(DA)
  DA=DA
  p = ax.pcolor(xvals, yvals, DA, cmap=cm.RdBu, vmin=0, vmax=1)
  cb = fig.colorbar(p, ax=ax)