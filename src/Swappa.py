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
                elif(l == ' ' and wordCount==1):
                    wordCount = wordCount + 1;
                elif(l == '('):
                    phone['model'] = buffer[1:];
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
                buffer="";
                phone['carrier'] = "N/A";
            """print("ID:" + str(phone['id']));
            print("Make:" + phone['make']);
            print("Model:" + phone['model']);
            print("Carrier:" + phone['carrier']);"""
            phones.append(phone);

            rowCount = rowCount + 1;

    def local(self, city):
        searchURL = self.URL+"local/";
        if(city=="phoenix" or city=="arizona" or city=="az" or city =="phx" or city=="px"):
            searchURL = searchURL + "phoenix";
        elif(city=="dc" or city=="washington dc"):
            searchURL = searchURL + "washington-dc";
        elif(city=="chicago" or city=="illinois"):
            searchURL = searchURL + "chicago";
        elif(city=="detroit" or city=="michigan"):
            searchURL = searchURL + "detroit";
        elif(city=="charlotte"):
            searchURL = searchURL + "charlotte";
        elif(city=="raleigh" or city == "durham"):
            searchURL = searchURL + "raleigh-durham";
        elif(city=="cincinatti"):
            searchURL = searchURL + "cincinnati";
        elif(city=="cleveland" or city=="akron"):
            searchURL = searchURL + "cleveland-akron";
        elif(city=="columbus"):
            searchURL = searchURL + "columbus";
        elif(city=="austin"):
            searchURL = searchURL + "austin";
        elif(city=="dallas" or city=="ft worth" or city=="ft. worth" or city=="ft.worth"):
            searchURL = searchURL + "dallas-fort-worth";
        elif(city=="houston"):
            searchURL = searchURL + "houston";
        elif(city=="san antonio"):
            searchURL = searchURL + "san-antonio";
        elif(city=="la" or city=="los angeles"):
            searchURL = searchURL + "los-angeles";
        elif(city=="orange county"):
            searchURL = searchURL + "orange-county";
        elif(city=="sacramento"):
            searchURL = searchURL + "sacramento";
        elif(city=="san-diego"):
            searchURL = searchURL + "san-diego";
        elif(city=="san-francisco"):
            searchURL = searchURL + "san-francisco";
        elif(city=="miami" or city=="ft lauderdale" or city=="ft. lauderdale" or city=="fort lauderdale" or city=="miami" or city == "broward" or city=="miami dade"):
            searchURL = searchURL + "miami-fort-lauderdale";
        elif(city=="orlando"):
            searchURL = searchURL + "orlando";
        elif(city=="tampa"):
            searchURL = searchURL + "tampa";
        elif(city=="boston"):
            searchURL = searchURL + "boston";
        elif(city=="minneapolis" or city=="st. paul" or city=="st paul" or city=="st.paul"):
            searchURL = searchURL + "minneapolis-st-paul";
        elif(city=="las vegas" or city=="nevada"):
            searchURL = searchURL + "las-vegas";
        elif(city=="oregon" or city=="portland"):
            searchURL = searchURL + "portland";
        elif(city=="tacoma" or city=="seattle"):
            searchURL = searchURL + "seattle-tacoma";
        elif(city=="denver" or city=="colorado"):
            searchURL = searchURL + "denver";
        elif(city=="atlanta" or city=="georgia" or city=="atl"):
            searchURL = searchURL + "atlanta";
        elif(city=="baltimore" or city=="maryland"):
            searchURL = searchURL + "baltimore";
        elif(city=="baltimore" or city=="maryland"):
            searchURL = searchURL + "baltimore";
        elif(city=="kansas-city"):
            searchURL = searchURL + "kansas-city";
        elif(city=="st. louis" or city=="st.louis" or city=="st louis"):
            searchURL = searchURL + "st-louis";
        elif(city=="nyc" or city=="new york" or city=="new york city"):
            searchURL = searchURL + "new-york-city";
        elif(city=="philadelphia" or city=="pennsylvania" or city=="pa" or city=="philly"):
            searchURL = searchURL + "philadelphia";
        print(searchURL);

bs = Swappa();
bs.search("iphone 7");
bs.local("broward")
