from flask import Flask, render_template, request
from rss.Feed import *

app = Flask(__name__,
            static_url_path='', 
            static_folder='static',
            template_folder='templates')

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/une/")
def une():
    return showResults(url="https://www.lemonde.fr/rss/une.xml")

@app.route("/en_continu/")
def en_continu():
    return showResults(url="https://www.lemonde.fr/rss/en_continu.xml")

@app.route("/videos/")
def videos():
    return showResults(url="https://www.lemonde.fr/videos/rss_full.xml")

@app.route("/portfolios/")
def portfolios():
    return showResults(url="https://www.lemonde.fr/photo/rss_full.xml")

@app.route("/les_plus_lus/")
def les_plus_lus():
    return showResults(url="https://www.lemonde.fr/rss/plus-lus.xml")

@app.route("/les_plus_partages/")
def les_plus_partages():
    return showResults(url="https://www.lemonde.fr/rss/plus-partages.xml")

@app.route("/une_international/")
def une_international():
    return showResults(url="https://www.lemonde.fr/international/rss_full.xml")

@app.route("/europe/")
def europe():
    return showResults(url="https://www.lemonde.fr/europe/rss_full.xml")

@app.route("/ameriques/")
def ameriques():
    return showResults(url="https://www.lemonde.fr/ameriques/rss_full.xml")

@app.route("/afrique/")
def afrique():
    return showResults(url="https://www.lemonde.fr/afrique/rss_full.xml")

@app.route("/asie/")
def asie():
    return showResults(url="https://www.lemonde.fr/asie-pacifique/rss_full.xml")

@app.route("/proche_orient/")
def proche_orient():
    return showResults(url="https://www.lemonde.fr/proche-orient/rss_full.xml")

@app.route("/royaume_uni/")
def royaume_uni():
    return showResults(url="https://www.lemonde.fr/royaume-uni/rss_full.xml")

@app.route("/etats_unis/")
def etats_unis():
    return showResults(url="https://www.lemonde.fr/etats-unis/rss_full.xml")

@app.route("/politique/")
def politique():
    return showResults(url="https://www.lemonde.fr/politique/rss_full.xml")

@app.route("/societe/")
def societe():
    return showResults(url="https://www.lemonde.fr/societe/rss_full.xml")

@app.route("/les_decodeurs/")
def les_decodeurs():
    return showResults(url="https://www.lemonde.fr/les-decodeurs/rss_full.xml")

@app.route("/justice/")
def justice():
    return showResults(url="https://www.lemonde.fr/justice/rss_full.xml")

@app.route("/police/")
def police():
    return showResults(url="https://www.lemonde.fr/police/rss_full.xml")

@app.route("/campus/")
def campus():
    return showResults(url="https://www.lemonde.fr/campus/rss_full.xml")

@app.route("/education/")
def education():
    return showResults(url="https://www.lemonde.fr/education/rss_full.xml")

@app.route("/une_economie/")
def une_economie():
    return showResults(url="https://www.lemonde.fr/economie/rss_full.xml")

@app.route("/entreprises/")
def entreprises():
    return showResults(url="https://www.lemonde.fr/entreprises/rss_full.xml")

@app.route("/argent/")
def argent():
    return showResults(url="https://www.lemonde.fr/argent/rss_full.xml")

@app.route("/economie_francaise/")
def economie_francaise():
    return showResults(url="https://www.lemonde.fr/economie-francaise/rss_full.xml")

@app.route("/industrie/")
def industrie():
    return showResults(url="https://www.lemonde.fr/industrie/rss_full.xml")

@app.route("/emploi/")
def emploi():
    return showResults(url="https://www.lemonde.fr/emploi/rss_full.xml")

@app.route("/immobilier/")
def immobilier():
    return showResults(url="https://www.lemonde.fr/immobilier/rss_full.xml")

@app.route("/medias/")
def medias():
    return showResults(url="https://www.lemonde.fr/medias/rss_full.xml")

@app.route("/une_culture/")
def une_culture():
    return showResults(url="https://www.lemonde.fr/culture/rss_full.xml")

@app.route("/cinema/")
def cinema():
    return showResults(url="https://www.lemonde.fr/cinema/rss_full.xml")

@app.route("/musiques/")
def musiques():
    return showResults(url="https://www.lemonde.fr/musiques/rss_full.xml")

@app.route("/television_et_radio/")
def television_et_radio():
    return showResults(url="https://www.lemonde.fr/televisions-radio/rss_full.xml")

@app.route("/le_monde_des_livres/")
def le_monde_des_livres():
    return showResults(url="https://www.lemonde.fr/livres/rss_full.xml")

@app.route("/arts/")
def arts():
    return showResults(url="https://www.lemonde.fr/arts/rss_full.xml")

@app.route("/scenes/")
def scenes():
    return showResults(url="https://www.lemonde.fr/scenes/rss_full.xml")

@app.route("/une_sport/")
def une_sport():
    return showResults(url="https://www.lemonde.fr/sport/rss_full.xml")

@app.route("/football/")
def football():
    return showResults(url="https://www.lemonde.fr/football/rss_full.xml")

@app.route("/rugby/")
def rugby():
    return showResults(url="https://www.lemonde.fr/rugby/rss_full.xml")

@app.route("/tennis/")
def tennis():
    return showResults(url="https://www.lemonde.fr/tennis/rss_full.xml")

@app.route("/cyclisme/")
def cyclisme():
    return showResults(url="https://www.lemonde.fr/cyclisme/rss_full.xml")

@app.route("/basket/")
def basket():
    return showResults(url="https://www.lemonde.fr/basket/rss_full.xml")




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
    return render_template('results.html', 
                           title=title, 
                           description=description, 
                           published=published, 
                           results=results)

if __name__ == '__main__':
    app.run(debug=True)