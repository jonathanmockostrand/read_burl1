#
#Jonathan Strand
#Dept. of Geology & Geophysics, TAMU. 2013-09-03
#Python for Geoscientists
#
#Script to read burl1 data from noaa
#http://www.ndbc.noaa.gov/download_data.php?filename=burl1h2011.txt.gz&dir=data/historical/stdmet/
#
import numpy as np
import datetime as dt

f = open('burl1_2011.dat')

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