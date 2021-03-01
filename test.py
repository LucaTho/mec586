# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 16:29:53 2021

@author: lucat
"""
import numpy as np
from math import *
import matplotlib.pyplot as plt
from scipy.integrate import odeint
# constants
p0 = 1013.25 * 10**2  # atmospheric pressure (Pa)
R = 8.314462  # gas constant (J / (K.mol))
Mwat = 0.01801  # molecular mass of water (kg / mol)
Mair = 0.028976  # molecular mass of air (kg / mol)


temp = 273

psat = 10 ** 3 * 0.61121 * exp((18.678 - (temp - 273.15) / 234.5) * (temp - 273.15) / (temp - 273.15 + 257.14))  # vapor pressure


pv1 = p0 * Mwat / (R * temp)
pv2 =  psat * Mwat / (R * temp)
print (p0, psat, pv1, pv2)