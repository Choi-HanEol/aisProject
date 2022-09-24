import pandas as pd
import numpy as np

pd.set_option('mode.chained_assignment',  None)

data_df=pd.DataFrame({'Message ID':[1, 1, 1, 1, 1, 1, 1, 1, 3, 1],
'Message repeated':[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
'User ID':[227006760, 227006760, 786434, 249191000, 316013198, 366913120, 367156850, 205507490, 366950460, 205035000],
'Navigational status':[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
'ROT-turning':[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
'SOG':[0.0, 0.0, 1.6, 0.0, 0.0, 0.0, 0.1, 0.0, 7.0, 0.0],
'Position accuracy':[0, 1, 1, 1, 1, 0, 0, 1, 0, 1],
'Longtitude':[0.7, 4.25, 5.19, 23.26, 93.22, 159.4, 133.31, 4.20, 141.5, 2.55],
'Latitude':[49.28, 51.14, 51.58, 37.57, 54.19, 18.19, 38.39, 51.52, 27.44, 51.14],
'COG':[36.7, 63.3, 112.0, 247.0, 237.9, 329.5, 175.0, 248.1, 193.3, 0.0],
'True Heading':[511, 511, 511, 511, 511, 299, 511, 511, 193, 511],
'Time Stamp':[14, 15, 15, 12, 16, 16, 15, 16, 17, 15],
'Reserved for regional applications':[0, 0, 4, 1, 0, 0, 0, 4, 0, 0],
'Spare':[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
'RAIM-Flag':[0, 1, 0, 0, 1, 1, 0, 1, 0, 1],
'Communication State':[0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
'remain frame':[1, 0, 1, 1, 5, 6, 0, 1, 0, 2],
'UTC':[11.30, 4.50, 11.30, 11.30, 0.3, 1.18, 4.47, 11.30, 0.0, 1.19]})


sorted_data=data_df.sort_values(by=['User ID', 'UTC'], ascending=True)
sorted_data.reset_index(drop=True, inplace=True)
