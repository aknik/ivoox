# DESCARGA UNA SUSCRIPCION A PODCAST COMPLETA. TODOS LOS EPISODIOS
#import telebot
#from telebot import types
import time,os,re,requests,json

TOKEN = "289123777:AAH-1mZ3C-xxxxxxxx_xIGOv0"
admin = "@mibot"
bot = telebot.TeleBot(TOKEN)

def urlify(s):

     # Remove all non-word characters (everything except numbers and letters)
     s = re.sub(r"[^\w\s]", '', s)
     # Replace all runs of whitespace with a single dash
     s = re.sub(r"\s+", '_', s)
     return s

agent = "iVoox/2.15(134) (Linux; Android 7.2; Scale/1.0)"
url1  = "http://api.ivoox.com/1-1/"
url2  = "?function=getSuscriptionAudios&format=json&session=32661612065&page=1&idSuscription=8511076&unread=0"

r = requests.get(url1+url2)
json = r.json()
i = 0

for row in json:
    i += 1
    #podcasttitle = urlify(row['podcasttitle'])
    filename = os.path.basename(str(row['file']))
    savefile = './Podcasts/Skylab/' + filename.split("_")[0] + '.mp3'
    os.system ('wget --user-agent='+ agent +' -c ' + file + ' -O ' + savefile )
    print filename

