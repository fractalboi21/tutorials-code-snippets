import requests
from bs4 import BeautifulSoup
html = requests.get("https://pythonawesome.com/").content
soup = BeautifulSoup(html,"lxml")

#you find seo keywords from meta tags

#tags link script a  noscript nav head 
#href src
def get_links_from_tag_attribute(tag,attribute):
    script_tags = soup.find_all(tag)
    src_links = []
    for script_tag in script_tags:
      try:
        src = script_tag[attribute]
        src_links.append(src)
      except KeyError:
        pass
    return src_links

def is_abs_link(link):
    return link[0:4] == "http"

def split_link_types(links):
    abs_links = []
    rel_links = []
    for link in links:
        if is_abs_link(link):
            abs_links.append(link)
        else:
            rel_links.append(link)
            
    return abs_links, rel_links
            
