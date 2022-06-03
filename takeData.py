from multiprocessing.managers import ListProxy
import bs4
import requests
class TakeData():
    def __init__(self, link):
        self.link = link
        self.startScan()

    def startScan(self):
        r = requests.get(self.link)
        self.source = bs4.BeautifulSoup(r.content,"lxml")

    def arananKelimeler(self, kelimeler, kelimeFrekansi = False, inboundLink = False):
        allLink = list()
        allLink.append(self.link)
        resultLink = list()
        for kelime in kelimeler:
            for i in self.source.find_all('a'):
                a = 0
                newlink = 'https://ois.istinye.edu.tr'+i.get('href')
                allLink.append(newlink)

                linkRequests = requests.get(newlink)
                linkSource = bs4.BeautifulSoup(linkRequests.content, 'lxml')

                for yazi in linkSource.find_all('td'):
                    if kelime.lower() in yazi.text.lower():
                        if kelimeFrekansi == True and inboundLink == True:
                            a += 1
                            resultLink.append(kelime.upper()+' ifadesi '+i.text+' -> '+str(newlink)+' '+str(a)+' kez bulundu!')
                        elif kelimeFrekansi == True and inboundLink == False:
                            a += 1
                            resultLink.append(kelime.upper()+' ifadesi '+i.text+' -> '+str(a)+' kez bulundu!')
                        elif kelimeFrekansi == False and inboundLink == True:
                            resultLink.append(kelime.upper()+' ifadesi '+i.text+' -> '+str(newlink))
        resultLink = list(set(resultLink))
        return resultLink
