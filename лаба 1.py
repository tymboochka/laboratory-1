import requests
web = requests.get('https://dfedorov.spb.ru/python3/sport.txt')
web.encoding = 'cp1251'
sport_cnt = {}
text = web.text
for i in text.split('\n'):
    clmn = i.strip().split('\t')
    if len(clmn) >= 4:
        sports = clmn[3]
        for sport in sports.split(','):
            sport_improve = sport.strip().lower()
            if sport_improve:
                sport_cnt[sport_improve] = sport_cnt.get(sport_improve, 0) + 1
top_3 = sorted(sport_cnt.items(), key=lambda x: x[1], reverse=True)[:3]
print("Три наиболее популярных вида спорта в стране:")
for i, (sport, count) in enumerate(top_3, 1):
    print(f"{i}. {sport.capitalize()} - {count} объектов")
