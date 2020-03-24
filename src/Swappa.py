from bs4 import BeautifulSoup
import requests
import json
class Swappa:
    URL = "https://swappa.com/"
    def search(self, srch):
        phones = [];
        searchURL = self.URL + "search?q=";
        #https://swappa.com/search?q=iphone+6
        for element in srch:
            if(element==" "):
                searchURL = searchURL + "+";
            else:
                searchURL = searchURL + element;

        print(searchURL);
        r = requests.get(searchURL);
        soup = BeautifulSoup(r.content, 'html5lib');
        #print(soup.prettify());
        wrap = soup.find('div', attrs = {'id':'wrap'});
        table = wrap.find('section', attrs = {'class':'section_main'});
        row = table.find('div', attrs = {'class':'row'});
        rowCount = 0;
        for rows in row.findAll('div', attrs = {'class':'col-xs-6 col-sm-3 col-md-2'}):
            phone = {};
            cps = rows.find('div', attrs = {'class':'cell_product search'});
            phoneLinkTitle= cps.find('a', attrs = {'class':'image'});
            phoneLinkTitle = phoneLinkTitle['title'];
            #print(phoneLinkTitle);
            #print(phoneLinkTitle.text);
            wordCount = 0;
            buffer = "";
            carrier = False;
            for l in phoneLinkTitle:
                phone['id'] = rowCount;
                if(l == ' ' and wordCount==0):
                    phone['make'] = buffer;
                    buffer = "";
                    wordCount = wordCount + 1;
                    #print(phone['make']);
                elif(l == ' ' and wordCount==1):
                    #phone['make'] = buffer;
                    #buffer = "";
                    wordCount = wordCount + 1;
                elif(l == '('):
                    #print(phone['make']);
                    phone['model'] = buffer[1:];
                    #print(phone['model']);
                    buffer="";
                    carrier = True;
                elif(l == ' '):
                    wordCount = wordCount + 1;
                elif(l == ')'):
                    phone['carrier'] = buffer[1:];
                    buffer = "";
                buffer = buffer + l;
            if(len(buffer)>0 and carrier == False):
                phone['model'] = buffer[1:];
                #print(phone['model']);
                buffer="";
                phone['carrier'] = "N/A";
            print("ID:" + str(phone['id']));
            print("Make:" + phone['make']);
            print("Model:" + phone['model']);
            print("Carrier:" + phone['carrier']);
            phones.append(phone);

            rowCount = rowCount + 1;

    def local(self, zip):
        print(zip);

bs = Swappa();
bs.search("iphone 7");
