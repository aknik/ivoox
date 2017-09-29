# Descarga los podcast subscritos que se han publicado "hoy"
# Para python 3

import time,os,re,requests,json

def urlify(s):

     # Remove all non-word characters (everything except numbers and letters)
     s = re.sub(r"[^\w\s]", '', s)
     # Replace all runs of whitespace with a single dash
     s = re.sub(r"\s+", '_', s)
     return s

def download_file(url,savefile):
    r = requests.get(url, stream=True)
    with open(savefile, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                #f.flush() commented by recommendation from J.F.Sebastian
    return savefile

agent = '"iVoox/2.15(134) (Linux; Android 7.0; Scale/1.0)"'
url1  = "http://api.ivoox.com/1-1/"
url2  = "?function=getSuscriptionAudios&format=json&session=8............."

headers = {
    'User-Agent': agent,
    'Accept-Encoding': 'gzip',
    'accept-language': 'es-ES',
    'Connection': 'Keep-Alive',
}

i = 0

while True:

    r = requests.get(url1+url2, headers=headers)
    if r.status_code == 200 or i > 9:
        break
    i += 1
    time.sleep(3+i)

i = 0

for row in r.json():
    i += 1
    podcasttitle = urlify(row['podcasttitle'])
    file = str(row['file'])
    filename = os.path.basename(file)
    print ("<<<   ",row['datetext'], podcasttitle)

    savefile = './Podcasts/' + filename.split("_")[0] + '.mp3'
    if (row['datetext'] == 'hace 8 días' ):
        if os.path.isfile(savefile):
            os.remove(savefile)
    if (row['datetext'] == 'hace 1 día' or row['datetext'] == 'Hoy'):
        os.system ('wget --user-agent='+ agent +' -c ' + file + ' -O ' + savefile )

        print (podcasttitle, savefile)
        print ("-----------------------------------------------------------------------------------")


