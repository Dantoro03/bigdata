
## Unir llistes
.Append

``` python
llista_1= ["Adria", "Carles", "Julia"]
llista_2= ["Joan", "Maria", "Roger"]

```

## Condicionants
### cadenes 

```python
llista_noms =  ["Carme, Jaume"]

for nom in llista_noms:
	if nom == "Joan":
		print (f"{nom}si que és en joan")
	else:
		print (f"{nom}no és en joan")
```

### Integer

```python

llista = [1,2,3,4,5,6,7,8,9,10]

for n in numeros:
	if n < 6:
		print (f"{n} es menor que 6")
	elif n == 6:
		print (f"{n} es igual que 6")
	elif n > 6:
		print (f"{n} es major que 6")	
```

### Tuple

``` python

llista_1 = [6,9]
llista_2 = ["josep", "cristina"]
llista_final = []
for nota, nom in zip(llista_1, llista_2)
	conjunt = (nota, nom)
	llista_final.append(conjunt)
print (llista_final)

for t in llista_final:
	nota = t[0]
	nom = t[1]
print(nota,nom)
```

## Funcions integrades

### len

```python

numeros = [1,2,3,4]

x = len(numeros)

print(len(numeros))
print (x)
```

Index
```python 
alumnes = ["Sandra", "Roger", "Emma", "Carlos", "Albert", "Adrià", "Joan"]

nom = "Joan"

if nom in alumnes:
	position = alumnes.index(nom) + 1
	print (f"sí, en la posició {position}")
else:
	print ("no")


```
### convertir cadena en int

``` python
var = "5"
varnum = int(var)
```

Set

```python 
alumnes = ["adrià", "carla", "joan", "pere", "pere", "carla"]

print (len(set(alumnes)))
```
## Ejercicios

 ### ejercicios 1 
``` python
a = "esto es un ejercicio"  
  
print(a)  
  
nota = 9  
  
assi = "Analitica digital"  
  
print (f"En la assignatura {assi} he obtenido un {nota}")

x = (f"En la assignatura {assi} he obtenido un {nota}")
```

ejercicio 2

``` python 
notas = ["5", "7", "6", "4", "8", "2"]  
  
alumnos = ["jaume", "carla", "pere", "adrià", "rafael", "agnès"]  
  
  
for nota, alumno in zip(notas, alumnos):  
    notas_int = int(nota)  
    notas_final = notas_int +1  
    print(f"{alumno} ha tret {notas_final}")
	
```

ejercicio 3

```python
llista = [  "david",  "dani","marta","jaume",  "adria", "carla",  "joan",  "pere", "carla",  "pere",  "adria",  "quico",  "pere",  "joan",  "agustí",  "adria",  "joan",  "adria",  "siscu",  "carles",  "dani",  "carla"  ]  
y = len(set(llista))  
print (f"han assitit {y} persones a les sesions")  
llista2  = []  
llista3 = set(llista)  
  
for n in llista3:  
    a = llista.count(n)  
    if a > 2:  
        llista2.append(n)  
x=len(llista2)  
p = ((x/y)*100)  
  
print(f"un {p}% ha anat a més d'una sesió")
```

Ejercició 4

``` python
notes = ["5","3","7","8","9.5","4","6,2"]  
alumnes = ["adria","agnès","josep","rafa","cristina","Gemma","Eduard"]  
  
for nota, alumno in zip(notes, alumnes):  
  
    print(f"{alumno} ha tret un {nota}")  
  
notes2 = []  
x=0  
for m in notes:  
    if "." in m:  
        m_arreglada = float(m)  
        notes2.append(m_arreglada)  
    elif "," in m:  
        m_arreglada = float(m.replace(",", "."))  
        notes2.append(m_arreglada)  
    else:  
        m_arreglada = int(m)  
        notes2.append(m_arreglada)  
print(notes2)  
print(round(sum(notes2)/len(notes2),1))  
  
nota_max = max(notes2)  
posicio_max = notes2.index(nota_max)  
print(f"{nota_max} de {alumnes[posicio_max]}")  
  
nota_min = min(notes2)  
posicio_min = notes2.index(nota_min)  
print(f"{nota_min} de {alumnes[posicio_min]}")
```

# Introducción a Pandas

## Exportar a CSV

