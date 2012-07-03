#!/bin/bash
#PBS -l walltime=0:30:00,ncpus=128,vmem=128GB
#PBS -wd

mpirun -np $PBS_NCPUS make_topog_parallel \
    --mosaic ocean_mosaic.nc \
    --topog_type realistic \
    --topog_file etopo1.nc \
    --topog_field z \
    --scale_factor -1 \
    --fill_shallow \
    --min_depth 40. \
    --bottom_depth 5500. \
