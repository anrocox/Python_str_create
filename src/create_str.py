#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 8, 2014

@author: anroco

How to create a string in python?

¿Como definir un string en python?
'''

#enclosed in single quotes
s = 'allows embedded "double" quotes.'
print(s)

#enclosed in double quotes
s = "allows embedded 'single' quotes."
print(s)

#triple single or double quotes allows multiple lines
s = '''Textual data in Python
is handled with str objects.
Strings are immutable sequences
of Unicode code points.'''
print(s)

#the \ can be used to escape quotes. \n (new line), \t (tab), \\ (\), etc.
s = 'She said "isn\'t".'
print(s)

#created from other objects using the str constructor. returns object.__str__()
s = str(27364)
print(s)
