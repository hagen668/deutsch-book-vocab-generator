class dataCleaning:
    def __init__(self, data):
        self.data = data
        
    def textcleaner(self):
        # use nltk to tokenize text
        import nltk
        nltk.download('punkt')
        #nltk.download('stopwords')
        import re
        from nltk.tokenize import sent_tokenize, word_tokenize
        from nltk.corpus import stopwords
        # use spacy to access german dictionary
        #import spacy   
        #!{sys.executable} -m spacy download de_core_news_md 

        # tokenize the words
        tokens = nltk.word_tokenize(self.data)
        text = nltk.Text(tokens)
        deutsch_stopwords = stopwords.words("german")

        # remove non alphanumeric characters and stop words
        nonPunct = re.compile('.*[A-Za-z].*')
        raw_words = [w for w in text if nonPunct.match(w)]
        #nondotwords = [s.replace('.', '') for s in nonPunct_words]
        #raw_words = [s.replace('-', '') for s in nondotwords] 
        raw_words_lwr = [token.lower() for token in raw_words]
        raw_words_no_stop = [w for w in raw_words_lwr if not w in deutsch_stopwords]
        return raw_words_no_stop

    def textlemmatizer(self):

        # !{sys.executable} -m spacy download de_core_news_md
        # import spacy

        # use the SpaCy package for lemmatization and POS tagging
        # edit the below dictionary to reflect the language of the text
        # nlp = spacy.load('de_core_news_md')

        # lemmatize words
        words_lemma = []
        for word in raw_words_lwr:
             doc = nlp(word)
             result = ' '.join([x.lemma_ for x in doc]) 
             words_lemma.append(result)


        # de-dupe lemmatized word list
        lemma_deduped = []
        [lemma_deduped.append(x) for x in words_lemma if x not in lemma_deduped]

    def texttranslator(self):
        # import googletrans package
        # pip3 install 'googletrans==4.0.0rc1'
        from googletrans import Translator

        # translation prep
        translator = Translator()
        flashcards_en = []
        flashcards_de = []

        # translation execution
        for translation in self.data:
            result = translator.translate(translation, src='de', dest='en')
            flashcards_de.append(result.origin)
            flashcards_en.append(result.text)
            
        # clean up english translations
        flashcards_en = [s.replace('to ', '') for s in flashcards_en] 

        # German-English dictionary created here
        flashcard_dict = dict(zip(flashcards_de, flashcards_en))



        
#dc=dataCleaning(data)
#dc.textcleaner()