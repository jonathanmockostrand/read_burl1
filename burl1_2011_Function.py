################################################################################
#
#Jonathan Strand
#Dept. of Geology & Geophysics, TAMU. 2013-09-11
#Python for Geoscientists
#
################################################################################
#
#This script contains a python function that will read date, sea-level pressure,
#wind speed, and wind direction from a NOAA bouy data file. Wind speed and
#direction has been converted to northward and eastward wind vectors.
#
#http://www.ndbc.noaa.gov/download_data.php?filename=burl1h2011.txt.gz&dir=data/historical/stdmet/
#
################################################################################

import numpy as np
import datetime as dt

def noaa_convert(file):
    '''
    Function:
        noaa_convert(file)

    Input:
        file.dat
        
    Output:
        Date as datetime
        Pressure as sea-level pressure
        wU and wV as Components U and V of wind vector 
        (converted from wind speed and direction)
    '''
    
    f = open(file)

    date = []
    pressure = []
    wU = []
    wV = []

    for line in f.readlines()[2:]:
        data = line.split()
        YYYY = int(data[0])
        MM = int(data[1])
        DD = int(data[2])
        hh = int(data[3])
        mm = int(data[4])
    
        date.append( dt.datetime(YYYY, MM, DD, hh, mm) )
        pressure.append( float(data[12]) )
        wU.append( -(float(data[6])) * np.sin(float(data[5]) * np.pi/180) )
        wV.append( -(float(data[6])) * np.cos(float(data[5]) * np.pi/180) )


    date = np.array(date)
    pressure = np.array(pressure)
    wU = np.array(wU)
    wV = np.array(wV)

    print '#Dates     \n', date
    print '#Pressure     \n', pressure
    print '#wU     \n', wU
    print '#wV     \n', wV

        
#output = noaa_convert('burl1_2011.dat')
