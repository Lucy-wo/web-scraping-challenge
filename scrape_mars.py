from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
from bs4 import BeautifulSoup
import requests
import os
import time

def init_browser():
   executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
   return Browser("chrome", **executable_path, headless=False)
       

def scrape():
    browser=init_browser()
    #----NASA Mars News
    url_news = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url_news)
    time.sleep(1)
    html_news = browser.html
    soup_news = BeautifulSoup(html_news, 'html.parser')
    results_title = soup_news.find_all('div',class_='content_title')[1]
    news_title=results_title.text.strip()
    news_p = soup_news.find('div', class_='article_teaser_body').text
    print(news_title)
    print(news_p)
    
    #----JPL Mars Space Images - Featured Image
    url_spaceimg = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url_spaceimg)
    time.sleep(1)
    html_spaceimg = browser.html
    soup_spaceimg = BeautifulSoup(html_spaceimg, 'html.parser')
    results_img_spaceimg = soup_spaceimg.find_all('div',class_='img')[0].find('img')['src']
    results_img_spaceimg_1=results_img_spaceimg.split('/',)
    results_img_spaceimg_2=results_img_spaceimg_1[4].split('-',)
    featured_image_url='https://www.jpl.nasa.gov/'+results_img_spaceimg_1[1]+'/'+results_img_spaceimg_1[2]+'/largesize/'+results_img_spaceimg_2[0]+'_hires.jpg'
    print(featured_image_url)
   
    #----Mars Weather
    url_weather = 'https://twitter.com/marswxreport?lang=en'
    response_weather = requests.get(url_weather)
    weather_soup = BeautifulSoup(response_weather.text, 'html.parser')
    mars_weather_tweet = weather_soup.find_all('div', class_ = "js-tweet-text-container")[0].find('p').text
    mars_weather=mars_weather_tweet.replace('\n','').split('pic.twitter.com/',)[0]
    print(mars_weather)
   
    #----Mars Facts
    import pandas as pd
    url_facts = 'https://space-facts.com/mars/'
    tables = pd.read_html(url_facts)
    mars_table=tables[0]
    mars_table.columns=['description','value']
    mars_table.set_index('description',inplace=True)
    html_table = mars_table.to_html()
    #html_table.replace('\n', '')
    #mars_table.to_html('mars_table.html')
    
    #----Mars Hemispheres
    url_cerberus = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    browser.visit(url_cerberus)
    time.sleep(1)
    html_cer = browser.html
    soup_cerberus = BeautifulSoup(html_cer, 'html.parser')
    results_cerberus = soup_cerberus.find('img',class_='wide-image')['src']
    link__cerberus='https://astrogeology.usgs.gov/'+results_cerberus
    title_cerberus=soup_cerberus.find('h2',class_='title').text
  

    url_schiaparelli = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
    browser.visit(url_schiaparelli)
    time.sleep(1)
    html_schiaparelli = browser.html
    soup_schiaparelli = BeautifulSoup(html_schiaparelli, 'html.parser')
    results_schiaparelli = soup_schiaparelli.find('img',class_='wide-image')['src']
    link__schiaparelli='https://astrogeology.usgs.gov/'+results_schiaparelli
    title_schiaparelli=soup_schiaparelli.find('h2',class_='title').text

    url_syrtis = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    browser.visit(url_syrtis)
    time.sleep(1)
    html_syrtis = browser.html
    soup_syrtis = BeautifulSoup(html_syrtis, 'html.parser')
    results_syrtis = soup_syrtis.find('img',class_='wide-image')['src']
    link__syrtis='https://astrogeology.usgs.gov/'+results_syrtis
    title_syrtis=soup_syrtis.find('h2',class_='title').text

    url_valles = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
    browser.visit(url_valles)
    time.sleep(1)
    html_valles = browser.html
    soup_valles = BeautifulSoup(html_valles, 'html.parser')
    results_valles = soup_valles.find('img',class_='wide-image')['src']
    link__valles='https://astrogeology.usgs.gov/'+results_valles
    title_valles=soup_valles.find('h2',class_='title').text

    hemisphere_image_urls = [
    {"title": title_valles, "img_url": link__valles},
    {"title": title_cerberus, "img_url": link__cerberus},
    {"title": title_schiaparelli, "img_url": link__schiaparelli},
    {"title": title_syrtis, "img_url": link__syrtis}
    ]
    print(hemisphere_image_urls)
    listings = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url":featured_image_url,
        "mars_weather":mars_weather,
        "mars_table": html_table,
        "hemisphere_image_urls":hemisphere_image_urls
    }
    return listings
    
    

    


    
   



