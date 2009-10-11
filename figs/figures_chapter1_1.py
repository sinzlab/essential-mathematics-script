# -*- coding: utf-8 -*-
"""
figures_chapter1_1.py
"""
from pylab import *
from numpy import *

def fac( n ):
    if n<=1:
        return n
    return n*fac(n-1)
    
def Poisson( k, lam, dt ):
    return exp(-lam*dt)*(lam*dt)**k/fac(k)
    
def ISI( mu, s ):
    return mu*exp(-mu*s)
    
def createPoisson():
    x = arange(0,10,0.01)
    y1 = zeros_like(x)
    y2 = zeros_like(x)
    y3 = zeros_like(x)
    y4 = zeros_like(x)
    for ii in xrange(len(x)):
        y1[ii] = Poisson(1,1,x[ii])
        y2[ii] = Poisson(1,2,x[ii])
        y3[ii] = Poisson(1,0.5,x[ii])
        y4[ii] = Poisson(3,1,x[ii])
    clf()
    plot(x,y1, label='$k=1$, $\lambda=1$')
    plot(x,y2, label='$k=1$, $\lambda=2$')
    plot(x,y3, label='$k=1$, $\lambda=0.5$')
    plot(x,y4, label='$k=3$, $\lambda=1$')
    xlabel('time [s]')
    ylabel('probability')
    legend()
    
def createISI():
    x = arange(0,1,0.001)
    y1 = zeros_like(x)
    y2 = zeros_like(x)
    y3 = zeros_like(x)
    for ii in xrange(len(x)):
        y1[ii] = ISI(1,x[ii])
        y2[ii] = ISI(2,x[ii])
        y3[ii] = ISI(0.5,x[ii])
    clf()
    plot(x,y1, label='$\mu=1$')
    plot(x,y2, label='$\mu=2$')
    plot(x,y3, label='$\mu=0.5$')
    xlabel('time [s]')
    ylabel('probability')
    legend()