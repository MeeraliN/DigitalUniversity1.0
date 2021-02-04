from flask import Flask, render_template, request
import numpy as np
import speech_recognition as sr 
import wave, math, contextlib
import nltk
import random
from sklearn.feature_extraction.text import TfidfVectorizer
import string
import warnings
from nltk.corpus import stopwords
from nltk import sent_tokenize, word_tokenize, PorterStemmer
from moviepy.editor import AudioFileClip
from os import path
import os
from gensim.summarization import keywords
nltk.download('stopwords')
try :
  nltk.data.find('tokenizers/punkt')
  
except LookupError:
  print('punkt')
  nltk.download('punkt')

try :
  nltk.data.find('corpora/wordnet')
except LookupError:
  nltk.download('wordnet')
print("Imports Done")
from flaskwebgui import FlaskUI #get the FlaskUI class

app = Flask(__name__)
ui = FlaskUI(app)
@app.route('/')
def uploads_file():
   return render_template('Transcribo.html')
def conversionop(a):
    audioclip = AudioFileClip(a)
    audioclip.write_audiofile("file.wav")
def recognizing_text():
    from progress.bar import Bar
    with contextlib.closing(wave.open("file.wav",'r')) as f:
        waves = f.getnframes()
        framerate = f.getframerate()
        duration = waves / float(framerate)
        finaltotal = math.ceil(duration / 60)

    text=''
    r = sr.Recognizer()
    bar = Bar('IncrementalBar', max=finaltotal)
    for i in range(0, finaltotal):
        with sr.AudioFile("file.wav") as source:
            audio = r.record(source, offset=i*60, duration=60)
        f = open("transcription.txt", "a")
        f.write(r.recognize_google(audio))
        f.write(" ")
        bar.next()
    bar.finish()    
         #We noticed here that joining every new string to the base string was resulting in ram running out. Thus, we are using text file    
    print("Recognition Done")
    f.close()
def punctuates(doo=True):
    if doo==True:
        text=open("transcription.txt", "r")
        text=text.read()
        from punctuator import Punctuator

        p = Punctuator('hel.pcl')
        punctuated=p.punctuate(text)  
        print("Punctuating Done")  
        return punctuated
    else:
        text=open("transcription.txt", "r")
        text=text.read()
        return text

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        s=f.filename
    conversionop("exa.mp4")
    recognizing_text()
    print("Recognition Done")
    text=punctuates()
    HANDICAP=1
    def remove_punctuation_marks(text) :
        punctuation_marks = dict((ord(punctuation_mark), None) for punctuation_mark in string.punctuation)
        return text.translate(punctuation_marks)
    #Tokenizing the words using nltk
    def get_lemmatized_tokens(text) :
        normalized_tokens = nltk.word_tokenize(remove_punctuation_marks(text.lower()))
        return [nltk.stem.WordNetLemmatizer().lemmatize(normalized_token) for normalized_token in normalized_tokens]
    #Getting average of the values of the sentences scored
    def get_average(values) :
        greater_than_zero_count = total = 0
        for value in values :
            if value != 0 :
                greater_than_zero_count += 1
                total += value 
        return total / 1
    #Getting the final score of the sentences/words.
    def get_threshold(tfidf_results) :
        i = total = 0
        while i < (tfidf_results.shape[0]) :
            total += get_average(tfidf_results[i, :].toarray()[0])
            i += 1
        return total / tfidf_results.shape[0]
    #Getting the final summary with the most scored sentences in text
    def get_summary(documents, tfidf_results) :
        summary = ""
        i = 0
        while i < (tfidf_results.shape[0]) :
            if (get_average(tfidf_results[i, :].toarray()[0])) >= get_threshold(tfidf_results) * HANDICAP :
                    summary += ' ' + documents[i]
            i += 1
        return summary

    def finalsummary(punctuated):

        warnings.filterwarnings("ignore")
        documents = nltk.sent_tokenize(punctuated)
        tfidf_results = TfidfVectorizer(tokenizer = get_lemmatized_tokens, stop_words = stopwords.words('english')).fit_transform(documents)
        a=get_summary(documents, tfidf_results)
        return a
    a=finalsummary(text)    
    print("Summarization DOne!")
    text_en = text
    final=keywords(text_en,words = 10, lemmatize = True)
    print(final)
    lens=len(final)
    
    return render_template("summary.html",a=a,final=final,punctuated=text,lens=lens)
if __name__ == '__main__':
   ui.run()    