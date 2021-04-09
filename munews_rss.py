# Joseph Falzini
# CS371
# Python Project - Create an RSS XML File for MU News

import requests
import bs4
import PyRSS2Gen  # Used to create the RSS format for the XML file
import datetime # Fetches the current date and time 

# Use the request module to pull the website
url1 = "https://www.monmouth.edu/news/archives"
hdrs = {"Accept-Language": "en-us, en;q=0.5"}
req = requests.get(url1, headers = hdrs)
soup = bs4.BeautifulSoup(req.text, "html.parser")

# Arrays to store XML information
hdline = []
links = []
pub_date = []

# Parse the XML for Articles
articles = soup.find_all('article')

# Append the articles to the article array
for article in articles:
    hdline.append(article['aria-label'])

    # Links for articles
    articlelinks = article.find('a')
    links.append(articlelinks['href'])

    # Publication date of articles
    dates = article.find('div', {'class': 'article-meta'})
    dates_text = dates.text.strip()
    pub_date.append(dates_text)

# Retrieving the second URL
url2 = "https://www.monmouth.edu/news/archives/page/2/"
req2 = requests.get(url2, headers = hdrs)
soup = bs4.BeautifulSoup(req2.text, "html.parser")

# Repeat the same steps for URL1
articles = soup.find_all('article')

for article in articles:
    hdline.append(article['aria-label'])

    articlelinks = article.find('a')
    links.append(articlelinks['href'])

    dates = article.find('div', {'class': 'article-meta'})
    dates_text = dates.text.strip()
    pub_date.append(dates_text)

# Initiating PyRSSGen
rss = PyRSS2Gen.RSS2(
    title = "Joseph Falzini's MU News RSS Feed",
    link = "https://www.monmouth.edu/news/archives",
    description = "",
    lastBuildDate = datetime.datetime.now(),
)

# Adding items to PyRSSGen
for i in range(0, len(hdline)):
    rss.items.append(PyRSS2Gen.RSSItem (
        title = hdline[i],
        link = links[i],
        description = "",
        pubDate = pub_date[i],
    ))

rss.write_xml(open("JF_munews.rss.xml", "w"))