import os
from datetime import timedelta, date, datetime
from scraper import Scraper
import pandas as pd
import argparse

class Engine(Scraper):

    def __init__(self, url, type, dates):
        super(Engine, self).__init__(url)
        self.get_slots()
        self.df = pd.DataFrame(self.slots)
        self.type = type
        self.dates = dates
        now = datetime.now()
        self.dt_string = now.strftime("%Y-%m-%d %H:%M")
        self.process()

    def process(self):
        self.filter()
        if not os.path.isdir('./data'):
            os.mkdir('./data')
        if self.df.shape[0] > 0:
            token = self.df['time_stamp']
            token.to_csv('./data/new_token.csv')
            self.df.to_csv('./data/new.csv')

    def convert_dates(self, dates):
        date_items = []
        for date_item in dates:
            date_items.append((date.today() + timedelta(days=date_item)).strftime("%Y-%m-%d"))
        return date_items

    def filter(self):
        # remove past slots
        # filter on type
        # filter on dates
        # at least one place av
        dates = self.convert_dates(self.dates)
        self.df = self.df[
            (self.df['time_stamp'] > self.dt_string) &
            (self.df['type'] == self.type) &
            (self.df['date_stamp'].isin(dates)) &
            (self.df['places'] > 0 )
        ]





if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--days', metavar='N', type=str, nargs='+',
                        help='an integer for the accumulator')
    args = parser.parse_args()
    dates = args.days[0].replace(' ', '').split(',')
    try:
        dates = args.days[0].replace(' ', '').split(',')
        ndates =[]
        for x in dates:
            ndates.append(int(x))
    except:
        print('Days are not configured correctly')
        exit(0)
    engine = Engine(
        url='https://www.fitforfree.nl/groepslessen/rotterdam-conradstraat',
        type='Vrije Fitness',
        dates=ndates
                    )
    print('done')
# data-places-available
