import pandas as pd
import math
import numpy as np

# Чтение данных из файла Excel
df = pd.read_excel('merged_sheet.xlsx')

df['column'] = round((df['longitude'] - df['longitude'].min())/((df['longitude'].max() - df['longitude'].min())/8))
df['row'] = round((df['latitude'] - df['latitude'].min())/((df['latitude'].max() - df['latitude'].min())/5))

#df['column1'] = round((df['column'] - df['column'].min())/((df['column'].max() - df['column'].min())/8))
#df['row1'] = round((df['row'] - df['row'].min())/((df['row'].max() - df['row'].min())/5))

df['number'] = df['column'] + 9*df['row']


sorted_df = df.sort_values(by='number')

#print(sorted_df.groupby(['number', 'type'])['type'].count())

df_agr = sorted_df.groupby(['number', 'type'])['type'].count().reset_index(name='count')

df_agr.to_excel('agr.xlsx', index = False)

sorted_df.to_excel(f"sort.xlsx", index=False)

#chunk_size = 2000
#print(math.ceil(len(sorted_df)/ chunk_size))
#for i, chunk in enumerate(np.array_split(sorted_df, math.ceil(len(sorted_df)/ chunk_size))):
#    chunk.to_excel(f'file_{str(i).zfill(3)}_{chunk_size}.xlsx', index=False)