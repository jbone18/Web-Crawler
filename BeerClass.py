    # create another class, Websites, which will be the parent of BeerClass
    # Websites will have a base URL, potential URLS... as well as a list of beers
    # the list of beers will be what references ClassBeers (Beers have a Webite)
    # this will connect all the beers to a specific website to help organize 
    # both the database and the RegEx code.

class Websites:
    def __init__(self, baseURL=set(), checkURL=set(), validURL=set()):
        #pub website objects for each base URL
        # http://www.irongoatbrewing.com', https://www.onetreehardcider.com/
        # URL, newURL, endOfURL, brewery, name, Type, ABV, IBU, description
        self.baseURL = (PubWebsite( 'https://www.onetreehardcider.com/', #URL
                                    "href=\"(.*?)\"", #newURL
                                    'data-href=":beer" href=".*>(1|2|3|4|5|6|7|8|9|0).(.*)</a>\s<em', #endOfURL
                                    '(<title>)(One Tree Cider House)', #brewery group(2)
                                    'data-href=":beer" href=".*>(1|2|3|4|5|6|7|8|9|0).(.*)</a>\s<em', #name group(2)
                                    'data-href=":beer" href=".*>\s<em>(.*)\s-', #type group(1)
                                    '<span>(.*?)%\s(ABV)\s•\s(.*?)IBU.*', #ABV group(1), IBU group(2)
                                    '', #IBU is included in ABV RegEx
                                    '----------------------'), PubWebsite('http://www.irongoatbrewing.com', 
                                    "<a href=\"(.*?)\"", #newURL
                                    "<div\sclass=\"cube\">", #endOfURL
                                    '(Our Beers \|)\s*(Iron Goat Brewing)', #brewery group(2)
                                    '<h3><a\s*?(.*?>)(.*?)</a>', #name group(2)
                                    '------------------------------------------', #type
                                    '<div\sclass=\"cube\">\s*?(\w*?)\s*?<div class=\"value\">(.*?)</div>\s*?(.*?)\s*?</div>', #ABV 
                                    '',
                                    '(Bitterness Units\s*?</div>\s*?<br>)\s*(.*)(\s*?</div>)')) # get a new PubWebsite object for each website to be crawled
        self.checkURL = checkURL
        self.validURL = validURL

    def setBaseURL(self, base):
        self.baseURL = base
    def setCheckURL(self, check):
        self.checkURL = check
    def setValidURL(self, valid):
        self.validURL = valid


    def __getBaseURL__(self):
        return self.baseURL
    def __getCheckURL__(self):
        return self.checkURL
    def __getValidURL__(self):
        return self.validURL

class PubWebsite:
    def __init__(self, URL, newURL, endOfURL, brewery, name, Type, ABV, IBU,description):
        self.URL = URL
        self.newURL = newURL
        self.endOfURL = endOfURL
        self.brewery = brewery
        self.name = name
        self.Type = Type
        self.ABV = ABV
        self.IBU = IBU
        self.description = description


    def __getURL__(self):
        return self.URL

class Beers: 
    # init prevents inheritance of Websites init function
    def __init__(self, Btype='', name = '', brewery='', ibu = '', abv = '', Bdescr=''):
        #Websites.__init__()
        self.Btype = Btype
        self.name = name
        self.brewery = brewery
        self.ibu = ibu
        self.abv = abv
        self.Bdescr = Bdescr
   
    def setBeerType(self, bt):
        self.Btype = bt
    def setName(self, n):
        self.name = n
    def setBrewery(self, b):
        self.brewery = b
    def setIBU(self, i):
        self.ibu = i
    def setABV(self, a):
        self.abv = a
    def setBeerDescription(self, bd):
        self.Bdescr = bd 


    def __getBeerType__(self):
        return self.Btype
    def __getName__(self):
        return self.name
    def __getBrewery__(self):
        return self.brewery
    def __getIBU__(self):
        return self.ibu 
    def __getABV__(self):
        return self.abv
    def __getBeerDescription__(self):
        return self.Bdescr
  