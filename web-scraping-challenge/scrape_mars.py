# Dependencies and Setup
from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import time

#Site Navigation
executable_path = {'executable_path': '/Users/zanek/Downloads/chromedriver.exe'}
browser = Browser("chrome", **executable_path, headless=False)


# NASA Mars News
def mars_news(browser):
    # Visit the NASA Mars News Site
    # Open browser to NASA Mars News Site
        browser.visit('https://mars.nasa.gov/news/')

    # Search for news titles
    title_results = soup.find_all('div', class_='content_title')

    # Search for paragraph text under news titles
    p_results = soup.find_all('div', class_='article_teaser_body')

    # Extract first title and paragraph, and assign to variables
    news_title = title_results[0].text
    news_p = p_results[0].text
    return news_title, news_p

# JPL Mars Space Images - Featured Image
def featured_image(browser):
    # Open browser to JPL Featured Image
    browser.visit('https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars')

    # Click through to find full image
    browser.click_link_by_partial_text('FULL IMAGE')

    # Click again for full large image
    html = browser.html
    soup = bs(html, 'html.parser')

    # Search for image source
    results = soup.find_all('figure', class_='lede')
    relative_img_path = results[0].a['href']
    featured_img = 'https://www.jpl.nasa.gov' + relative_img_path
    return featured_img


# Mars Facts
def mars_facts():
    # Visit the Mars Facts Site Using Pandas to Read and use Pandas to scrape data
    tables = pd.read_html('https://space-facts.com/mars/')

    #Take second table for Mars facts
    df = tables[0]

    # Rename columns and set index
    df.columns=['Description', 'Value']
    return df.to_html(classes="table table-striped")

# Mars Hemispheres
def hemisphere(browser):
    # Open browser to USGS Astrogeology site
    browser.visit('https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars')


    html = browser.html
    soup = bs(html, 'html.parser')

    hemi_names = []

    # Search for the names of all four hemispheres
    results = soup.find_all('div', class_="collapsible results")
    hemispheres = results[0].find_all('h3')

    # Get text and store in list
    for name in hemispheres:
        hemi_names.append(name.text)

    # Search for thumbnail links
    thumbnail_results = results[0].find_all('a')
    thumbnail_links = []

    for thumbnail in thumbnail_results:
    
        # If the thumbnail element has an image...
        if (thumbnail.img):
        
            # then grab the attached link
            thumbnail_url = 'https://astrogeology.usgs.gov/' + thumbnail['href']
        
            # Append list with links
            thumbnail_links.append(thumbnail_url)

    full_imgs = []

    for url in thumbnail_links:
    
        # Click through each thumbanil link
        browser.visit(url)
    
        html = browser.html
        soup = bs(html, 'html.parser')
    
        # Scrape each page for the relative image path
        results = soup.find_all('img', class_='wide-image')
        relative_img_path = results[0]['src']
    
        # Combine the reltaive image path to get the full url
        img_link = 'https://astrogeology.usgs.gov/' + relative_img_path
    
        # Add full image links to a list
        full_imgs.append(img_link)

    # Zip together the list of hemisphere names and hemisphere image links
    mars_hemi_zip = zip(hemi_names, full_imgs)

    hemisphere_image_urls = []

    # Iterate through the zipped object
    for title, img in mars_hemi_zip:
    
        mars_hemi_dict = {}
    
        # Add hemisphere title to dictionary
        mars_hemi_dict['title'] = title
    
        # Add image url to dictionary
        mars_hemi_dict['img_url'] = img
    
        # Append the list with dictionaries
        hemisphere_image_urls.append(mars_hemi_dict)

    return hemisphere_image_urls


# Main Web Scraping Bot
def scrape_all():
    executable_path = {"executable_path": "/Users/zanek/Downloads/chromedriver.exe"}
    browser = Browser("chrome", **executable_path, headless=False)
    news_title, news_paragraph = mars_news(browser)
    img_url = featured_image(browser)
    facts = mars_facts()
    hemisphere_image_urls = hemisphere(browser)
    timestamp = dt.datetime.now()

    data = {
        "news_title": news_title,
        "news_paragraph": news_p,
        "featured_image": img_url,
        "weather": mars_weather,
        "facts": facts,
        "hemispheres": hemisphere_image_urls,
        "last_modified": timestamp
    }
    browser.quit()
    return data 

if __name__ == "__main__":
    print(scrape_all())