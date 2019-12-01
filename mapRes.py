import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mapbox
from osmapi import OsmApi
import cartopy.crs as ccrs
from datetime import datetime
import traceback


'''
import osmnx as ox

import matplotlib.pyplot as plt

place_name = "Greece"
graph = ox.graph_from_place(place_name)
type(graph)
'''
'''
ax = plt.axes(projection=ccrs.PlateCarree())

#ax.set_extend(20.1500159034, 34.9199876979, 26.6041955909, 41.8269046087)
ax.coastlines()

# Save the plot by calling plt.savefig() BEFORE plt.show()
plt.savefig('coastlines.pdf')
plt.savefig('coastlines.png')

plt.show()
'''
df = pd.read_csv('restz2.csv')
lat = df.longitude
lon = df.latitude


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.scatter(lon, lat)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1,projection=ccrs.PlateCarree())
ax.scatter(lon, lat)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1,projection=ccrs.PlateCarree())
ax.scatter(lon, lat)
ax.coastlines()

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1,projection=ccrs.PlateCarree())
ax.scatter(lon, lat)
ax.stock_img()
ax.coastlines()
fig = plt.figure()

ax = fig.add_subplot(1, 1, 1,projection=ccrs.PlateCarree())
ax.scatter(lon, lat)
ax.stock_img()
ax.coastlines()
ax.gridlines()
plt.show()

'''
geocoder = mapbox.Geocoder(access_token='pk.eyJ1IjoiYWxleHNwaXQiLCJhIjoiY2szbXpnYzZuMGx5cTNsb2R3b3ZkbjgxNSJ9.lZa8_wj3k4Qyh98jggzvjg')



df = pd.read_csv('res.csv')
BBox = ((20.1500159034, 34.9199876979, 26.6041955909, 41.8269046087))

ruh_m = plt.imread('map')
fig, ax = plt.subplots(figsize = (20,20))
ax.scatter(df.longitude, df.latitude, zorder=1, alpha= 0.2, c='b', s=10)
ax.set_title('Greece zaxarokalama')
ax.set_xlim(BBox[0],BBox[1])
ax.set_ylim(BBox[2],BBox[3])
ax.imshow(ruh_m, zorder=0, extent = BBox, aspect= 'equal')
'''