# Swappa Python Library

Here's a Python package to access data from Swappa.

https://swappa.com/

To-Do
- [X] Organize retrieved data into JSON
- [X] Local
- [ ] Add url's of listing into returned JSON object
- [ ] Carrier
- [ ] Brand
- [ ] Top Menu Search
- [ ] Seller API
- [ ] Documentation

```
cd swappa
pip3 install -r bin/requirements.txt
source bin/activate
```

## code is in src/Swappa.py

## DOCUMENTATION
### Here is what works so far
```
bs = Swappa();
print(bs.search("iphone 7"));
print(bs.local("phoenix")); #from https://swappa.com/local and some acronyms (nyc, phnx, sd, etc)
```

### open issues pls
