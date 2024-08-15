import folium
from folium.plugins import HeatMap
import pandas as pd

df = pd.read_excel('merged_sheet.xlsx')

df_sign = df[df['type'] == 'ROAD_SIGN_POST']
df_light = df.loc[(df['type'] == 'FLASH_LIHGT_POST') | (df['type'] == 'ROAD_LIGHT_POST')]

heatmap = folium.Map(location=[55.7558, 37.6173], zoom_start=12)

heat_data = [[row['latitude'], row['longitude']] for index, row in df_sign.iterrows()]
HeatMap(heat_data, gradient={'0':'#dce3fa', '0.25':'#9aadec','0.5':'#5e77d3', '0.75':'#193468','1': '#202735'}).add_to(folium.FeatureGroup(name='Дорожные знаки').add_to(heatmap))

heat_data = [[row['latitude'], row['longitude']] for index, row in df_light.iterrows()]
HeatMap(heat_data, gradient={'0':'#ffefea', '0.25':'#fbd9d3','0.5':'#ffb09c', '0.75':'#ee2400','1': '#900000'}).add_to(folium.FeatureGroup(name='Опоры освещения').add_to(heatmap))

folium.LayerControl().add_to(heatmap)

heatmap.save('heatmap.html')