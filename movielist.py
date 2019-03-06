import bs4 as bs
import sys
import urllib.request
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl

class Page(QWebEnginePage):
    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebEnginePage.__init__(self)
        self.html = ''
        self.loadFinished.connect(self._on_load_finished)
        self.load(QUrl(url))
        self.app.exec_()

    def _on_load_finished(self):
        self.html = self.toHtml(self.Callable)
        #print('Load finished')

    def Callable(self, html_str):
        self.html = html_str
        self.app.quit()

#This is the URL from the oscars awards database that has all movies ever nominated
url='http://awardsdatabase.oscars.org/Search/GetResults?query=%7B%22AwardCategory%22:[%229998%22,%221%22,%222%22,%223%22,%224%22,%225%22,%226%22,%227%22,%228%22,%229%22,%2210%22,%229997%22,%2211%22,%2212%22,%2213%22,%2214%22,%2215%22,%2216%22,%2217%22,%2218%22,%2219%22,%2220%22,%2221%22,%2222%22,%2223%22,%2224%22,%2225%22,%2226%22,%2227%22,%2228%22,%2229%22],%22Sort%22:%222-Film%20Title-Alpha%22,%22Search%22:%22Basic%22%7D'

#Opens the webpage
source = Page(url)

#BeautifulSoup retrieves the HTML
soup = bs.BeautifulSoup(source.html, 'html.parser')

#saving the movies to a file
file=open('movielist.txt','w')

for nom in soup.find_all('div',class_='result-group-title'):
	film = nom.a.text #this is the name of a movie
	file.write(film)
	file.write('\n')
	print(film)

file.close()
