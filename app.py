from flask import Flask, render_template, request
# from sklearn.feature_extraction.text import CountVectorizer
from preprocess import textPreprocess
import pandas as pd
import pickle
import numpy as np

sentimentAnalyzer = pickle.load(open('sentimentAnalyzer.pkl','rb'))
spamDetector = pickle.load(open('spam_model_with_pipe.pkl','rb'))
clusterModel = pickle.load(open('clusterModel.pkl','rb'))


path = 'prediction.csv'
df = pd.read_csv(path)

app = Flask(__name__)
class_senti = ['Irrelevant', 'Neutral', 'Negative', 'Positive']
class_spam = ['No Spam', 'Spam']

@app.route('/')
def index():
    return render_template('index.html', comments = df['comment'].values,
                           spam = df['pred_spam'].values,
                           senti = df['pred_sentiment'].values,
                           class_spam = class_spam, class_senti = class_senti, cluster = df['cluster'].values,
                           n = len(df['comment'].values))

@app.route('/pred',methods=['POST', "GET"])
def pred():
    text = request.form.get('comment')
    processedText = textPreprocess(text)
    spam = spamDetector.predict(np.array([processedText])) 
    spam = class_spam[spam[0]]

    senti = sentimentAnalyzer.predict(np.array([processedText])) 
    senti = class_senti[senti[0]]

    cluster = clusterModel.predict([processedText])
    return render_template('prediction.html',
                           spam = spam, text = text, senti=senti, cluster=cluster)
@app.route('/prediction')
def prediction():
    return render_template('prediction.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__=='__main__':
    Flask.run(reload=True)