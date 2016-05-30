import feedparser
from flask import Flask
from flask import render_template

app = Flask(__name__)

RSS_FEEDS = {
        'hn' : 'https://news.ycombinator.com/rss',
        'bbc' : 'http://feeds.bbci.co.uk/news/rss.xml'
        }

@app.route("/")
@app.route("/<publication>")
def get_news(publication="hn"):
    feed = feedparser.parse(RSS_FEEDS[publication])
    first_article = feed['entries'][0]
    return render_template("home.html", articles=feed['entries'])

if __name__ == '__main__':
    app.run(port=5000, debug=True)
