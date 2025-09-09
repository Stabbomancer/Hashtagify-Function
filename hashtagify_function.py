# -*- coding: utf-8 -*-
"""
Created on Mon Sep  8 22:56:26 2025

@author: Samuel Geltman
"""

def hashtagify(str):
    str = str.title()
    str = str.replace(' ','')
    str = "#{}".format(str)
    print(str)

hashtagify("Hello world")