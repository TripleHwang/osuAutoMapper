# -*- coding: utf-8 -*-
"""
Created on Sat May 09 20:42:51 2015

@author: Kergadon
"""

import scipy.io.wavfile as wf
import numpy as np
filename='In my room162.wav'
data=wf.read(filename)
wd=data[1]
rate=data[0]
wdt=wd.transpose()
wdr=wdt[0]
wdl=wdt[1]
wdr=np.array(wdr)
wdl=np.array(wdl)
#import pylab
import matplotlib.mlab as pylab
import matplotlib.pyplot as plt

def xlspecgram(wdat,name=None,debug=False):
  wdat=np.array(wdat)  
  ns=len(wdat)//1000000+1
  wdd=np.array_split(wdat,ns)
  sdatar=[]
  plt.xlabel('Time(seconds)')
  plt.ylabel('freqeuncy (Hz)')
  
  for n in range(len(wdd)):
    sd=pylab.specgram(wdd[n],Fs=44100,NFFT=512,pad_to=512*2)
    sdatar.append(sd)
    if debug:        
      if name!=None:
        ts=name + ' sample number ' + str(n)
      else:
        ts='sample number ' + str(n)
        plt.title(ts)
      ss=ts+'.png'
      plt.savefig(ss,dpi=400)
    plt.close()
  n=0
  levs={}  
  print 'sg done'  
  for f in sdatar[0][1]:
    levs[str(f)]=[]
  for sdat in sdatar:
    for n in range(len(sdat[1])):
      levs[str(sdat[1][n])]+=sdat[0][n].tolist()
    print 'part ' + str(n) + ' of ' + str(len(wdd)) + ' done'
    n+=1    
  return [sdatar,levs]    
  


if __name__=='__main__':
  sdatar=xlspecgram(wdr,name='right',debug=False)
  levelsRight=sdatar[1]
  #del(sdatar)
  #sdatal=xlspecgram(wdl,name='right',debug=False)
  #levelsLeft=sdatal[1]
  print 'start'
  import json
  #import pickle
  tlen=len(wdr)/float(data[0])
  kf=[]
  for k in levelsRight.keys():
    kf.append(float(k))
  kf.sort()
  ksf=[]
  for k in kf:
    ksf.append(str(k))
  
  plt.close()
  ta=np.linspace(0,tlen,len(levelsRight['0.0']))
  ta.tofile(filename[:-4]+'x.times',sep=',')
  fa=sdatar[0][0][1]
  fa.tofile(filename[:-4]+'y.freqs',sep=',')
  if False:
    for freq in ksf:
      print "saving "+ str(int(float(freq))) +" Hz data"
      fp=open(filename[:-4]+str(int(float(freq)))+'right.list','w+')  
      json.dump(levelsRight[freq],fp)    
      fp.close()
  print 'x saved'
#  fpl=open(filename+'left.dic','w')
#  json.dump(levelsRight,fpr)
#  json.dump(levelsLeft,fpl)
#  fpr.close()
#  fpl.close()

  print 'libs saved'
  '''
  levels=levelsRight  
  
  tlen=len(wdr)/float(data[0])
  kf=[]
  for k in levels.keys():
    kf.append(float(k))
  kf.sort()
  ksf=[]
  for k in kf:
    ksf.append(str(k))
  plt.close()
  ta=np.linspace(0,tlen,len(levels['0.0']))
  for ks in np.array_split(ksf,20):
    for freq in ks:
      print 'ploting ' + float(freq)/float(ksf[-1])*100 + ' % done'
      ts=str(int(float(freq)))+' amplitude vs time'
      plt.plot(ta,levels[freq])    
      plt.xlabel('Time(sconds)')
      plt.ylabel('amplitude (a.u.)')
      plt.title(ts)
      fs=ts+'.svg'
      plt.draw()
      plt.savefig(fs)
      plt.close()    
  '''      