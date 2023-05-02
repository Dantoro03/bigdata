import pandas as pd
import json
import glob
from tqdm import tqdm

files = glob.glob("api_responses/*") #abrir todos los archivos

llista_dfs = []

for file in tqdm(files):
    with open(file, encoding='utf-8') as jsonfile:
        dades =json.load(jsonfile)
        tweets = dades['data']
        vacia = None #creo una variable per crear una columna buida
        for tweet in tweets: #entro a la informació de cada tweet
            time = tweet['created_at']
            author_id = tweet['author_id']
            users = dades['includes']['users']
            likes = tweet['public_metrics']['like_count']
            retweet = tweet['public_metrics']['retweet_count']
            reply = tweet['public_metrics']['reply_count']
            quote = tweet['public_metrics']['quote_count']
            created_at = tweet['created_at']

            if 'entities' in tweet: #entro a les entitats del tweet per poder agafar els hashtags
                entities = tweet['entities']
                if 'hashtags' in entities:
                    tags = entities['hashtags']
                    for hashtag in tags:
                        hashtags = hashtag['tag']
                else:
                    hashtags = None
            else:
                hashtags = None
            for user in users:
                if user['id'] == author_id: #busco l'id del usuari que ha fet el tweet
                    user_name = user['username']
                    followers = user['public_metrics']['followers_count']
                    break
                else:
                    pass
            text = tweet['text']
            text_l = text.lower() #paso el text a minuscules per a que no hi hagi case sensitive
            if text_l.find('ada') >= 0:
                Ada = 1
            elif text_l.find('colau') >= 0:
                Ada = 1
            else:
                Ada = 0
            if text_l.find('basha') >= 0:
                Basha = 1
            elif text_l.find('changue') >= 0:
                Basha = 1
            else:
                Basha = 0
            if text_l.find('ernest') >= 0:
                Ernest = 1
            elif text_l.find('maragall') >= 0:
                Ernest = 1
            else:
                Ernest = 0
            if text_l.find('jaume') >= 0:
                Jaume = 1
            elif text_l.find('collboni') >= 0:
                Jaume = 1
            else:
                Jaume = 0
            if text_l.find('xavier') >= 0:
                Xavier = 1
            elif text_l.find('trias') >= 0:
                Xavier = 1
            else:
                Xavier = 0
            if text_l.find('anna') >= 0:
                Anna = 1
            elif text_l.find('grau') >= 0:
                Anna = 1
            else:
                Anna = 0
            if text_l.find('eva') >= 0:
                Eva = 1
            elif text_l.find('parera') >= 0:
                Eva = 1
            else:
                Eva = 0
            if text_l.find('daniel') >= 0:
                Daniel = 1
            elif text_l.find('sirera') >= 0:
                Daniel = 1
            else:
                Daniel = 0
            df = pd.DataFrame({ #creo el dataframe
                'created_at': time,
                'user_id': author_id,
                'user_name': user_name,
                'followers_count': followers,
                'text': text,
                'text2': vacia, #variable buida per corretgir un error en el que alguns textos es colaven a la següent columna
                'like': likes,
                'retweet': retweet,
                'reply': reply,
                'quote': quote,
                'hashtags': hashtags,
                'Ada Colau': Ada,
                'Basha Changue': Basha,
                'Ernest Maragall': Ernest,
                'Jaume Collboni': Jaume,
                'Xavier Trias': Xavier,
                'Anna Grau': Anna,
                'Eva Parera': Eva,
                'Daniel Sirera': Daniel,

            }, index=[0])
            llista_dfs.append(df) #fico el dataframe en una llista fora del bucle per guardar les dades
df_final = pd.concat(llista_dfs) #concateno tots els dataframes de la llista
df_final.to_csv('df_final.csv', sep ='\t' , index= False)