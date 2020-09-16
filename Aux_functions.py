# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 10:45:49 2020

@author: massa
"""
import numpy as np
from bizdays import Calendar, load_holidays 

holidays = load_holidays('Brazil.txt')
cal = Calendar(holidays, ['Sunday', 'Saturday'], name = 'Brazil')

def janela_previa(d_inicial, d_final):
    wdw = cal.bizdays(d_inicial, d_final)
    if cal.isbizday(d_inicial) == False:
        d_inicial = cal.adjust_previous(d_inicial)
    else:
        d_inicial = d_inicial        
    di = cal.offset(d_inicial, -wdw)
    
    return di

def Delta_T(d_inicial, d_final, d_count):
    
    if d_count == '252':
        du = 252
        Delta = (cal.bizdays(d_inicial, d_final))
        T = Delta/du
        return (round(T,4))
    
    elif d_count == '360':
        du = 360
        Delta = (np.busday_count(d_inicial, d_final))
        T = Delta/du
        
        return (round(Delta_T,4))
    
def Yd_conv(yd, conv):
    
    if conv.lower() == 'dtoc':
        i_conv = np.exp(yd) - 1     
        return round(i_conv,6)
    
    elif conv.lower() == 'ctod':
        i_conv = np.log(1+yd)
        return round(i_conv,6)