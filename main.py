import pandas as pd
import numpy as np

data_df=pd.DataFrame({'Message ID':[1, 1, 1, 2, 3, 1, 2, 3, 1, 3 ],
'Message repeated':[2, 3, 1, 3, 5, 7, 1, 3, 5, 7],
'User ID':[127, 127, 127, 128, 129, 130, 103, 125, 128, 130],
'Navigational status':[0, 1, 4, 6, 2, 7, 9, 3, 8, 1],
'ROT-turning':[560, 124, 2376, 345, 8, 1232, 458, 387, 469, 235],
'SOG':[61.2, 42.3, 12.6, 53.3, 90.1, 83.2, 31.2, 64.1, 66.6, 32.6 ],
'Position accuracy':[0, 1, 1, 1, 1, 0, 1, 1, 0, 1],
'Longtitude':[27.5, 25.4, 12.3, 64.2, 12.4, 38.7, 46.8, 23.4, 95.5, 54.3 ],
'Latitude':[5.5, 2.4, 2.6, 8.3, 3.7, 7.3, 3.6, 9.8, 4.5, 8.3],
'COG':[95.9, 93.2, 93.1, 84.1, 82.4, 74.1, 82.6, 91.6, 18.5, 19.4],
'True Heading':[351, 123, 235, 325, 321, 234, 292, 181, 290, 86],
'Time Stamp':[53, 32, 53, 21, 41, 44, 12, 52, 29, 31],
'Reserved for regional applications':[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
'Spare':[0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
'RAIM-Flag':[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
'Communication State':[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
'remain frame':[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
'UTC':[15.17, 17.19, 12.45, 23.45, 12.54, 8.06, 9.15, 19.09, 22.11, 13.25]})


sorted_data=data_df.sort_values(by=['User ID', 'UTC'], ascending=True)
sorted_data.reset_index(drop=True, inplace=True)
