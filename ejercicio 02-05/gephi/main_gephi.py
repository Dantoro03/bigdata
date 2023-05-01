import pandas as pd
import json
import glob
import tqdm as tqdm

files = glob.glob("api_responses/*") #abrir todos los archivos

llista_dfs = []

for file in files:
    with open(file, encoding='utf-8') as jsonfile:
        dades =json.load(jsonfile)
        tweets = dades['data']
        vacia = None #creo una variable per crear una columna buida
        for tweet in tweets: #entro a la informació de cada tweet
            author_id = tweet['author_id']
            users = dades['includes']['users']
            if 'entities' in tweet: #entro a les entitats del tweet per poder agafar els hashtags
                entities = tweet['entities']
                if 'mentions' in entities:
                    menciones = entities['mentions']
                    for citados in menciones:
                        citado = citados['username']
                else:
                    target = None
            else:
                target = None
            for user in users:
                if user['id'] == author_id:
                    source = user['username']
                    break
                else:
                    pass
            text = tweet['text']
            df = pd.DataFrame({ #creo el dataframe
                'Source': source,
                'Target': citado,
                'text': text,
                'text2': vacia, #variable buida per corretgir un error en el que alguns textos es colaven a la següent columna
            }, index=[0])
            llista_dfs.append(df) #fico el dataframe en una llista fora del bucle per guardar les dades
df_final = pd.concat(llista_dfs) #concateno tots els dataframes de la llista
df_final.to_csv('df_final_gephi.csv', sep ='\t' , index= False)