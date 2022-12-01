# Authors

* 🇫🇷 Philippe Alvais
* 🇧🇷 Alexandre Opadre

# Introduction
Help! We don't know how to write a "Hello World!" program however we know how to scrape pages. 😱

That's where our genius kicked in. 🤯

Because we don't know how to print Hello World, we rely on that fantastic website that has Hello Worlds in hundreds of programming languages: http://helloworldcollection.de/

Our scraper then navigates the DOM to find the Hello World code that's relevant for Python 3

Once the code is extracted, a simple `eval()` executes the remote code and prints **Hello World**

... which we then **PACKAGED IN A FLASK API**

![Sometimes, my genius... it's almost frightening](https://media.tenor.com/0YzwtDxPt4AAAAAC/jeremy-clarkson-sometimes-my-genius.gif)

# Requirements

* Python 3.9
* Too much caffeine
* The brains of mad men

# How to run?

`python3 main.py`