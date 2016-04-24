#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


def lines(ax, nlines):
    x = np.arange(5)
    for i in range(nlines):
        ax.errorbar(x, 0.2 * x + i * 0.3, yerr=0.13, marker='s', ls='-',
                    lw='1.5', capsize=0)

def test_apj1col():

    from apj1col import style as apj1col
    with plt.style.context(apj1col):
        fig = plt.figure(1)
        ax = fig.add_subplot(111)
        lines(ax, 3)
        ax.set_xlim(-0.1, 4.1)
        ax.set_xlabel('X-label')
        ax.set_ylabel('Y-label')
    plt.savefig('/tmp/apj1_example.pdf')


