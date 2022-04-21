from internet import Internet, get, BeautifulSoup, post


#!status
"""
Scatter Attributes: 
    self.
        __ScatterSoup
        __ScatterResHead 
        __ScatterSession
        __ScatterCSRF
        
"""  

class ScatterSecrets(Internet):
    
    def __init__(self):
        self.__GetContent()
        self.__GetCookie()
        self.__GetCSRF()


    def __GetContent(self):
        res = get('https://scatteredsecrets.com/')
        self.__ScatterSoup = BeautifulSoup(res.content, 'html.parser')
        self.__ScatterResHead = res.headers
        
    def __GetCookie(self):
        self.__Session = self.__ScatterResHead['set-cookie'].split(';')[0].split('=')[1]
        
    def __GetCSRF(self):
        # tag = self.__ScatterSoup.find('input', {'type': 'hidden', 'name': 'csrf_token'})
        # self.__ScatterCSRF = tag.attrs['value']
        self.__CSRFToken = self.__ScatterSoup.find('input', {'type': 'hidden', 'name': 'csrf_token'}).attrs['value']

        
    def Search(self):
        self.AddStatus('[+] ')
        InputHeaders = {
            "Host": "scatteredsecrets.com",
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0",
            "Cookie": f"session={self.__Session}",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate",
            "Referer": "https://scatteredsecrets.com/",
            "Content-Type": "application/x-www-form-urlencoded",
            "Origin": "https://scatteredsecrets.com",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-User": "?1",
            "Te": "trailers"
        }

        Parameters = {"identifier" : self.GetSearchKey,
                    "csrf_token" : self.__CSRFToken,
                    "action" : "search"
                    }
        self.AddResult(''.join(BeautifulSoup(post('https://scatteredsecrets.com/', headers=InputHeaders, data=Parameters).content, 'html.parser').find('small', {'class': 'alerter'}).contents))
