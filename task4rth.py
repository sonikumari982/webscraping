import requests,json
from bs4 import BeautifulSoup

def movie_scrape_details(uri):
    sp=requests.get(uri)
    soup=BeautifulSoup(sp.text,'html.parser')

    details={}
    main_div=soup.find('div',class_="TitleBlock__TitleContainer-sc-1nlhx7j-1 jxsVNt").h1.get_text()
    details["name"]=main_div

    ma=soup.find('li',attrs={"data-testid":"title-techspec_runtime"})
    ma1=ma.find('div',class_="ipc-metadata-list-item__content-container").get_text().strip()
    a=ma1
    if 'min' in a:
        a2=(int(a[0])*60+int(a[8:].strip('minutes')))
    elif 'min' not in a:
        a2=(int(a[0])*60)
    else:
        a2=('nun')
    details["runtime"]=a2

    poster=soup.find('div',class_="ipc-media ipc-media--poster-27x40 ipc-image-media-ratio--poster-27x40 ipc-media--baseAlt ipc-media--poster-l ipc-poster__poster-image ipc-media__img").img['src']
    details["poster_image_url"]=poster


    diractor=soup.find('div',class_="ipc-metadata-list-item__content-container")
    diractor2=diractor.find_all('li',class_="ipc-inline-list__item")
    list_of_diractors=[]
    for li in diractor2:
        list_of_diractors.append(li.a.get_text())
    details["director"]=list_of_diractors


    new_langu=soup.find('li',attrs={"data-testid":"title-details-languages"})
    new1=new_langu.find_all('li',class_="ipc-inline-list__item")
    p1=[]
    for p in new1:
        p1.append(p.a.get_text())
    details["language"]=p1

    contr=soup.find('li',attrs={"data-testid":"title-details-origin"}).a.get_text()
    details["country"]=contr

    bao=soup.find('span',attrs={"data-testid":"plot-l"}).get_text()
    details["bio"]=bao

    gen=soup.find('li',attrs={"data-testid":"storyline-genres"})
    gen1=gen.find('div',class_="ipc-metadata-list-item__content-container").a.get_text()
    details["genre"]=gen1

    return details

scrape_movie_details=[]
try:
    with open('/home/praveen/Desktop/Untitled Folder/task2/task2s.json','r') as tas:
        ta=json.load(tas)
        counter = 0
        for b,c in ta.items():
            for d in c:
                scrape_movie_details.append(movie_scrape_details(d['uri']))
                counter+=1
                print(counter)
    with open('task4s1.json','w') as up:
        json.dump(scrape_movie_details,up,indent=4)

except:
    with open('task4s1.json','w') as up:
        json.dump(scrape_movie_details,up,indent=4) 