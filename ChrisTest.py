#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 18:18:21 2017

@author: christopher
"""

from Reference import*
from sys import*
from RocketParameters import*
from RocketStaging import* 

print(inertMass(m_pay, dV[0], Isp[0], f_inert[0]))
print(initialMass(m_pay, f_inert[0], dV[0], Isp[0]))
