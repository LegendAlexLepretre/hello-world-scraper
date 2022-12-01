from bs4 import BeautifulSoup
import flask
from io import StringIO
import sys
from urllib.request import urlopen

app = flask.Flask(__name__)
app.config["DEBUG"] = True


def scrape_hello_world():
    # Let's scrape this amazing website to find a Hello World
    page = urlopen('http://helloworldcollection.de/')
    soup = BeautifulSoup(page, "html.parser")

    # Honestly I'm not even sure what this does
    element = soup.body.find('a', {"name": "Python" + u'\xa0' + "3"})
    code = element.find_next('pre').text

    # Who likes variables? let's capture the terminal output instead
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()

    # This is where the magic happens
    eval(code)

    # I promise this wasn't copy/pasted from StackOverflow
    sys.stdout = old_stdout
    message = mystdout.getvalue()
    return message


@app.route('/', methods=['GET'])
def home():
    return f"<h1>{scrape_hello_world()}</h1>"


app.run()
