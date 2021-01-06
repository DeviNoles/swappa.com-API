from django.http import HttpResponse
from .services import Serv
# Create your views here.
from django.views.generic import TemplateView

class GetSite(TemplateView):
    template_name = 'site.html'
    def get_context_data(self, *args, **kwargs):
        #mycontext = super(template_name, self).get_context_data(**kwargs)
    #    print(self.kwargs['City'])
        myObj = Serv(self.kwargs['City'])
        context = {
            'getID': myObj.getID(),
            'getTitle': myObj.getTitle(),
            'getPrice' : myObj.getPrice(),
            'getURL': myObj.getURL(),
        #    'getImages': myObj.getImages(),
        #    'test': parseSwappaObject(self),
            #'returnedItems': getItems(self),
        }
        return context


def index(request):

    #print(bs.local("phoenix"));# any city from https://swappa.com/local and some acronyms (nyc, phnx, sd, etc);
    rethtml = """<!DOCTYPE html>
<html>
<body>

<h2>Swappa.com API Example</h2>

<form action="Phoenix"
  <label for="cname">City Name:</label><br>
  <input type="text"><br>
  <input type="submit" value="Submit">
</form>

<p>Clicking the search button will use the Swappa API to scrape swappa.com for results.</p>

</body>
</html>""" #html im gonna return
    return HttpResponse(rethtml)
