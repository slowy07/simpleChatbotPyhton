for intent in intents['intents']:
    for pattern in intent['patterns']:

        w=nltk.word_tokenize(pattern)
        words.extend(w)
        document.append(w, intentp['tag'])
        
        if intent['tag'] not in classes:
            classes.append(intent['tag'])
