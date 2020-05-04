import requests
from bs4 import BeautifulSoup
from IPython.core.display import clear_output
import time
from random import randint
from warnings import warn
import pandas
import matplotlib.pyplot as plt
from selenium import webdriver
from lxml import html

#store data in lists
names = []
years = []
imdb_ratings = []
metascores = []
votes = []

start_time = time.time()
sent_requests = 0
years_url = [str(i) for i in range(2018,2020)]
pages = [str(i) for i in range(1,2)]
headers = {"Accept-Language": "en-US, en;q=0.5"}

for year in years_url:

    for page in pages:

        #request
        response = requests.get('http://www.imdb.com/search/title?release_date=' + year 
        + '&sort=num_votes,desc&page=' + page, headers = headers)

        #pause
        time.sleep(randint(5,12))

        #monitor requests
        sent_requests += 1
        elapsed_time = time.time() - start_time
        print('Request: {}; Frequency: {} requests/s'.format(sent_requests, sent_requests/elapsed_time))
        clear_output(wait = True)

        #warning for status codes
        if response.status_code != 200:
            warn('Request: {}; Status code: {}'.format, response.status_code)
        
        #break look if too many requests
        if sent_requests > 10:
            warn("Too many requests")
            break
        
        #parse html content
        page_html = BeautifulSoup(response.text, 'html.parser')

        #select all movie container in a page
        mv_containers = page_html.find_all('div', class_ = 'lister-item mode-advanced')

        #for each movie
        for container in mv_containers:

            #if has metascore rating
            if container.find('div', class_ = 'ratings-metascore') is not None:

                #scrape name
                name = container.h3.a.text
                names.append(name)

                #scrape year
                year = container.h3.find('span', class_ = 'lister-item-year').text
                years.append(year)

                #scrape IMDb rating
                imdb = float(container.strong.text)
                imdb_ratings.append(imdb)

                #scrape metascore rating
                m_score = container.find('span', class_ = 'metascore').text
                metascores.append(int(m_score))

                #scrape votes
                vote = container.find('span', attrs = {'name':'nv'})['data-value']
                votes.append(int(vote))

#merge data into pandas DataFrame
movie_ratings = pandas.DataFrame({'movie': names, 'year': years, 
    "imdb": imdb_ratings, 'metascore': metascores, 'votes': votes})
#reorder columns
movie_ratings = movie_ratings[['movie', 'year', 'imdb', 'metascore', 'votes']]
#show first 10 entries
# movie_ratings.head(10)

#checks unique values of years
# movie_ratings['year'].unique()

#only show ints under year
movie_ratings.loc[:, 'year'] = movie_ratings['year'].str[-5:-1].astype(int)

#checks min and max value of imdb and metascore ratings
# movie_ratings.describe().loc[['min', 'max'], ['imdb', 'metascore']]

#saves data to csv file
# movie_ratings.to_csv('movie_ratings.csv')

#plot the data
fig, axes = plt.subplots(nrows = 1, ncols = 2, figsize = (16,4))
ax1, ax2 = fig.axes
ax1.hist(movie_ratings['imdb'], bins = 10, range = (0,10)) #bin range = 1
ax1.set_title('IMDb ratings')
ax2.hist(movie_ratings['metascore'], bins = 10, range = (0,100)) #bin range = 10
ax2.set_title('Metascore')
for ax in fig.axes:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
plt.show()