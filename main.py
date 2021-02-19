# coding: utf-8
import requests
from bs4 import BeautifulSoup

class LineSend:
    def __init__( self, notification_message ):
        self.message = notification_message
        LineSend.send( self )

    def send( self ):
        line_notify_token = 'mVZ91mHwvZS2X3QE6qXL1JbbMKJSn1pnSF2RVoCXHdS'
        line_notify_api = 'https://notify-api.line.me/api/notify'
        headers = { 'Authorization': f'Bearer {line_notify_token}' }
        data = { 'message': f'{self.message}' }
        requests.post( line_notify_api, headers = headers, data = data )


def main():
    site = requests.get( "https://tsuiran.jp/trend/hourly" )
    data = BeautifulSoup( site.text, "html.parser" )

    #debug
    #print( data.title )

    rank = data.find_all( class_="lazy" )

    hour_title = []
    str_title = ""

    for item in rank:
        title = item.find( "h2" ).text
        hour_title.append( title )
        str_title += "\n" + title
        #print( title )

    print( hour_title )
    LineSend( str_title )

if __name__ == '__main__':
    main()

