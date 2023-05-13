
# Tableau

## Candidats

![[Candidatos.png]](https://github.com/Dantoro03/bigdata/blob/main/ejercicio%2002-05/Candidatos.png)

En aquest grafic podem veure que hi ha una gran diferencia entre Ada Colau i els altres candidats en quant a les mencions que es fan a la xarxa dels candidats. L'actual alcaldesa rep més de 20.000 mencions comparada amb la següent candidata més mencionada. Es necesari destacar que Ada Colau no te cap compte actiu en aquesta xarxa social i encara amb aixo es la candidata de la que més es parla, seguida de Eva Parera la candidata més activa a Xarxes socials. També es destacable que exceptuant a Eva Parera podem veure una relació inversament proporcional entre l'activitat d'un candidat i les mencions que rep. 


## Hastags

![[Hashtags 1.png]]((https://github.com/Dantoro03/bigdata/blob/main/ejercicio%2002-05/Hashtags%201.png)

Si analitzem els hashtags més utilitzats podem veure que els temes dels que més es parla (els hashtags més utilitzats) son de noticies o entrevistes (URGENTE, OPINIÓN, ENTREVISTA, ÚLTIMAHORA), un esperable hashtag de Barcelona, tres hashtags relacionats amb algun polític o partit i un últim de Pólonia. Però aquest temes encara ser els més parlats no son els que generen més impacte, ja que exceptuant URGENTE i TriasAlcalde la resta de hashtags no estan entre els deus hashtag  amb més impacte. 
Els Hashtags que si que generen més impacte son els que parlen de la llei de vivenda (leyantiocupasYAA, leyantiocupas, ViviendaARV) o hashtags utilitzats relacionats directament amb partits politics (SoloSumaPSOE, TriasAlcalde, LaBarcelonaSensata, Elecciones2023, YolandaPresidenta)

(he mesurat el impacte assignant un valor a cada interacció, sumant aquest valors i dividint-los entre les vegades que s'ha utilitzat aquest hashtag. Els valors que he assignat a cada interacció son: like = 0.2 per requerir molt poca interacció amb l'usuari i no dona visibilitat directa al tweet, retweet = 0.5 per requerir molt poca interacció amb l'usuari però si donar visibilitat directa al tweet, Quote y Reply = 1 per requerir molta interacció amb l'usuari i donar visibilitat al tweet)

![[Usuaris.png]](https://github.com/Dantoro03/bigdata/blob/main/ejercicio%2002-05/Usuaris.png)

Entre las cuentas más activas de la conversación encontramos tres medios de comunicación (naciodigital, elnacionalcat i btvnoticies) i siete usuarios, todas esta cuentas tienen entre 45 i 90 tweets publicados en la conversación y si vemos

Entre els comptes més actius de la conversa social trobem tres mitjans de comunicació (naciodigital, elnacionalcat i btvnoticies) y set usuaris, tots aquest comptes tenen publicats entre 45 i 90 tweets a la conversa i analitzant els hashtags que utilitza cada usuari (els mitjans de comunicació només utilitzen hashtags de noticies) la majoria utilitzen hashtags de ÚLTIMAHORA i són els que més publiquen aixi que podem intuir que son comptes dedicats a informar sobre temes de politica. Però tambè trobem que tres usuaris (LauraMartiBCN, Ssuuss21 i Wittgenstein_jm) utilitzen hashtags en contra del govern actual (AixiNo, ColauNoCompleix, stopinmigraciónilegal, FrauColau)

# Graph
![[gephi1.png]](https://github.com/Dantoro03/bigdata/blob/main/ejercicio%2002-05/gephi1.PNG)

A primera vista podem veure tres grups ben diferenciats
![[gephi2.png]](https://github.com/Dantoro03/bigdata/blob/main/ejercicio%2002-05/gephi2.PNG)

El primer grup son comptes on fan humor amb els polítics especialment criticant a la esquerra. la majoria no fan contingut exclusiu sobre Barcelona. Son pocs comptes amb un alt grau d'entrada es a dir, molta gent els etiqueta per a que parlin d'un tema o fasin broma de barcelona.

![[gephi3.png]](https://github.com/Dantoro03/bigdata/blob/main/ejercicio%2002-05/gephi3.PNG)

El següent  grup son comptes que si es centren en parlar de Barcelona i hi podem veure partits polítics com Esquerra Republicana,  aquest nodes no son tan grans, pero estan molt més juntsm es a dir que tendeixen a mencionarse mutuament molt més.
![[Gephi 4.png]](https://github.com/Dantoro03/bigdata/blob/main/ejercicio%2002-05/Gephi%204.PNG)

L'ultim grup son petits nodes molt dispersos entre sí que es relacionen al voltant de JuanmiGG_News un periodista frelance d'esquerres. Aquesta comunitat es relaciona bastant amb la comunitat anterior i altres intermitges menys destacables. Cal destacar que en aquesta comunitat trobem el compte de Yolanda Diaz posicionat molt proper al centre de les comunitats. 
