#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
General plots to test the colors.
'''

import sys
import numpy as np
import matplotlib.pyplot as plt

def lines(ax, nlines):
    x = np.arange(5)
    for i in range(nlines):
        ax.errorbar(x, 0.2 * x + i * 0.3, yerr=0.13, marker='s', ls='-',
                    lw='1.5', capsize=0)

if __name__ == "__main__":
    from flatui import colors as flat
    fig = plt.figure(1)
    ax = fig.add_subplot(111)
    lines(ax, 9)
    ax.set_xlim(-0.1, 4.1)
    plt.savefig('junk.pdf')
