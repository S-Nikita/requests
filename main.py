from stackoverflow import StackOverflow
from superhero import SuperHero
from ya import YaUploader
import sys
import datetime
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

if __name__ == '__main__':
    # Поиск самого умного супергероя
    hulk = SuperHero('Hulk')
    hulk.get_id_by_name()
    hulk.make_request()

    captain_america = SuperHero('Captain America')
    captain_america.get_id_by_name()
    captain_america.make_request()

    thanos = SuperHero('Thanos')
    thanos.get_id_by_name()
    thanos.make_request()

    print(hulk.most_intelligent_hero(thanos, captain_america))

    # Загрузка файла на ЯДиск
    path_to_file = 'API_TEST/upload.txt'
    file = 'upload.txt'
    token = 'TOKEN_PLACEHOLDER'
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
    print(result)

    # Получение аопросов по Python со StackOverflow
    todate = datetime.date.today()
    fromdate = todate - datetime.timedelta(days=2)
    tagged = 'python'
    site = 'stackoverflow'
    data = StackOverflow(fromdate, todate, tagged, site)
    stackoverflow_result = data.get_questions()
    print(stackoverflow_result)
