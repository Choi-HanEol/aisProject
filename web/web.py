from idlelib import tooltip

import os, time, sys, io
import pandas as pd
import numpy as np
import json
import requests
import branca
import folium
import csv
from folium import plugins
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import QWebEngineView  # pip install PyQtWebEngine

### 데이터 추출
f = open('UlsanAIS_220917.csv')
data = csv.reader(f)
header = next(data)
data_list = []

# 532~612
idx = 2  # 노란색 영역처리 데이터 인덱싱
for row in data:
    if (idx >= 532 and idx <= 612):
        data_list.append(row)
    idx += 1

ais_df = pd.DataFrame(data=data_list, columns=header)
data_size = len(ais_df)
f.close()


class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI(0)

    def initUI(self, i):
        super().__init__()
        self.setWindowTitle('AIS Viewer')
        self.window_width, self.window_height = 1600, 1200
        self.setMinimumSize(self.window_width, self.window_height)

        # self.timer = QTimer(self)
        # self.timer.start(1000/30)
        # self.timer.timeout.connect(self.updateMarker(20))

        layout = QVBoxLayout()
        self.setLayout(layout)
        self.m = folium.Map(location=[35.5193, 129.3733], zoom_start=12)
        self.m.add_child(plugins.MeasureControl())  # 마우스 좌표값(위도,경도)얻기

        ### 보트 마커
        # for i in range(data_size):
        #     self.boatMarker = plugins.BoatMarker(
        #         location=(ais_df['Latitude'][i], ais_df['Longitude'][i]),
        #         color='blue',
        #         heading=ais_df['True Heading\n(HDG)'][i],
        #         popup="- MMSI: %d\n- Latitude: %f\n- Longitude: %f\n- index: %d" % (int(ais_df['MMSI'][i]), float(ais_df['Latitude'][i]), float(ais_df['Longitude'][i]), int(i))
        #     )
        #     self.boatMarker.add_to(m)
        #     self.update()
        #     self.show()

        self.boatMarker = plugins.BoatMarker(
            location=(ais_df['Latitude'][i], ais_df['Longitude'][i]),
            color='blue',
            heading=ais_df['True Heading\n(HDG)'][i],
            popup="- MMSI: %d\n- Latitude: %f\n- Longitude: %f\n- index: %d" % (
            int(ais_df['MMSI'][i]), float(ais_df['Latitude'][i]), float(ais_df['Longitude'][i]), int(i))
        )
        self.boatMarker.add_to(self.m)

        # exit_code = 0
        # # def main():
        # i = int(sys.argv[1])
        # plugins.BoatMarker(
        #     location=(ais_df['Latitude'][i], ais_df['Longitude'][i]),
        #     color='blue',
        #     heading=ais_df['True Heading\n(HDG)'][i],
        #     popup="- MMSI: %d\n- Latitude: %f\n- Longitude: %f\n- index: %d" % (int(ais_df['MMSI'][i]), float(ais_df['Latitude'][i]), float(ais_df['Longitude'][i]), int(i))
        # ).add_to(m)

        # if i >= data_size:
        #     exit_code = 1

        # 울산항만공사 좌표에 마크
        folium.Marker([35.5193, 129.3733],
                      popup="울산항",
                      tooltip="울산항만공사").add_to(self.m)

        # 특정 좌표를 기점으로 원 표시

        folium.Circle([35.5193, 129.3733],
                      color='tomato',
                      radius=1500,
                      tooltip='울산항 구역').add_to(self.m)

        # 각 부두 마크
        folium.Marker([35.5305, 129.3753],
                      popup="제1부두",
                      tooltip="울산항 제1부두",
                      icon=folium.Icon('red', icon='star'),
                      ).add_to(self.m)

        folium.Marker([35.5259, 129.3723],
                      popup="제2부두",
                      tooltip="울산항 제2부두",
                      icon=folium.Icon('red', icon='star'),
                      ).add_to(self.m)

        folium.Marker([35.522, 129.3751],
                      popup="제3부두",
                      tooltip="울산항 제3부두",
                      icon=folium.Icon('red', icon='star'),
                      ).add_to(self.m)

        folium.Marker([35.5208, 129.3753],
                      popup="제4부두",
                      tooltip="울산항 제4부두",
                      icon=folium.Icon('red', icon='star'),
                      ).add_to(self.m)

        folium.Marker([35.519, 129.3751],
                      popup="제5부두",
                      tooltip="울산항 제5부두",
                      icon=folium.Icon('red', icon='star'),
                      ).add_to(self.m)

        data1 = io.BytesIO()
        self.m.save(data1, close_file=False)
        webView = QWebEngineView()
        webView.setHtml(data1.getvalue().decode())
        layout.addWidget(webView)

        line = QLineEdit(self)
        line.setFixedHeight(100)
        line.setStyleSheet("color:red; font-size:100px;")
        layout.addWidget(line)

        # self.timer = QTimer(self)
        # self.timer.start(1000/30)
        # self.timer.timeout.connect(self.updateMarker)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            # self.i += 1
            # self.boatMarker = plugins.BoatMarker(
            #     location=(ais_df['Latitude'][self.i], ais_df['Longitude'][self.i]),
            #     color='blue',
            #     heading=ais_df['True Heading\n(HDG)'][self.i],
            #     popup="- MMSI: %d\n- Latitude: %f\n- Longitude: %f\n- index: %d" % (int(ais_df['MMSI'][self.i]), float(ais_df['Latitude'][self.i]), float(ais_df['Longitude'][self.i]), int(self.i))
            # )
            # self.boatMarker.add_to(self.m)
            # self.update()
            self.close()

    # def drawMarker(self, )


# class UpdateData(QThread):
#     update_date = pyqtSignal(MyApp)  # pyqt5   python3 str，  Qstring

#     def run(self):
#         cnt = 1
#         while cnt <= 81:
#             self.update_date.emit(MyApp(cnt))  #
#             cnt += 1
#             time.sleep(1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet('''
        QWidget {
            font-size: 35px;
        }
    ''')
    myApp = MyApp()
    # myApp.show()

    # update_data_thread = UpdateData()
    # update_data_thread.update_date.connect(myApp.updateMarker)  #
    # update_data_thread.start()
    # for i in range(81):
    #     time.sleep(1)
    #     myApp.updateMarker(i)
    # myApp.show()

    myApp.show()
    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')

# if __name__ == "__main__":
#     main(0)
#     time.sleep(1)
#     os.execl(sys.executable, sys.executable, *sys.argv)