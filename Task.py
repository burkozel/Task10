import requests

names = [{"name": "Thanos"}, {"name": "Hulk"}, {"name": "Captain America"}]
response = requests.get("https://superheroapi.com/api/2619421814940190/search/")
for name in names:
    hero_stats = requests.get("https://superheroapi.com/api/2619421814940190/search/" + name["name"])
    name["intelligence"] = int(hero_stats.json()["results"][0]["powerstats"]["intelligence"])
print(sorted(names, key= lambda name: -name["intelligence"])[0]["name"])