from idlelib import tooltip

import pandas as pd
import numpy as np
import json
import requests
import branca
import folium
import csv
from folium import plugins

### 데이터 추출
f = open('UlsanAIS_220917.csv')
data = csv.reader(f)
header = next(data)
data_list = []

# 532~612
idx = 2    #노란색 영역처리 데이터 인덱싱
for row in data:
    if(idx >= 532 and idx <= 612):
        data_list.append(row)
    idx += 1

ais_df = pd.DataFrame(data=data_list, columns=header)
data_size = len(ais_df)
f.close()


m = folium.Map(location=[35.5193, 129.3733], zoom_start=14)
m.add_child(plugins.MeasureControl())   #마우스 좌표값(위도,경도)얻기

### 보트 마커
for i in range(data_size):
    plugins.BoatMarker(
        location=(ais_df['Latitude'][i], ais_df['Longitude'][i]),
        color='blue',
        heading=ais_df['True Heading\n(HDG)'][i],
        popup="- MMSI: %d\n- Latitude: %f\n- Longitude: %f\n- index: %d" % (int(ais_df['MMSI'][i]), float(ais_df['Latitude'][i]), float(ais_df['Longitude'][i]), int(i))
    ).add_to(m)

#울산항만공사 좌표에 마크
folium.Marker([35.5193, 129.3733],
              popup="울산항",
              tooltip="울산항만공사").add_to(m)



#특정 좌표를 기점으로 원 표시

folium.Circle([35.5193, 129.3733],
                    color='tomato',
                    radius = 1500,
                    tooltip='울산항 구역').add_to(m)

#각 부두 마크
folium.Marker([35.5305, 129.3753],
              popup="제1부두",
              tooltip="울산항 제1부두",
              icon=folium.Icon('red', icon='star'),
             ).add_to(m)

folium.Marker([35.5259, 129.3723],
              popup="제2부두",
              tooltip="울산항 제2부두",
              icon=folium.Icon('red', icon='star'),
             ).add_to(m)

folium.Marker([35.522, 129.3751],
              popup="제3부두",
              tooltip="울산항 제3부두",
              icon=folium.Icon('red', icon='star'),
             ).add_to(m)

folium.Marker([35.5208, 129.3753],
              popup="제4부두",
              tooltip="울산항 제4부두",
              icon=folium.Icon('red', icon='star'),
             ).add_to(m)

folium.Marker([35.519, 129.3751],
              popup="제5부두",
              tooltip="울산항 제5부두",
              icon=folium.Icon('red', icon='star'),
             ).add_to(m)


m.save('BoatMarker.html')