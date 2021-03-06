import requests
import re
from urllib.parse import urlparse
from BeerClass import Beers, Websites, PubWebsite

beer_type = {'Stout', 'IPA', 'ESB', 'Blonde', 'Scotch Ale', 'Sour Ale', 'Porter', 'Rye-ot', 'Rye', 'Ale', 'Pale Ale' }

# list of drink objects
drinks = list()



#### FIND REGEX FOR ONETREE AND PUT THEM IN ITS CLASS, start with partURL here (work on the RegEx so it returns valid url's)

# finds potential URLS from a website
def Crawler(URL, partURL):
    urls = set() 
    nextUrl = set()

    #url is the website that is being crawled through)
    r = requests.get(URL, allow_redirects=True)

    #download html from the webcrawler 
    open('url.txt', 'wb').write(r.content)

    #open the txt file for searching
    file = open('url.txt', "r")

    # find potential URLS
    for line in file:
        while line:
            m = re.search(partURL, line)
            if m:
                urls.add(m.group(1))
                n = m.end()
                line = line[n+1:]
                #print(m.group(1))
            else:
                break


    #create new URL's using the base url + url extension from webcrawler
    for val in urls:
            #duplicate URLS will be valid google searches, this prevents that from happening
          #  copy = re.search(URL, val)
          #  if copy:
          #      q = re.search("(https://www.onetreehardcider.com/)(.*?)/", val)
          #      if q:
          #          val = q.group(2)
          #
          #      #test if the urls are valid. if not throw an exception
          #      try:
          #          newUrl = URL + val
          #          x = requests.get(newUrl) # https://stackoverflow.com/questions/16778435/python-check-if-website-exists
          #          if x.status_code == 200:
          #              nextUrl.add(newUrl)
          #      except IOError:
          #          print(newUrl, " ---- url invalid") 
          #          (newUrl, " ---- url invalid")
          #
          #  else:
          #      try:
          #          x = requests.get(val) # https://stackoverflow.com/questions/16778435/python-check-if-website-exists
          #          if x.status_code == 200:
          #              nextUrl.add(val)
          #      except IOError:
          #          print(newUrl, " ---- url invalid") 
          #          (val, " ---- url invalid")     



        #try:
        #    newUrl = URL + val
        #    x = requests.get(newUrl) # https://stackoverflow.com/questions/16778435/python-check-if-website-exists
        #    if x.status_code == 200:
        #        nextUrl.add(newUrl)
        #
        #except IOError:
        #    print(newUrl, " ---- url invalid") 
        #    (newUrl, " ---- url invalid")



        if val == "https://untappd.com/v/one-tree-cider-house/6394441" or val == "/our-beers":
            if val == "/our-beers":
                val = 'http://www.irongoatbrewing.com/our-beers'
            nextUrl.add(val)
            return(nextUrl)
    return(nextUrl)


# searches valid URLS for info from a specific site
def findInfo(newUrl_, endofURL_, brewery_, name_, Type_, ABV_, IBU_, description_):
    #go through new list of urls and start getting content
    for val in newUrl_:
        #open the url
        x = requests.get(val, headers = {'User-agent': 'your bot 0.1'})

        open('url.txt', 'wb').write(x.content)

        #save the url as an html, then open it to work on
        html = open('url.txt', encoding = 'utf8')
        
        #combine all the strings of each url's HTML into one string. (\n = white space)
        response = ' '.join(html)
        
        d = re.search(endofURL_, response)

        #while statement keeps this loop open until html is completely searched
        #each html will have the same brewery the drinks are from, so this is set ahead of time.
        beer = Beers()



        # BREWERY check
        breweryy = re.search(brewery_, response)
        brewery = breweryy.group(2)  
        while d:
            i = 0
            
            # NAME check
            if len(beer.__getName__()) == 0:
                name = re.search(name_, response)
                if name.group(2)[0] == " ":
                    edit_name = name.group(2)[1:]
                    beer.setName(edit_name)
                else:
                    beer.setName(name.group(2))

            # TYPE          
            while len(beer.__getBeerType__()) == 0:
                f = re.search(Type_, response)

                # this is to find the cider type
                if f:
                    fg = f.group(1)
                    if fg == "Cider":
                        beer.setBeerType(f.group(1))  
                        break

                # this is to find all other types        
                for bt in beer_type:
                    #if a beertype exists end this loop
                    if len(beer.__getBeerType__()) != 0:
                        #print('----------------------------------------------------------------------------')
                        break
                    stringname = str(name.group(2))
                    while (stringname): 
                        #print (stringname, bt)
                        #if the beer type os found add it
                        if (stringname == bt):
                            beer.setBeerType(stringname)
                            break
                        #concatenate string, removing first word in string
                        else:
                            whitespace = re.search("^([\w\-]+)|&*", stringname)
                            e = whitespace.end()
                        stringname = stringname[1+e:]
            
            # ABV and IBU
            ibu_or_abv = re.search(ABV_, response)
            if len(beer.__getABV__()) == 0:
                #this is only for Iron Goat
                if ibu_or_abv.group(1) == "ABV": 
                    beer.setABV(ibu_or_abv.group(2))
                #this is only for one Tree
                if ibu_or_abv.group(2) == "ABV":
                    beer.setABV(ibu_or_abv.group(1))
                    beer.setIBU("0")
                
            if len(beer.__getIBU__()) == 0:
                if ibu_or_abv.group(1) == "IBU":
                    beer.setIBU(ibu_or_abv.group(2))

            #Splice from here back
            i = ibu_or_abv.end()

            #strip this previous stuff off the string get i to be the end of the previously wanted statement
           

            #if beer has ibu and abv, find description then add beer to list
            if len(beer.__getABV__()) != 0 and len(beer.__getIBU__()) != 0:
                description = re.search(description_, response)
                if description:
                    edit = description.group(2)

                    #edit the desci. so it is normal english
                    #needed because not all descr. have the same html syntax so they need editing
                    if edit[0:3] == "<p>" and edit[-1] == ">":
                        edit = (description.group(2)[3:-4])
                        beer.setBeerDescription(edit)
                    else:
                        beer.setBeerDescription(description.group(2))

                else:
                    beer.setBeerDescription("No description given")

                beer.setBrewery(brewery)                    
                drinks.append(beer)
                beer = Beers()   

            response = response[i+1:]
            d = re.search(endofURL_, response)
    return drinks


# print the drinks that have been found
def returnInfo(drinks):
    #print(' ')
    #print(nextUrl)
    print('yikes ')

    for a in drinks:
        print(a.__getName__(), a.__getBeerType__(), a.__getBrewery__(), a.__getIBU__(), a.__getABV__())
        print(a.__getBeerDescription__())

        print('-------------------------------------------------------------------')