from bs4 import BeautifulSoup
import requests
from datetime import datetime
from config import headers
import calendar


class Scraper:

    def __init__(self, url):
        req = requests.get(url, headers)
        self.content = BeautifulSoup(req.content, 'html.parser')
        self.slots = []

    def get_slots(self):
        items = self.content.findAll('div', {'class': 'col-md-4'})
        for item in items:
            try:
                for slot in item.findAll('li'):
                    time_stamp = datetime.fromtimestamp(
                                int(slot.find('span', itemprop='startDate').get('url-timestamp'))
                            )
                    self.slots.append(
                        {
                            'type': slot.find('article').get('data-name'),
                            'weekday': calendar.day_name[time_stamp.weekday()],
                            'places': int(slot.find('article').get('data-places-available')),
                            'date_stamp': datetime.fromtimestamp(
                                int(slot.find('span', itemprop='startDate').get('url-timestamp'))
                            ).strftime('%Y-%m-%d'),
                            'time_start': slot.find('span', itemprop='startDate').get_text(),
                            'time_end': slot.find('span', itemprop='endDate').get_text(),
                            'time_stamp': time_stamp.strftime('%Y-%m-%d %H:00'),
                        }
                    )
            except:
                pass


if __name__ == '__main__':
    scraper = Scraper('https://www.fitforfree.nl/groepslessen/rotterdam-conradstraat')
    scraper.get_slots()

# data-places-available
