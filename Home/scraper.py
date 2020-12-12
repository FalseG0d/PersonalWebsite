import requests as re
from bs4 import BeautifulSoup
from .models import Game,Article


def game_Scraper():
    url="https://falseg0d.itch.io/"

    r=re.get(url)
    htmlcontent=r.content

    soup=BeautifulSoup(htmlcontent,'html.parser')

    context=[]

    for link in soup.find_all('a',class_="title game_link"):
        context.append(link.string)

    for link in soup.find_all('a',class_="thumb_link game_link"):
        context.append(link.get('href'))

    for link in soup.find_all('div',class_="game_thumb"):
        context.append(link.get('style').split('\'')[1])

    for link in soup.find_all('div',class_="game_text"):
        context.append(link.string)

    for link in soup.find_all('div',class_="game_genre"):
        context.append(link.string)


    Game.objects.all().delete()
    x=len(context)/5
    x=int(x)

    for i in range(x):
        game=Game(name=context[i],itch_link=context[x*1+i],image=context[x*2+i],description=context[x*3+i],genre=context[x*4+i])
        
        game.save()


def article_Scraper():
    url="https://gargapoorv1011.medium.com/"

    r=re.get(url)
    htmlcontent=r.content

    soup=BeautifulSoup(htmlcontent,'html.parser')

    context=[]

    for link in soup.find_all('a',class_="di bo"):
        context.append(link.string)

    for link in soup.find_all('a',class_="di bo"):
        context.append('https://gargapoorv1011.medium.com'+link.get('href'))

    for tag in soup.find_all('p',class_='gr'):
        context.append(tag.string)

    Article.objects.all().delete()
    x=len(context)/3
    x=int(x)

    print(context)

    for i in range(x):
        game=Article(name=context[i],link=context[x*1+i],abstract=context[x*2+i])
        
        game.save()
