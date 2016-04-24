#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Flat ui colors (http://flatuicolors.com)
'''

# from . import plt
import matplotlib.pyplot as plt

class _Colors(object):
    def __init__(self):
        self.blue = '#3498db'
        self.red = '#e74c3c'
        self.green = '#2ecc71'
        self.orange = '#e67e22'
        self.yellow = '#f1c40f'
        self.purple = '#9b59b6'
        self.gray = '#95a5a6'
        self.teal = '#1abc9c'
        self.bluegray = '#34495e'

        self.dark_blue = '#2980b9'
        self.dark_red = '#c0392b'
        self.dark_green = '#27ae60'
        self.dark_orange = '#d35400'
        self.dark_yellow = '#f39c12'
        self.dark_purple = '#8e44ad'
        self.dark_gray = '#7f8c8d'
        self.dark_teal = '#16a085'
        self.dark_bluegray = '#2c3e50'

colors = _Colors()

color_sequence = ['blue', 'red', 'green', 'orange', 'purple', 'yellow', 'gray',
                  'teal', 'bluegray']

color_cycle = plt.cycler('color', [colors.__dict__[s] for s in color_sequence])
color_cycle += plt.cycler('mec', [colors.__dict__['dark_{}'.format(s)]
                                  for s in color_sequence])

style = {'axes.prop_cycle': color_cycle}
