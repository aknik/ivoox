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

agent = "iVoox/2.17(135) (Linux; Android 5.0; Scale/1.0)"
url1  = "http://api.ivoox.com/1-1/"
url2  = "?function=getSuscriptionAudios&format=json&session=801953506496568"

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
    if not os.path.exists('/root/Podcasts/' + podcasttitle):
        os.makedirs('/root/Podcasts/' + podcasttitle)
    savefile = '/root/Podcasts/' + podcasttitle +"/" +filename.split("_")[0] + '.mp3'
    if (row['datetext'] == 'hace 8 días' ):
        if os.path.isfile(savefile):
            os.remove(savefile)
    if (row['datetext'] == 'Hoy' or row['datetext'][0:7] == 'hace 1 ' ):
        os.system ('wget --user-agent='+ agent +' -c ' + file + ' -O ' + savefile )

        print (podcasttitle, savefile)
        print ("-----------------------------------------------------------------------------------")

