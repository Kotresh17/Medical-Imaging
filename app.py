import requests
import tldextract
import urllib2
import time
from bs4 import BeautifulSoup
from pprint import pprint
import os
import imgkit
import cookielib




def main(page_url):
    extracted = tldextract.extract(page_url)
    folder_name  = "./"+ extracted.domain + "." + extracted.suffix
    css_folder = folder_name + "/css"
    screenshot_folder = folder_name + "/screenshot"

    # # create the directories to store the files
    # # check if the path does not exist before 
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
        os.mkdir(css_folder)
        os.mkdir(screenshot_folder)

    print("Created Folders for : ", page_url)

    # #make screenshot of the webapge
    imgkit.from_url(page_url, screenshot_folder + "/" + extracted.domain + ".jpg")
    print("Done making screenshot for : " + page_url)

    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}

    req = urllib2.Request(page_url, headers=hdr)

    page_contents = urllib2.urlopen(req)
    page = urllib2.urlopen(req)
    soup = BeautifulSoup(page, 'html.parser')
    links = soup.find_all('link', href=True)

    with open(folder_name + "/index.html", "w+") as f:
        f.write(page_contents.read())
        print("Done Writing the HTML file")

    for url in links : 
        correct_url = url['href']
        filename = url['href'].split('/')[-1].split('.')[0]
        file_ext = url['href'].split('.')[-1]
        if(filename != '' and file_ext == 'css'):
            try:
                req = urllib2.Request(url['href'], headers=hdr)
                content = urllib2.urlopen(req)
                output_filename = css_folder + "/" + filename + "." + file_ext
                with open(output_filename, "w+") as f:
                    f.write(content.read())
                print("Done Writing CSS file : ", output_filename)
            except ValueError as e:
                pass
    print("Tasks Accomplished for : ", page_url)

#run the script against multiple url 

input_file = "url.txt"
urls = open(input_file).readlines()
for address in urls : 
   print("Address : ", address)
   main(address)