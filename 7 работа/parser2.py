from bs4 import BeautifulSoup as bs
import codecs
import requests as req

# Загружаем страницу
resp = req.get("https://github.com/explore")
# Получаем DOM модель
doc = bs(resp.text, 'html.parser')

repos = []
# извлечение данных о репозиториях
# выбираем артикулы с информацией
for node in doc.select('article.border.rounded.color-shadow-small.color-bg-secondary.my-4'):
    about_tag=[]
    # выбираем названия реопзиториев
    name_tag = node.select('h1.f3.color-text-secondary.text-normal.lh-condensed a')
    # проверяем нашлось ли название
    if name_tag:
        # получаем первую и вторую часть названия
        name1=name_tag[0].decode_contents().strip()
        name2=name_tag[1].decode_contents().strip()
        # получаем количество звезд
        stars = node.select('a.social-count.float-none')[0].decode_contents().strip()
        # если количество звезд не число
        if not stars.isnumeric():
            # удаляем последний символ "k" и умножаем на 1000
            stars=int(float(stars[:-1])*1000)
        else:
            stars=int(stars)
        # получаем описание реопзитория
        about_tag = node.select("div.px-3.pt-3 div")
        # если описания нет пишем None
        if about_tag:
            about=about_tag[0].decode_contents().strip()
        else: about="None"
        # Добавляем данные в список репозиториев
        repos.append({'name': f"{name1}/{name2}", 'stars': stars, 'about': about})

# выводим список в виде таблицы
print(f'{"Название репозитория":40}  {"Звезды":6} {"Описание":80}')
print('-'*100)
for repo in repos:
    print(f'{repo["name"][:40]:40}  {repo["stars"]:6} {repo["about"]:80}')

print()
# выводим сводные данные
print('Количество репозиториев на странице: ', len(repos))
print('Самое длинное описание:', sorted(repos, key=lambda x: len(x['about']),reverse=True)[0]['about'])
most_popular = sorted(repos, key=lambda x: x['stars'], reverse=True)[0]
print('Больше всего звезд:', most_popular['name'], 'Звезд ', most_popular['stars'])

