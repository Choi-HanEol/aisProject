import CategorizationByUserID
import folium

# def min_to_degree(L):
#     splited_list = str(L).split('.')
#
#     result = float(splited_list[0]) + float(splited_list[1])/60
#     return result

data_size = len(CategorizationByUserID.sorted_data)
location_data = []
color_list = ['red', 'blue', 'green', 'purple', 'orange', 'darkred',
              'lightred', 'beige', 'darkblue', 'darkgreen', 'cadetblue',
              'darkpurple', 'white', 'pink', 'lightblue', 'lightgreen',
              'gray', 'black', 'lightgray']


m = folium.Map(location=[CategorizationByUserID.sorted_data['Latitude'][0], CategorizationByUserID.sorted_data['Longtitude'][0]], zoom_start=4)


k=0



for i in range(data_size):
    CategorizationByUserID.sorted_data['Latitude'][i] = CategorizationByUserID.sorted_data['Latitude'][i]
    CategorizationByUserID.sorted_data['Longtitude'][i] = CategorizationByUserID.sorted_data['Longtitude'][i]

    folium.Circle(location=[CategorizationByUserID.sorted_data['Latitude'][i], CategorizationByUserID.sorted_data['Longtitude'][i]],
                  popup=CategorizationByUserID.sorted_data['UTC'][i], radius=50, color=color_list[k]).add_to(m)



    location_data.append([CategorizationByUserID.sorted_data['Latitude'][i], CategorizationByUserID.sorted_data['Longtitude'][i]])

    if(i>=data_size-1):
        folium.PolyLine(locations=location_data, tooltip='Polyline', color=color_list[k]).add_to(m)
        break
    if(CategorizationByUserID.sorted_data['User ID'][i] != CategorizationByUserID.sorted_data['User ID'][i+1]):
        folium.PolyLine(locations=location_data, tooltip='Polyline', color=color_list[k]).add_to(m)
        location_data.clear()
        k+=1


m.save('map.html')