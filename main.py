import pandas as pd

#Llegeixo les columnes necesaries
df=pd.read_csv("feb_23_es_simple.csv", sep="\t", usecols=['captured_at','viewer_count','game_name','streamer_name'])


#Ejercicio 1
#Agrupo totes les files segons quan han estat capturades y sumo tot els viewers counts
df2 = df.groupby("captured_at")['viewer_count'].sum().reset_index()
#exporto les dades a un dataframe
df2.to_csv("Ejercicio_1.csv")

'''#Si la memoria no dona, utilitzar aquest codi
list=[] #creo una llista per afegir les dades de cada chunk

#llegeixo el dataframe per chunks
df = pd.read_csv("feb_23_es_simple.csv", chunksize=10000, sep='\t', usecols=['captured_at','viewer_count'])

#itero dins del chunk
for chunk in df:
    df2 = chunk.groupby('captured_at')['viewer_count'].sum().reset_index() #agrupo el chunk segons l'hora de captura i sumo els viewers
    list.append(df2) #afegeixo les dades a la llista que hem creat abans
    print(chunk)

final_frame_1 = pd.concat(list) #concateno la llista de chunks
final_frame_2 = final_frame_1.groupby("captured_at")['viewer_count'].sum() #torno a agrupar y sumar per si algun chunk a tallat les dades
final_frame_2.to_csv("viewers_date.csv") #exporto el csv
'''
#Ejercicio 2

#Creo dos dataframes un per el total de captures y altre per el total de views
capturas = df['game_name'].value_counts().reset_index()
views = df.groupby("game_name")['viewer_count'].sum().reset_index()

#corretgeixo els noms de les columnes
capturas.rename(columns = {'game_name':'capturas', 'index':'game_name'}, inplace = True)

#uneixo els dos dataframes (queda ordenat per captures)
df3 = pd.merge(capturas, views)

df3.to_csv('Ejercicio_2.csv', index=True)

#Ejercicio 3
#agrupo segons la captura i el joc i sumo els viewers de cada categoria
df4 = df.groupby(["captured_at", "game_name"])['viewer_count'].sum().reset_index()
df4_2 = pd.merge(df3, df4)
df4_2.to_csv("Ejercicio_3.csv", index=True)



#Ejercicio 4

streams = df['streamer_name'].value_counts().reset_index()
viewers = df.groupby("streamer_name")['viewer_count'].sum().reset_index()

#corretgeixo els noms de les columnes
streams.rename(columns = {'streamer_name':'captures', 'index':'streamer_name'}, inplace = True)

#uneixo els dos dataframes (queda ordenat per captures)
df5 = pd.merge(streams, viewers)

df5.to_csv('Ejercicio_4.csv', index=True)


#Ejercicio 5

#Agrupo el dataframe per les captures y calculo la desviació estandard dels viewers
df6 = df.groupby("captured_at")['viewer_count'].std().round(4).reset_index()
#Canvio el nom de la columna de viewer_count per desviacio
df6.rename(columns = {'viewer_count':'desviacio'}, inplace = True)

df6.to_csv('Ejercicio_5.csv', index=True)
