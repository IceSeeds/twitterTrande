# coding: utf-8
import csv
import datetime
import time

import schedule
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

    hour_title = []
    str_title = ""
    temp = []

    dt_now = datetime.datetime.now()
    dt_now = dt_now.strftime( '%Y年%m月%d日 %H:%M:%S' )
    header = ['date', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
    
    temp.append( dt_now )

    rank = data.find_all(class_="lazy")
    for item in rank:
        title = item.find( "h2" ).text
        temp.append( title )
        str_title += "\n" + title
        #print( title )
    hour_title.append( temp )

    print( hour_title )
    #LineSend( str_title )

    with open('trend.csv', "a", newline="", encoding = "utf-8") as csvfile:
        writer = csv.writer( csvfile, lineterminator='\n' )
        #writer.writerow( header )
        writer.writerows( hour_title )


if __name__ == '__main__':
    schedule.every( 1 ).hours.do( main )

    while True:
        schedule.run_pending()
        time.sleep( 1 )
