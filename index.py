#import the necessary libs
import sys
from bs4 import BeautifulSoup as bs

def addAriaLabels(path):
    soup = bs(open(path), 'html.parser')
    for inp in soup.find_all('input'):
      inp['aria-label'] = inp.get('placeholder', '')

    #write the file
    html = soup.prettify("utf-8")
    with open("output.html", "wb") as file:
        file.write(html)

if __name__ == "__main__":
    #call the function to add aria-labels to input tags
    addAriaLabels(sys.argv[1])
