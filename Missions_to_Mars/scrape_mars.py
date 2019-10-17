#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from bs4 import BeautifulSoup
import requests
from splinter import Browser

def scrape():
    # In[2]:


    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"


    # In[3]:


    executable_path = {'executable_path': './chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)


    # In[4]:


    browser.visit(url)


    # In[5]:


    for x in range(1,2):
        html = browser.html
        soup = BeautifulSoup(html,'html.parser')
        
        titles = soup.find_all('div',class_ = "content_title")
        text = soup.find_all('div',class_ = "article_teaser_body")
        headlines = []
        teasers = []
        for i in range(len(titles)):
            headlines.append(titles[i].text)
            latest_headline = headlines[0]
        for j in range(len(text)):
            teasers.append(text[j].text)
            latest_text = teasers[0]
    #  

    # In[6]:


    url_2 = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"


    # In[7]:


    browser.visit(url_2)


    # In[22]:


    for x in range(1,2):
        html = browser.html
        soup = BeautifulSoup(html,'html.parser')
        
        featured_img = soup.find_all('article',class_ = "carousel_item")[0]['style']
        
    #     featured_img_url = url_2 + featured_img
        featured_img_path = featured_img[23:75]
        featured_img_url = "https://www.jpl.nasa.gov" + featured_img_path
        print(featured_img_url)
        
    
    # In[23]:


    url_3 = "https://twitter.com/marswxreport?lang=en"


    # In[24]:


    browser.visit(url_3)


    # In[38]:


    for x in range(1,2):
        html = browser.html
        soup = BeautifulSoup(html,'html.parser')
        
        mars_weather = soup.find_all('p',class_ = "TweetTextSize")[0].text
        
        print(mars_weather)

     
    # In[39]:


    url_4 = "https://space-facts.com/mars/"


    # In[41]:


    mars_facts_tables = pd.read_html(url_4)[1]
    table = mars_facts_tables.set_index(0)
    table.columns = [''] * len(table.columns)
    table
    html_table = table.to_html()
    html_table

    # In[42]:


    url_5 = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"


    # In[43]:


    browser.visit(url_5)


    # In[62]:


    titles = ["Cerberus","Schiaparelli","Syrtis Major","Valles Marineris"]
    hemi_img = []
    for tit in titles:
        browser.click_link_by_partial_text(tit)
        html = browser.html
        soup = BeautifulSoup(html,'html.parser')
        hemi_img.append(soup.find_all("div", class_="downloads")[0].find_all("a")[0]["href"])
        browser.back()

    print(hemi_img)

     

    # In[ ]:

    mars_data = {
        "news_title" : latest_headline,
        "news_p" : latest_text,
        "featured_image" : featured_img_url,
        "mars_weather": mars_weather,
        "mars_facts_table": html_table,
        "hemi_names": titles,
        "hemi_img_url": hemi_img
    }
    
    
    print(mars_data)
    return mars_data

    browser.quit()

if __name__ == "__main__":
    print(scrape())

#%%

#%%
