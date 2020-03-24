from bs4 import BeautifulSoup
import requests
class Swappa:
    URL = "https://swappa.com/"
    def search(self, srch):
        searchURL = self.URL + "search?q=";
        #https://swappa.com/search?q=iphone+6
        for element in srch:
            if(element==" "):
                searchURL = searchURL + "+";
            else:
                searchURL = searchURL + element;

        print(searchURL);
        r = requests.get(searchURL)
        soup = BeautifulSoup(r.content, 'html5lib')
        print(soup.prettify())

bs = Swappa();
bs.search("iphone 7");
