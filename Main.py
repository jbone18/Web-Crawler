from PythonCrawler import Crawler, findInfo, returnInfo
from BeerClass import Beers, Websites, PubWebsite
from database import main, delete

urls = set()
drinkInfo = set()
website = Websites()

for a in website.baseURL:
    urls = Crawler(a.URL, a.newURL)
    drinkInfo = findInfo(urls, a.endOfURL, a.brewery, a.name, a.Type, a.ABV, a.IBU, a.description)
    returnInfo(drinkInfo)
    print("==================================================================================")


delete()

for i in drinkInfo:
    main(i)