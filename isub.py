# DESCARGA UNA SUSCRIPCION A PODCAST COMPLETA. TODOS LOS EPISODIOS
# VA DE LA PAGINA 1 A LA n descargando los episodios.   for page in range(0, 10):
import time,os,re,requests,json

def urlify(s):

     # Remove all non-word characters (everything except numbers and letters)
     s = re.sub(r"[^\w\s]", '', s)
     # Replace all runs of whitespace with a single dash
     s = re.sub(r"\s+", '_', s)
     return s
	 
for page in range(0, 10):


	agent = '"iVoox/2.15(134) (Linux; Android 7.2; Scale/1.0)"'
	url1  = "http://api.ivoox.com/1-1/"
	url2  = "?function=getSuscriptionAudios&format=json&session=326616120656816&page="+ str(page) +"&idSuscription=8297402&unread=0"
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
		#podcasttitle = urlify(row['podcasttitle'])
		file = str(row['file'])
		filename = os.path.basename(file)
		savefile = './Podcasts/EADO/' + filename.split("_")[0] + '.mp3'
		os.system ('wget --user-agent='+ agent +' -c ' + file + ' -O ' + savefile )
		print (filename)
