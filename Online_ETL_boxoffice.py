## Beautiful Soup 4 Practuce files.
import pandas as pd # data analysis
import requests # get url
from bs4 import BeautifulSoup as bs # data scraping
import matplotlib.pyplot as plt # Data visualisation
import datetime # Check week number

def get_site(week, year):
    html = 'http://www.boxofficemojo.com/weekend/chart/?yr={}&wknd={}&p=.htm'.format(year, week)
    r = requests.get(html)
    return r.content

def get_data_for_year(yr):
    # Box Office Mojo by IMDB pro
    BOM_url = f'https://www.boxofficemojo.com/year/{yr}/?grossesOption=totalGrosses'
    # open connection
    movies_html = requests.get(BOM_url)
    page_body = movies_html.content
    page_soup = bs(movies_html.text, 'html.parser')
    file_name = 'movies_content.txt'
    list_tr = page_soup.findAll("tr")
    n = len(list_tr)
    print(n)
    # first row is the header with Rank
    #print(list_tr[0].select('th'))
    movie_list = []
    #print(list_tr[137])
    #print(list_tr[138])
    try:
        for i in range(1, n):
            movie = []
            #movie_idx = list_tr[i].select('td',{"class" : "a-text-right mojo-header-column mojo-truncate mojo-field-type-rank mojo-sort-column"})[0].text
            movie_idx = list_tr[i].select('td')[0].text
            movie_release = list_tr[i].select('a')[0].text
            movie_gross = list_tr[i].select('td')[5].text
            movie_max_th = list_tr[i].select('td')[6].text
            movie_opening = list_tr[i].select('td')[7].text
            movie_of_total = list_tr[i].select('td')[8].text
            movie__open_th = list_tr[i].select('td')[9].text
            movie_open_date = list_tr[i].select('td')[10].text
            movie_close_date = list_tr[i].select('td')[11].text
            try:
                movie_distributor = list_tr[i].select('a')[1].text
            except: pass
            movie.append(movie_idx)
            movie.append(movie_release)
            movie.append(movie_gross)
            movie.append(movie_max_th)
            movie.append(movie_opening)
            movie.append(movie_of_total)
            movie.append(movie__open_th)
            movie.append(movie_open_date)
            movie.append(movie_close_date)
            movie.append(movie_distributor)
            movie_list.append(movie)
        #for ls in movie_list: print(ls)
    except Exception as e: pass
        #print(f"error in  = {i} row")
        #print(e.args)
        #pass
    print(len(movie_list))
    return movie_list

def main():
    movie_list = get_data_for_year(2019)
    df = pd.DataFrame(movie_list, index='Rank', columns={'Rank','Release','Gross','Max_Th','Opening',	'%_of_Total','Open_Th',	'Open',	'Close','Distributor'})
    df.set_index('Rank')
    df.to_excel('Ani_movies.xlsx', 'w')
    print(df.shape)
    print(df['Rank'])



if __name__ == '__main__':
    main()
