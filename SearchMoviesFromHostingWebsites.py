import urllib
import mechanize
from bs4 import BeautifulSoup
import re

def getgooglelinks(link):
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.addheaders=[('User-agent','chrome')]

    term = link.replace(" ","+")
    query ="https://www.google.be/search?&q="+term
    htmltext = br.open(query).read()
 
    soup = BeautifulSoup(htmltext)
 
    search = soup.findAll('div',attrs={'id':'search'})
   
    searchtext = str(search[0])
    sopu1 = BeautifulSoup(searchtext)
    List_items= sopu1.findAll('li')
    
    regex = "q(?!.*q).*?&amp"
    
    pattern = re.compile(regex)
    results_array = []
    for li in List_items:
        soup2 = BeautifulSoup(str(li))
        links = soup2.findAll('a')
      
        source_link = links[0]
        source_url = re.findall(pattern,str(source_link))
        delimiters = 'a href="/url?q=', '&amp'
        
       
        if len(source_url)>0:
            re.split(r'(a|href="/url?q|&amp)', source_url[0])
            
            results_array.append(str(source_url[0].replace("q=","").replace("&amp","")))
            
    return results_array



#li = open("C:\Users\Obaid92\Desktop\engine\movieslinks.txt","a+")

array =  getgooglelinks("Guardians of the Galaxy site:www.novamov.com")
#li.write("NovaMOvies\n")
for lis in array:
        if(lis.startswith( 'http' ))>0:
         print lis
        # li.write(lis+"\n")
#li.close()     
array =  getgooglelinks("Fast and ferious site:www.cloudy.ec")
#li.write("NovaMOvies\n")
for lis in array:
        if(lis.startswith( 'http' ))>0:
         print lis

