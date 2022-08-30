import requests,json
from bs4 import BeautifulSoup
# 
url='https://www.imdb.com/india/top-rated-indian-movies/'
sp=requests.get(url)
soup=BeautifulSoup(sp.text,'html.parser')
#  
def scrape_top_list():
    main_div= soup.find('div',class_="lister")
    tbody=main_div.find('tbody',class_="lister-list")
    trs=tbody.find_all('tr')
    movie_rank=[]
    movie_name=[]
    year_of_realease=[]
    movie_urls=[]
    movie_rating=[]
# 
    for tr in trs:
        position=tr.find('td',class_="titleColumn").get_text().strip()
        rank=" "
        for i in position:
            if '.' not in i:
                rank=rank+i
            else:
                break
        movie_rank.append(rank)
# 
        title=tr.find('td',class_="titleColumn").a.get_text()
        movie_name.append(title)
# 
        year=tr.find('td',class_="titleColumn").span.get_text()
        years=year[1:5]
        year_of_realease.append(int(years))
# 
        rating=tr.find('td',class_="ratingColumn imdbRating").strong.get_text()
        movie_rating.append(rating)
# 
        link=tr.find('td',class_="titleColumn").a['href']
        movie_link='https://www.imdb.com/'+link
        movie_urls.append(movie_link)
# 
    Top_movie=[]
    b={}
    for i in range(len(movie_rank)):
        b['position']=movie_rank[i]
        b['Name']=movie_name[i]
        b['year']=year_of_realease[i]
        b['rating']=movie_rating[i]
        b['uri']=movie_urls[i]
        Top_movie.append(b.copy())
    b=year_of_realease
    b2=[]
    b1={}
    for a in b:
        c=a%10
        c1=a-c
        if c1 not in b2:
            b2.append(c1)
    b2.sort
    for e in b2:
        e2=[]
        for e1 in Top_movie:
            if str(e//10) in str(e1['year']):
                e2.append(e1)
        b1[e]=e2
    with open('task3s.json','w') as f:
        json.dump(b1,f,indent=4)
print(scrape_top_list())