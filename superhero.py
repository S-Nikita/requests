import requests

# Задание №1 - Поиск самого умного супергероя


class SuperHero():
    def __init__(self, name):
        self.name = name

    # Поиск идентификатора героя в базе данных по имени
    def get_id_by_name(self):
        if self.name.upper() == 'HULK':
            self.id = 332
        elif self.name.upper() == 'CAPTAIN AMERICA':
            self.id = 149
        elif self.name.upper() == 'THANOS':
            self.id = 655
        else:
            print('Указанный Вами герой не рассматривается в рамках задачи')

    # Получение информации о герое по его идентификатору при помощи обращения к API
    def make_request(self):
        token = '2619421814940190'
        url = f'https://superheroapi.com/api/{token}/{self.id}/powerstats'

        response = requests.get(url=url)
        if response.status_code == 200:
            self.intelligence = response.json()['intelligence']
            print(f"{self.name} intelligence level is {self.intelligence}")

    # Анализ показателей интеллекта каждого из героев на максимальное значение
    def most_intelligent_hero(self, other_hero_1, other_hero_2):
        if isinstance(other_hero_1, SuperHero) and isinstance(other_hero_2, SuperHero):
            heroes_info = []
            heroes_info.append(
                {'name': self.name, 'intelligence': self.intelligence})
            heroes_info.append(
                {'name': other_hero_1.name, 'intelligence': other_hero_1.intelligence})
            heroes_info.append(
                {'name': other_hero_2.name, 'intelligence': other_hero_2.intelligence})

            max_intellegence = 0
            for hero in heroes_info:
                print(hero['intelligence'])
                if int(hero['intelligence']) > max_intellegence:
                    max_intellegence = int(hero['intelligence'])
                    most_intelligent_hero = hero['name']
            return f'Самый умный герой - {most_intelligent_hero}'
        else:
            return 'Введенный Вами персонаж не является супергероем'
