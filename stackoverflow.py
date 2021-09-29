import requests
from datetime import date


# Задание №3 - Получение вопросов с форума StackOverflow
class StackOverflow():
    def __init__(self, fromdate, todate, tagged, site):
        self.fromdate = fromdate
        self.todate = todate
        self.tagged = tagged
        self.site = site

    def get_questions(self):
        url = 'https://api.stackexchange.com/2.3/questions'
        params = {
            'fromdate': self.fromdate,
            'todate': self.todate,
            'tagged': self.tagged,
            'site': self.site
        }
        response = requests.get(url=url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return 'Bad request'
