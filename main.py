import requests
import time


class StackOverflow:
    def __init__(self, tag):
        self.tag = tag

    def get_questions(self):
        url = 'https://api.stackexchange.com/2.2/questions'
        date_list = []
        date_two_days_ago = int(time.time() - 172800)
        date_one_days_ago = int(time.time() - 86400)
        date_list.append(date_one_days_ago)
        date_list.append(date_two_days_ago)

        for date in date_list:
            params = {
                'fromdate': date,
                'order': 'asc',
                'sort': 'creation',
                'tagged': self.tag,
                'site': 'stackoverflow'
            }
            resp = requests.get(url, params=params, timeout=5).json()
            items = resp['items']

            for item in items:
                print(item['title'])


if __name__ == '__main__':
    stack_overflow = StackOverflow('Python')
    stack_overflow.get_questions()
