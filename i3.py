# Descarga los podcast subscritos que se han publicado "hoy"
# Para python 3

import time,os,re,requests,json

def urlify(s):

     # Remove all non-word characters (everything except numbers and letters)
     s = re.sub(r"[^\w\s]", '', s)
     # Replace all runs of whitespace with a single dash
     s = re.sub(r"\s+", '_', s)
     return s

agent = '"iVoox/2.15(134) (Linux; Android 4.0.2; Scale/1.0)"'
url1  = "http://api.ivoox.com/1-1/"
url2  = "?function=getSuscriptionAudios&format=json&session=801953506496666"

headers = {
    'User-Agent': agent,
    'Accept-Encoding': 'gzip',
    'accept-language': 'es-ES',
    'Connection': 'Keep-Alive',
}
r = requests.get(url1+url2, headers=headers)
json = r.json()
i = 0

for row in json:
    i += 1
    podcasttitle = urlify(row['podcasttitle'])
    file = str(row['file'])
    filename = os.path.basename(file)
    print (row['datetext'],filename)

    savefile = './Podcasts/' + filename.split("_")[0] + '.mp3'
    if (row['datetext'] == 'hace 8 días' ):
        if os.path.isfile(savefile):        
            os.remove(savefile) 
    if (row['datetext'] == 'hace 1 día' or row['datetext'] == 'Hoy'):
        os.system ('wget --user-agent='+ agent +' -c ' + file + ' -O ' + savefile )
        print (filename)