```python
import pandas as pd #principio del doc
#al final del doc
df = pd.DataFrame({
	"col1" : a
	"col2" : b
	"col3" : c	   
	}) 
# amb tupla
df = pd.DataFrame(tupla, llista_columnes)

df.to_csv("dataset.csv")
df.to_xlsx("dataset.xlsx", index=false)
```
Exportar mostra
```python
sample = df.sample(frac=0.1)  
sample.to_csv("sample.csv")
```
Pandas read the docs

## Importar de csv

```python
import pandas as pd

df = pd.read_csv("exemple.csv", sep=",", na_filter=false)
```

## Extraer valor máximo

```python
df = pd.DataFrame(llista_dades, columns=["temp","pres", "data"])  
max = df['temp'].idxmax()  
print(df.iloc[[max]]) #localizar indice valor
```
### Leer file.json

``` python
import json  
  
f = open('medidas.json')  
  
data = json.load(f)  
  
for i in data:  
    print(f"{i['fecha']} fa {i['temperatura']}")  
f.close()
```

Tasca 1: Unificar los nombres y apellidos de los alumnos en una única cadena de texto

```python 
notes = [1,6,8,9,10,6,5]  
alumnes = ["Jaume", "Carles", "Cristina", "Josep", "Rafael", "Agnès", "Marta"]  
cognoms = ["Tort","Soldevila","Luna","Muñoz","Fernandez","Hernandez", "Llopart"]  
nom = []  
for a, c in zip(alumnes, cognoms):  
    nomc = f"{a} {c}"  
    nom.append(nomc)  
print(nom)
```

Tasca 2: Crear una lista de "tuplas" que contengan los datos del alumno unificados, y la nota obtenida

```python
notes = [1,6,8,9,10,6,5]  
alumnes = ["Jaume", "Carles", "Cristina", "Josep", "Rafael", "Agnès", "Marta"]  
cognoms = ["Tort","Soldevila","Luna","Muñoz","Fernandez","Hernandez", "Llopart"]  
nom = []  
for a, c in zip(alumnes, cognoms):  
    nomc = f"{a} {c}"  
    nom.append(nomc)  
  
llista_notes = []  
  
notes = [1,6,8,9,10,6,5]  
alumnes = ["Jaume", "Carles", "Cristina", "Josep", "Rafael", "Agnès", "Marta"]  
cognoms = ["Tort","Soldevila","Luna","Muñoz","Fernandez","Hernandez", "Llopart"]  
  
llista_notes = []  
for a, c, n in zip(alumnes, cognoms, notes):  
    nomc = f"{a} {c}"  
    nom_nota = (nomc, n)  
    llista_notes.append(nom_nota)  
print(llista_notes)
```

Tasca 3: Sumar un punto a todas la notas, sin que puedan sobrepasar el 10

```python
notes = [1,6,8,9,10,6,5]  
alumnes = ["Jaume", "Carles", "Cristina", "Josep", "Rafael", "Agnès", "Marta"]  
cognoms = ["Tort","Soldevila","Luna","Muñoz","Fernandez","Hernandez", "Llopart"]  
  
llista_notes = []  
for a, c, n in zip(alumnes, cognoms, notes):  
    nomc = f"{a} {c}"  
    nom_nota = (nomc, n)  
    llista_notes.append(nom_nota)  
for persona in llista_notes:  
    if persona[1] <= 9:  
        nota = persona[1]+1  
    else:  
        nota = persona[1]  
    nova_persona = (persona[0], nota)  
    print(nova_persona)
```

Tasca 4: Añadir un tercer elemento a la tupla siguiendo este criterio:

``` python
notes = [1,6,8,9,10,6,5]  
alumnes = ["Jaume", "Carles", "Cristina", "Josep", "Rafael", "Agnès", "Marta"]  
cognoms = ["Tort","Soldevila","Luna","Muñoz","Fernandez","Hernandez", "Llopart"]  
  
llista_notes = []  
for a, c, n in zip(alumnes, cognoms, notes):  
    nomc = f"{a} {c}"  
    nom_nota = (nomc, n)  
    llista_notes.append(nom_nota)  
for persona in llista_notes:  
    nota= persona[1]+1  
    if nota >= 10:  
        nota= 10  
        q = "Matricula d'honor"  
        persona = persona + (q,)  
    elif nota >= 9:  
        q = "excel·lent"  
        persona = persona + (q,)  
    elif nota >= 7:  
        q = "notable"  
        persona  = persona + (q,)  
    elif nota >= 6:  
        q = "bé"  
        persona = persona + (q,)  
    elif nota >= 5:  
        q = "aprobat"  
        persona = persona + (q,)  
    else:  
        q = "suspès"  
        persona = persona + (q,)  
    nova_persona = (persona[0], nota, persona[2])  
    print(nova_persona)

```


