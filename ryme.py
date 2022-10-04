import requests

user = input('Enter a word:')
parameter = {}
parameter['rel_rhy'] = user
request = requests.get('https://api.datamuse.com/words', parameter)
ryme = request.json()
for i in ryme[0:5]:
    print(i['word'])
