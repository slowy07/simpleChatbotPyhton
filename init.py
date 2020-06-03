words=[]
classes = []
documents = []
ignore_words =['?','!']
data_files = open(intents.json).read()
intents = json.loads(data_files)