### Ejercicio 2

importar dataframe
```python
import pandas as pd

df= pd.read_csv("dataset_youtube.csv", sep=",", na_filter=False)

```

comptar columnes y files y llegir columnes

```python
total_rows=len(df.axes[0])  
total_cols=len(df.axes[1])  
  
print(f"(Number of Rows: {total_rows}")  
print(f"(Number of Columns: {total_cols}")
print(df.axes[1])
```

eliminar columnes
```python
lista_pop = ['defaultLanguage', 'dislikeCount','position','channelId','publishedAt', 'videoDescription', 'tags', 'videoCategoryId', 'videoCategoryLabel','duration','durationSec','dimension','definition', 'caption', 'defaultLAudioLanguage','thumbnail_maxres','licensedContent','favoriteCount']  

for n in lista_pop:  
    df.pop(n)
```

contar videos

```python

# comprobo quants canals unics hi ha 
canals = df['channelTitle']

canals_unics = df.channelTitle.unique

#separo el df segons el canal
df_1 = df.loc[df['channelTitle'] == NPR Music]
df_2 = df.loc[df['channelTitle'] == KEXP]

print(df_1.shape[0])
print(df_2.shape[0])
```

Calcular mitjana views, comentaris i likes

```python
print(round(df_1['viewCount'].mean(),2))     #viewers NPR
print(round(df_2['viewCount'].mean(),2))     #viewers KEXP
print(round(df_1['commentCount'].mean(),2))  #comments NPR
print(round(df_2['commentCount'].mean(),2))  #comments KEXP
print(round(df_1['likeCount'].mean(),2))     #likes NPR
print(round(df_2['likeCount'].mean(),2))     #likes KEXP
```

desviació

```python
prom_expectadors_1 = round(df_1['viewCount'].mean())
prom_expectadors_2 = round(df_2['viewCount'].mean())

for index,row in df_1.iterrows():
	df_1['desviacioV'] = prom_exèctadors_1 - row['viewCount']	
```

### Quick Start 

``` python
import spotipy  
from spotipy.oauth2 import SpotifyClientCredentials  
  
SPOTIPY_CLIENT_ID='cliente'  
SPOTIPY_CLIENT_SECRET='secreto'  
  
auth_manager = SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET)  
sp = spotipy.Spotify(auth_manager=auth_manager)
```

``` python
import spotipy  
from spotipy.oauth2 import SpotifyClientCredentials  
import json  
import time  
import pandas as pd  
  
SPOTIPY_CLIENT_ID='client'  
SPOTIPY_CLIENT_SECRET='secreto'  
  
auth_manager = SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET)  
sp = spotipy.Spotify(auth_manager=auth_manager)  
  
playlist = '417lrWJuZdotydKFOQJqrc'  
  
# https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.playlist_items  
query = sp.playlist_items(playlist, fields=None, limit=100, offset=0, market=None)  
  
relacions = []  
  
for i in query['items']:  
    artists = i['track']['artists']  
    for artist in artists:  
        source_artist_name = artist['name']  
        source_artist_id = artist['id']  
        #print(source_artist_name, source_artist_id)  
        related_artist = sp.artist_related_artists(source_artist_id)  
        time.sleep(1)  
        relacionats = related_artist["artists"]  
        for l in relacionats:  
            related_artist_name = l["name"]  
            tupla = (source_artist_name, related_artist_name)  
            relacions.append(tupla)  
  
df = pd.DataFrame.from_records(relacions, columns = ['source','target'])  
df.to_csv("dataset.csv", index=False)  
  
'''  
with open(f'{artist_id}data.json', 'w', encoding='UTF-8') as f:  
    json.dump(related_artist, f, ensure_ascii=False, indent=4)
'''
```