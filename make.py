import pandas as pd
import urllib.request
from collections import Counter
from insta_scrape import recent_post_links, insta_link_details, insta_url_to_img
example_username_urls = recent_post_links('example_username', post_count=10)
print(example_username_urls)
example_username_details = [insta_link_details(url) for url in example_username_urls]
example_username = pd.DataFrame(example_username_details)
example_username.head()
example_username.to_csv('csv/example_username_11_01_19.csv')
