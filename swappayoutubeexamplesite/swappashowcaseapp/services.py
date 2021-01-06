from .Swappa import Swappa
import json
#Here is what works so far
swappaObj = Swappa();
searchResult = swappaObj.local("phoenix");
#searchResult = ""
class Serv:

    def __init__(self, city):
        self.city = city
        print(swappaObj.local("phoenix"))
        self.searchResult = swappaObj.local("phoenix")
    def parseSwappaObject(self):
        for item in searchResult: #iterate through returned object
            #print(item) #uncomment to see the raw json object
            jsonObj = json.loads(item) #item gets loaded into json class for it to do all the parsing for us
            #print(jsonObj["id"])
            #print(jsonObj["title"])
            #print(jsonObj["price"])
            #print(jsonObj["url"])
        #print(bsl);
        return(searchResult);# any city from https://swappa.com/local and some acronyms (nyc, phnx, sd, etc);
        #return(bs.search("iphone 7"))
    def getID(self):
        IDresultArray = []
        for item in searchResult: #iterate through returned object
        #    print(item) #uncomment to see the raw json object
            jsonObj = json.loads(item) #item gets loaded into json class for it to do all the parsing for us
            resultid = jsonObj["id"]
            IDresultArray.append(resultid)
        return (IDresultArray)
    def getTitle(self):
        titleresultArray = []
        for item in searchResult: #iterate through returned object
        #    print(item) #uncomment to see the raw json object
            jsonObj = json.loads(item) #item gets loaded into json class for it to do all the parsing for us
            resulttitle = jsonObj["title"]
            titleresultArray.append(resulttitle)
        return (titleresultArray)
    def getPrice(self):
        priceresultArray = []
        for item in searchResult: #iterate through returned object
        #    print(item) #uncomment to see the raw json object
            jsonObj = json.loads(item) #item gets loaded into json class for it to do all the parsing for us
            resultprice = jsonObj["price"]
            priceresultArray.append(resultprice)
        return (priceresultArray)
    def getURL(self):
        URLresultArray = []
        for item in searchResult: #iterate through returned object
        #    print(item) #uncomment to see the raw json object
            jsonObj = json.loads(item) #item gets loaded into json class for it to do all the parsing for us
            resulturl = jsonObj["url"]
            URLresultArray.append(resulturl)
        return (URLresultArray)


    def getItems(self):
        retarray = {
        "id": getID(self),
        "price": getPrice(self),
        "title": getTitle(self),
        "getPrice": getURL(self),
    }
        print(retarray)
        return retarray
