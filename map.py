import CategorizationByUserID
import folium

data_size = len(main.sorted_data)
location_data = []
color_list = ['red', 'blue', 'green', 'purple', 'orange', 'darkred',
              'lightred', 'beige', 'darkblue', 'darkgreen', 'cadetblue',
              'darkpurple', 'white', 'pink', 'lightblue', 'lightgreen',
              'gray', 'black', 'lightgray']


m = folium.Map(location=[main.sorted_data['Latitude'][0], main.sorted_data['Longtitude'][0]], zoom_start=4)


k=0

for i in range(data_size):

    folium.Circle(location=[main.sorted_data['Latitude'][i], main.sorted_data['Longtitude'][i]],
                  popup=main.sorted_data['UTC'][i], radius=50, color=color_list[k]).add_to(m)

    location_data.append([main.sorted_data['Latitude'][i], main.sorted_data['Longtitude'][i]])

    if(i>=data_size-1):
        folium.PolyLine(locations=location_data, tooltip='Polyline', color=color_list[k]).add_to(m)
        break
    if(main.sorted_data['User ID'][i] != main.sorted_data['User ID'][i+1]):
        folium.PolyLine(locations=location_data, tooltip='Polyline', color=color_list[k]).add_to(m)
        location_data.clear()
        k+=1


m.save('map.html')
