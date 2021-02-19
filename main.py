import requests
from bs4 import BeautifulSoup

def main():
    site = requests.get( "https://tsuiran.jp/trend/hourly" )
    data = BeautifulSoup( site.text, "html.parser" )

    #debug
    #print( data.title )

    rank = data.find_all( class_="lazy" )

    hour_title = []

    for item in rank:
        title = item.find( "h2" ).text
        hour_title.append( title )
        #print( title )

    print( hour_title )


if __name__ == '__main__':
    main()

