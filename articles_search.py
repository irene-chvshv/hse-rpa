### https://github.com/MazarsLabs/hse-rpa

import os
import re
import requests
import sys
import pandas as pd
from pprint import pprint
from selenium.webdriver.chrome.options import Options
import selenium.webdriver as webdriver
import time
from email.message import EmailMessage
import smtplib
from conf import query, num_page, receiver, login, password

query_link = f"https://www.semanticscholar.org/search?q={query}&sort=relevance&page="

# working paths
working_dir = os.path.dirname(os.path.realpath(__file__))
folder_for_pdf = os.path.join(working_dir, "articles")
webdriver_path = "/usr/local/bin/chromedriver"   # proper version https://chromedriver.chromium.org/

# chek if articles directory is exist and create if not
if not os.path.isdir(folder_for_pdf):
    os.mkdir(folder_for_pdf)

# webdriver
chrome_options = Options()
chrome_options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
prefs = {"download.default_directory": folder_for_pdf, "download.prompt_for_download": False}
chrome_options.add_experimental_option('prefs', prefs)
os.environ["webdriver.chrome.driver"] = webdriver_path   # 'webdriver' executable needs to be in PATH. Please see https://sites.google.com/a/chromium.org/chromedriver/home

links_list = [query_link + str(page+1) for page in range(num_page)]   # create links to follow

driver = webdriver.Chrome(executable_path=webdriver_path, options=chrome_options)

final_info = []   # empty dictionary for articles info
paper_index = 0
for search_link in links_list:
    # get all links to articles from the page
    driver.get(search_link)
    time.sleep(5)
    
    articles_links = []
    for article in driver.find_elements_by_css_selector("a[data-selenium-selector='title-link']"):
        try:
            link = article.get_attribute("href")
            print(link)
            articles_links.append(link)
        except:
            pass

    for link in articles_links:
        driver.get(link)

        title = driver.find_element_by_css_selector("h1[data-selenium-selector='paper-detail-title']").text

        author_list = driver.find_element_by_css_selector("span.author-list").text

        elems = driver.find_elements_by_css_selector("span[data-heap-id='paper-meta-journal']")
        source = elems[0].text if elems else ''

        description = driver.find_element_by_css_selector("meta[name='description']").get_attribute('content')

        elems = driver.find_elements_by_css_selector("a[data-heap-nav='citing-papers']")
        if elems:
            n_citations = re.search('^(\d+)', elems[0].text).group(1)
        else:
            n_citations = '0'

        paper_index += 1
        tmp_info = {
            'title': title,
            'author_list': author_list,
            'source': source,
            'description': description,
            'n_citations': n_citations,
        }
        print(f'[+] Received info about paper "{title}"')

        try:
            url = driver.find_element_by_css_selector("a[data-selenium-selector='paper-link']").get_attribute("href")
            r = requests.get(url)
            r.raise_for_status()
            if 'application/pdf' not in r.headers.get('content-type'):
                raise ValueError('Not a pdf')

            full_path = os.path.join(folder_for_pdf, 'paper{}.pdf'.format(paper_index))
            with open(full_path, 'wb') as f:
                f.write(r.content)
            print(f'    Saved to "{full_path}"')
        except Exception:
            full_path = ''

        tmp_info.update({'path_to_file':full_path})

        final_info.append(tmp_info.copy())
        time.sleep(2)

driver.quit()

# write all info to excel
df = pd.DataFrame(final_info)
excel_path = os.path.join(working_dir, "data.xlsx")
df.to_excel(excel_path, index=False)

# create email
mail = EmailMessage()
mail['From'] = login
mail['To'] = receiver
mail['Subject'] = "Topics analysis"
mail.set_content("Hi!\n\nFind attached excel file with articles info.\n\nRegard,")

# add attachment
with open(excel_path, 'rb') as f:
    file_data = f.read()
    file_name = f'articles_info.xlsx'
mail.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

for item in final_info:
    file_name = item['path_to_file']
    if file_name:
        with open(file_name, 'rb') as f:
            file_data = f.read()
        mail.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

# send email
server = smtplib.SMTP('smtp.office365.com')  
server.starttls()  
server.login(login, password)    
server.send_message(mail)      
server.quit()      


    # ┏━┓┏━┓┏━━━┓┏━━━━┓┏━━━┓┏━━━┓┏━━━┓  
    # ┃ ┗┛ ┃┃┏━┓┃┗━━┓ ┃┃┏━┓┃┃┏━┓┃┃┏━┓┃  
    # ┃┏┓┏┓┃┃┃ ┃┃  ┏┛┏┛┃┃ ┃┃┃┗━┛┃┃┗━━┓  
    # ┃┃┃┃┃┃┃┗━┛┃ ┏┛┏┛ ┃┗━┛┃┃┏┓┏┛┗━━┓┃  
    # ┃┃┃┃┃┃┃┏━┓┃┏┛ ┗━┓┃┏━┓┃┃┃┃┗┓┃┗━┛┃  
    # ┗┛┗┛┗┛┗┛ ┗┛┗━━━━┛┗┛ ┗┛┗┛┗━┛┗━━━┛  
