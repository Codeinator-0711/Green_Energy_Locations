#import pandas as pd
#df = pd.read_csv("/Users/GabrielNutzer/Green_Energy_Locations/data/sample_addedinfo.csv")
#print(df.head(20))


import geopandas as gpd
import matplotlib.pyplot as plt

fp = "geomap/vg2500_bld.shp"
map_df = gpd.read_file(fp)
map_df.head()
map_df.plot()
