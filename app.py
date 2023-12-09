from flask import Flask, render_template, request
from rss.Feed import *
from data.rss_links import rss_links
from spacy.lang.fr.stop_words import STOP_WORDS as fr_stop
import matplotlib.pyplot as plt
from wordcloud import WordCloud

app = Flask(__name__,
            static_url_path='', 
            static_folder='static',
            template_folder='templates')

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/<string:link>")
def result(link):
    try:
        url = rss_links[link]
    except:
        url = rss_links[list(rss_links.keys())[0]]
    finally:
        return showResults(url)

def make_stop_words(filename:str="data/stopwords-fr.txt"):
    stop_words = []
    with open(filename, "r") as f:
        stop_words = f.read().splitlines()
    return stop_words

def make_wordcloud(text:str):
    stop_word = make_stop_words()
    text = text.replace("’", "'")
    text = text.replace("'", "' ")
    for word in stop_word:
        text = text.replace(" "+word+" ", " ")
    wordcloud = WordCloud(stopwords=set(fr_stop), background_color="white").generate(text)
    wordcloud.to_file('static/img/wordcloud.png')
    return wordcloud.words_.keys()

def showResults(url=None):
    feed = Feed(url)
    title = feed.getTitle()
    description = feed.getDescription()
    published = feed.getPublished()
    length = feed.getLength()
    entries = feed.getEntries()
    results = [{'title':entry.getTitle(), 
                'description':entry.getDescription(), 
                'published':entry.getPublished(), 
                'link':entry.getLink()} for entry in entries]
    wc_data = " ".join([d["description"] for d in results])
    wc_result = list(make_wordcloud(wc_data))

    return render_template('results.html', 
                           title=title, 
                           description=description, 
                           published=published, 
                           results=results,
                           wc_result=wc_result,
                           length=length)

if __name__ == '__main__':
    app.run(debug=True)