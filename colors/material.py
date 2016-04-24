#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Loads the colors into an object names colors with the different colors being
properties.
'''

import matplotlib.pyplot as plt

## Loading the colors in hex

global_vars = {}
local_vars = {}
with open('material_palette_hex.py') as f:
    code = compile(f.read(), 'meterial_palette_hex.py', 'exec')
    exec(code, None, local_vars)

class _Colors(object):
    def __init__(self, dict):
        self.__dict__.update(dict)

colors = _Colors(local_vars)

## Done loading the colors

## matplotlib sequences

color_sequence = ['indigo', 'green', 'orange', 'red', 'blue', 'light_green',
                  'deep_orange', 'pink', 'light_blue', 'lime', 'brown',
                  'purple', 'cyan', 'amber', 'grey', 'deep_purple', 'teal',
                  'blue_grey']

color_cycle = plt.cycler('color', [colors.__dict__['{}500'.format(s)]
                                   for s in color_sequence])
color_cycle += plt.cycler('mec', [colors.__dict__['{}900'.format(s)]
                                  for s in color_sequence])

style = {'axes.prop_cycle': color_cycle}
