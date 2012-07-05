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
            'Turbulence': ((0.5*cm, 200*cm), (0.5*second, 200.*second)),
            'Internal Waves': ((100*m, 10*km), (minute, 10*hour)),
            'Tides': ((1e3*km,1e4*km), (hour, 100*hour)),
            'Coastal': ((km, 10*km), (1*day, 10*day)),
            'Fronts': ((km, 20*km), (0.5*day, 20*day)),
            'Eddies': ((5*km, 100*km), (day, 10*week)),
            'Currents': ((50*km, 500*km), (week, season)),
            'Gyres': ((1e3*km, 1e4*km), (10*year, 100*year))
    }
    
    # TODO: Get from scales
    lmin, lmax = 1e-3*m, 100000*km
    tmin, tmax = 1e-3*second, 100*year
    
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
        ax.add_artist(ell_scales[e])
   
    # Labels
    ax.set_title('Ocean Process Length and Time Scales')
    ax.set_xlabel('Length Scale (m)')
    ax.set_ylabel('Time Scale (s)')
    
    plt.savefig('ocean_scales.pdf', bbox_inches='tight')

if __name__ == '__main__':
    main()
