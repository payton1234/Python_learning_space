import requests
from bs4 import BeautifulSoup
import time
def combine(a, b):
      return a + b

def name_date(website):
    response = requests.get(website)
    soup = BeautifulSoup(response.text, "html.parser")
    titles_name = soup.find_all("div", class_="ev-event-calendar__name")
    titles_date = soup.find_all("h3",class_="ev-event-calendar__date")
    name_list = []
    date_list = []
    for title in titles_name:
        name_list.append(title.select_one("a").getText())
    for title in titles_date:
        date_list.append(title.getText())
    #print(date.getText() for date in titles_date, name.select_one("a").getText() for name in titles_name)
    result_list = list(map(combine, (date_list), (name_list)))
    for i in result_list:
        print(i)

if __name__ == "__main__":
    pages = ["https://www.bbc.co.uk/events/rnc5d4/by/date/2007","https://www.bbc.co.uk/events/rnc5d4/by/date/2008","https://www.bbc.co.uk/events/rnc5d4/by/date/2009","https://www.bbc.co.uk/events/rnc5d4/by/date/2010","https://www.bbc.co.uk/events/rnc5d4/by/date/2011","https://www.bbc.co.uk/events/rnc5d4/by/date/2012","https://www.bbc.co.uk/events/rnc5d4/by/date/2013","https://www.bbc.co.uk/events/rnc5d4/by/date/2014","https://www.bbc.co.uk/events/rnc5d4/by/date/2015"]
    for w in pages:
        name_date(w)
        time.sleep(5)
