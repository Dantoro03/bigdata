
### Extraer canciones de la playlist

```python
import spotipy  
import time  
import pandas as pd  
import json  
from spotipy.oauth2 import SpotifyClientCredentials  
from tqdm import tqdm  
import glob

SPOTIPY_CLIENT_ID =   'myclient'
SPOTIPY_CLIENT_SECRET = 'mysecret'  
  
auth_manager = SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET)  
sp = spotipy.Spotify(auth_manager=auth_manager)  
  
playlists = ['Myplaylist']  
offset = 0   
contador = 0  
  
def query_principal(p, offset, contador):  #Definimos una función para crear un documento json por cada 100 canciones de cada playlist
    query = sp.playlist_items(p, fields=None, offset=offset, market=None) #Llamamos a la query
    if query['next'] == None:  #Si la query no tiene varible `next`, es decir ha recogido ya todas las canciones de la playlist
        with open(f'api-res/playlist-{p}-{contador}-response.json', 'w', encoding='UTF-8') as f:  #Abrimos un archivo Json  
            json.dump(query, f, ensure_ascii=False, indent=4)  #Metemos la query dentro del json
        pass  
    else:  #Si todavia quedan canciones en la playlist
        with open(f'api-res/playlist-{p}-{contador}-response.json', 'w', encoding='UTF-8') as f:  #Abrimos un archivo json
            json.dump(query, f, ensure_ascii=False, indent=4)  #Metemos la query dentro del json
        contador = contador+1  
        offset = offset+100  #Sumamos 100 puntos al offset
        time.sleep(1)  
        query_principal(p, offset, contador)  #Volvemos a lanzar la función con el offset aumentado para que la respuesta comience 100 canciones despues de la ultima respuesta
  
for p in playlists:  #Creamos un bucle que recorra la lista de playlist
    query_principal(p, offset, contador) #Lanzamos la función
```

### Extraer nombre, artista, popularity y id de cada canción

```python 
files = glob.glob("api-res/playlist-*.json")  #abrimos todos los json que hemos creado
llista_cancons = [] #Creamos una lista donde recoger todos los datos de las canciones

for file in files: #Creamos una función que recorra todos los archivos json
	playlist_id = file.split("-")[2] #sacamos el id de la playlist del nombre del archivo
	print(playlist_id)
	f = open(file, encoding="utf8") #Abrimos el json
	data = json.load(f) #Cargamos el json
	tracks = data["items"] 
	for track in tracks: #Recorremos cada canción dentro del json y sacamos las variables que necesitamos
		playlist = playlist_id 
		name = track['track']['name']
		art_name = track['track']['artists'][0]["name"]
		t_id = track['track']['id']
		popularity = track['track']['popularity']
		tup = ({"playlist_id":playlist, "id":t_id, "name":name, "artists_name":art_name, "popularity":popularity}) #Creamos una tupla con un diccionario con los datos que queremos extraer
		llista_cancons.append(tup) #Guardamos la tupla en la lista de canciones

with open(f'data.json', 'w', encoding='UTF-8') as f: #Guardamos todos los datos en un json
	json.dump(llista_cancons, f, ensure_ascii=False, indent=4)
```

## Extraer Features y crear DF
```python
f = open('data.json', encoding="utf8")  #Abrimos el json con los datos de todas las canciones
data = json.load(f)  #Cargamos el json
  
total_data = []  #Creamos una lista para llenarla con los datos
  
for d in tqdm(data): #Recorremos el json canción por canción
    features = sp.audio_features(d['id']) #Utilizamos la id de la cancion para extraer los features de cada canción
    d["features"] = features #Creamos una variable de dataframe con las features
    track_df = pd.DataFrame.from_dict(d, orient="columns") #Creamos un Dataframe con la información de las canciones del json
    features_data = pd.DataFrame.from_dict(features, orient='columns') #Creamos un Dataframe con las features de cada canción   
    final_track_df = pd.concat([track_df, features_data], axis=1) #Unimos los dos dataframes uno
    total_data.append(final_track_df) #Guardamos este Dataframe en la lista de dataframes
    time.sleep(1)  
total_df = pd.concat(total_data)  #Unimos todos los dataframes en uno final
total_df.to_csv("total_df.csv", index=False) #Convertimos el dataframe final en csv
```