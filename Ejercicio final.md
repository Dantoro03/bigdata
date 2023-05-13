
### Extraer canciones de la playlist

```python

SPOTIPY_CLIENT_ID =   'myclient'
SPOTIPY_CLIENT_SECRET = 'mysecret'  
  
auth_manager = SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET)  
sp = spotipy.Spotify(auth_manager=auth_manager)  
  
playlists = ['myplaylist']  
o = 0  
  
llista_respostes = []  
  
def query_principal(p, o):  
    query = sp.playlist_items(p, fields=None, limit=100, offset= o, market=None)    
    llista_respostes.append(query)    
    if query['next'] == None:
        pass
    else:
        o += 100        
        time.sleep(1)        
        query_principal(p, o)
for p in playlists:  
    llista_respostes.clear()
    query_principal(p, o)
      
with open('jsondata.json', 'w', encoding='UTF-8') as f:  
    json.dump(llista_respostes, f, ensure_ascii=False, indent=4) 

```

### Extraer nombre, artista y id de cada canción

```python 
f = open('jsondata.json', encoding="utf8")  
  
data = json.load(f)  
  
llista_cancons = []  
for resposta in data:  
    cancons = resposta['items']  
    for canco in cancons:  
        name = canco['track']['name']  
        art_name = canco['track']['artists'][0]["name"]  
        t_id = canco['track']['id']  
        tup = ({"id":t_id, "name":name, "artists_name":art_name})  
        llista_cancons.append(tup)  
  
with open('fuegodata.json', 'w', encoding='UTF-8') as f:  
    json.dump(llista_cancons, f, ensure_ascii=False, indent=4)
```