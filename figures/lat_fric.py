#!/usr/bin/env python
# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt

def main():
    dx = 1e4
    A2 = 5e2
    A4 = 1e10
    N = 1000
    
    n = np.arange(N, dtype='f8')
    k = (np.pi/dx) * (n / N)
    
    tau2 = A2 * k**2
    tau4 = A4 * k**4
    
    fig, ax = plt.subplots(1,1)
    
    ax.plot(n, tau2)
    ax.plot(n, tau4)
    ax.legend(['Laplacian', 'Biharmonic'])
   
    ax.yaxis.set_ticklabels(['-', '5000', '2500', '1667', '1250', '1000'])

    ax.set_title('Laplacian vs Biharmonic Viscosities')
    ax.set_xlabel('Mode number')
    ax.set_ylabel('Decay timescale (sec)')

    plt.savefig('lateral_friction.pdf', bbox_inches='tight')
    #toticks = lambda(x: list(x.astype('|S5')))
    #ax.xaxis.set_ticklabels(ticks)


if __name__ == '__main__':
    main()
