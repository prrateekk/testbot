import requests,json,time
import detectlanguage
from mtranslate import translate

pre = 'https://api.telegram.org/bot'
token = '373390278:AAG5bYHjKGGUi6S0K5RcwVHI7K8PECqA8rY'
detectlanguage.configuration.api_key = "6629c18e0734250839a4bac5b1fbc065"
last_text = None
lang = 'hi'

def greetuser(id,text):
	url = pre+token+'/sendmessage?chat_id='+str(id)+'&text='+text
	r = requests.post(url)
	'''
	language = detectlanguage.simple_detect(text)
	if (language=='en'):
		text = translate(text,lang)
	else:
		text = translate(text,'en')

	url = pre+token+'/sendmessage?chat_id='+str(id)+'&text='+text
	r = requests.post(url)
	'''

def getupdates():
	url = pre+token+'/getupdates'
	response = requests.get(url)
	response = response.json()
	length = len(response['result'])
	text = response['result'][length-1]['message']['text']
	global last_text
	if (text!=last_text):
		last_text = text
		greetuser(response['result'][length-1]['message']['from']['id'],text)
	time.sleep(0.5)

while True:
	getupdates()
