#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Style to make, by default, a single column plot of ApJ quality.
'''

import matplotlib.pyplot as plt

style = {
    'lines.linewidth' : 1.3,
    'lines.linestyle' : '-',

    'font.size' : 11,
    'font.family' : 'serif',
    'font.serif' : ['Times New Roman', 'Times', 'Bitstream Vera Serif',
                    'New Century Schoolbook', 'Century Schoolbook L', 'Utopia',
                    'ITC Bookman', 'Bookman', 'Nimbus Roman No9 L', 'Palatino',
                    'Charter', 'serif'],

    'axes.linewidth' : 1.2,
    'axes.grid' : 'False',
    'axes.xmargin' : 0.05,
    'axes.ymargin' : 0.05,
    'axes.labelsize' : 12.,

    'xtick.major.size' : 6,
    'xtick.minor.size' : 3,
    'xtick.major.width' : 1.,
    'xtick.minor.width' : 1.,
    'xtick.labelsize' : 11,

    'ytick.major.size' : 6,
    'ytick.minor.size' : 3,
    'ytick.major.width' : 1.,
    'ytick.minor.width' : 1.,
    'ytick.labelsize' : 11,


    'legend.numpoints' : 1,
    'legend.scatterpoints' : 1,
    'legend.fontsize' : 10,
    'legend.frameon' : False,

    'figure.figsize': (3.5, 3.5),
    'figure.dpi' : 150,
    'figure.subplot.left' : 0.18,
    'figure.subplot.right' : 0.95,
    'figure.subplot.bottom' : 0.15,
    'figure.subplot.top' : 0.95,

    'image.interpolation' : 'nearest',

    'errorbar.capsize' : 0.,

    'savefig.dpi' : 100,
}
