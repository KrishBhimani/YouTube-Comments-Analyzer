# Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import string
import nltk
from nltk.stem import SnowballStemmer
nltk.download('stopwords')
from nltk.corpus import stopwords


# Preprocessing
stemmer = SnowballStemmer(language='english')
def textPreprocess(text):
    try:
        text = ' '.join([i for i in text.lower().split() if ((i.find('http') < 0) & (i.find('.com') < 0))]) # remove links
        text = text.replace('<br',' ') # remove br tag
        text = ''.join([i for i in text if i not in string.punctuation ]) # lower casing and remove punctuations
        text = ''.join([i for i in text if i.isnumeric()==False]) # remove numeric values
        text = ' '.join([stemmer.stem(i) for i in text.split() if i not in stopwords.words('english')]) # stemming and remove stopwords
    except:
        text = ''
    return text