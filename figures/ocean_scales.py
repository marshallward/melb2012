#!/usr/bin/env python
# coding: utf-8

import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import numpy as np

def main():
    
    # Time units
    second = 1.
    minute = 60.*second
    hour = 60*minute
    day = 24*hour
    week = 7*day
    month = 2629744.
    season = 3*month
    year = 12*month
    
    cm = 1e-2
    m = 100.*cm
    km = 1000.*m
    
    # Data points
    proc_scales = {
            'Capillary\nWaves': ((0.2*cm, 5*cm), (0.5e-2*second, 2e-1*second)),
            'Turbulence': ((0.5*cm, 2*m), (0.5*second, 200.*second)),
            'Sound\nWaves': ((10*m, 200*m), (0.5e-2*second, 2e-1*second)),
            'Surface\nWaves': ((m, 50*m), (0.1*second, minute)),
            'Internal\nWaves': ((0.1*km, 100*km), (minute, 20*hour)),
            'Mixed Layer': ((m, 200*m), (minute, 2*hour)),
            'Tides': ((5e2*km,5e3*km), (hour, 20*hour)),
            'Mesoscale\nEddies': ((km, 250*km), (0.5*day, 20*week)),
            'Wind-\nDriven': ((0.2e3*km, 10e3*km), (month, 50*year)),
            'THC': ((500e3, 20e3*km), (20*year, 1000*year))
    }
    
    # TODO: Get from scales
    lmin, lmax = 1e-3*m, 100000*km
    tmin, tmax = 1e-3*second, 2000*year
    
    xmin, xmax = np.log10((lmin, lmax))
    ymin, ymax = np.log10((tmin, tmax))
    
    # Create plot
    fig, ax = plt.subplots(nrows=1, ncols=1)
    ax.set_xscale('log')
    ax.set_yscale('log')
    
    ax.set_xlim([lmin, lmax])
    ax.set_ylim([tmin, tmax])
    
    # Make some ellipses
    ell_scales = {}
    for p in proc_scales:
        ls, le = proc_scales[p][0]
        ts, te = proc_scales[p][1]
        
        xs, xe = (np.log10((ls, le)) - xmin) / (xmax - xmin)
        ys, ye = (np.log10((ts, te)) - ymin) / (ymax - ymin)
        
        xm = 0.5 * (xs + xe)
        ym = 0.5 * (ys + ye)
        
        w = xe - xs
        h = ye - ys
        
        ell_scales[p] = Ellipse(xy=(xm,ym), width=w, height=h,
                                transform=ax.transAxes)
    
    for e in ell_scales:
        ell = ell_scales[e]
        ax.add_artist(ell)
        ell.set_facecolor(np.random.rand(3))
        ax.text(ell.center[0], ell.center[1], e,
                ha='center', va='center', transform=ax.transAxes)
   
    # Labels
    ax.set_title('Ocean Process Length and Time Scales')
    ax.set_xlabel('Length Scale (m)')
    ax.set_ylabel('Time Scale (s)')
    
    plt.savefig('ocean_scales.pdf', bbox_inches='tight')

if __name__ == '__main__':
    main()
