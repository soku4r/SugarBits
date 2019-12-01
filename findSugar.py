import datetime as dt  # Python standard library datetime  module
import numpy as np
from netCDF4 import Dataset  # http://code.google.com/p/netcdf4-python/
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap, addcyclic, shiftgrid
import xarray as xr


nc_file_t = 'resulttemp.nfc'
nc_file_h = 'rehum.nfc'
ft = Dataset(nc_file_t, mode='r')
fh = Dataset(nc_file_h, mode='r')
t_lons = ft.variables['lon'][:]
t_lats = ft.variables['lat'][:]
t = ft.variables['t'][:]
t_time = ft.variables['time']
t_plev = ft.variables['plev']

h_lons = fh.variables['lon'][:]
h_lats = fh.variables['lat'][:]
h = fh.variables['r'][:]
h_time = fh.variables['time']
h_plev = fh.variables['plev']
print(len(h_time)/6)

file2 = open("resultstzotzis.txt.txt", "w+")


count = 0
longt_saved = []
latit_saved = []
p = 3
for x in range(len(h_lats)):
    for y in range(len(h_lons)):
        for p in range(len(h_plev)):
            i = 0
            found_start = False
            count_part_days = 0
            start = 0
            count_hum = 0
            while(i < len(h_time) and found_start == False):
                if (t[i][p][x][y] - 273.15) > 16 and (t[i][p][x][y] - 273.15) < 35:
                    count_part_days = count_part_days + 1
                    if(h[i][p][x][y] < 60):
                        count_hum = count_hum + 1
                    else:
                        count_hum = 0
                else:
                    count_part_days = 0
                    count_hum = 0
                if(count_hum > 12):
                    count_part_days = 0
                    count_hum = 0
                if(count_part_days >= 5*6):
                    found_start = True
                    start = i - 5*6
                i = i + 1
            j = 0
            bad_day_counter = 0
            possible = True
            while j < len(h_time):
                t_night0clock = t[j][p][x][y] - 273.15
                h_night0clock = h[j][p][x][y]
                j = (j + 1) #% (len(h_time))
                t_night3clock = t[j][p][x][y] - 273.15
                h_night3clock = h[j][p][x][y]
                j = (j + 1)# % (len(h_time))
                t_day10clock = t[j][p][x][y] - 273.15
                h_day10clock = h[j][p][x][y]
                j = (j + 1) #% (len(h_time))
                t_day14clock = t[j][p][x][y] - 273.15
                h_day14clock = h[j][p][x][y]
                j = (j + 1) #% (len(h_time))
                t_day17clock = t[j][p][x][y] - 273.15
                h_day17clock = h[j][p][x][y]
                j = (j + 1) #% (len(h_time))
                t_night21clock = t[j][p][x][y] - 273.15
                h_night21clock = h[j][p][x][y]
                j = (j + 1) #% (len(h_time))
                #t_average_day = t_day17clock 
                t_average_day = (t_day10clock + t_day14clock + t_day17clock)/3
                #t_average_night = t_night3clock
                t_average_night = (t_night0clock + t_night21clock + t_night3clock)/3
                #h_average_day = h_day17clock
                h_average_day = (h_day10clock + h_day14clock + h_day17clock)/3
                #h_average_night =h_night3clock
                h_average_night = ( h_night0clock + h_night21clock + h_night3clock)/3
                if(h_average_day < 60 and h_average_night < 60) or (t_average_day > 35 or t_average_day < 10) or (t_average_night < 3 or t_average_night > 35) :
                    bad_day_counter = bad_day_counter + 1
                else:
                    bad_day_counter = 0
                if(bad_day_counter > 10 or t_average_day < -5 or t_average_night < -8):
                    possible = False
                    #print(j, "stop" )
                    break
                
            if(possible):
                print("good")
                longt_saved.append(h_lons[y])
                latit_saved.append(h_lats[x])
                file2.write(str(h_lons[y]) + " " + str(h_lats[x]) + "\n")
        print(y)
    print(x)


file2.close
