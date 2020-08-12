### Corgis of Instagram!

A fun scraping project to see the recent posts from a bunch of prominent Corgis of Instagram to see their comparative performance and some of the hastags and mentions they use to help promote their posts. You can read more about the process from my related blog post [Tutorial: Web scraping Instagram’s most precious resource — corgis.](https://medium.com/swlh/tutorial-web-scraping-instagrams-most-precious-resource-corgis-235bf0389b0c)

#### The functions being used do the following:

- recent_post_links: scrapes the most recent Instagram posts and grabs their urls (can set any number)
- insta_link_details: takes a post url and returns a dictionary with post details, including:
  - link - original url link
  - type - whether it is a photo or video
  - likes/views - count of likes or views for photo or video
  - age - when posted
  - comment - initial comment from poster
  - hashtags - hashtags extracted from comment, via regular expression
  - mentions - mentions extracted from comment, via regular expression

### Bonus: How to extract the photo:

- insta_url_to_img: gets photo from post url. Note: does not currently work with posts that have multiple images, only grabs the first, and does not work with videos.

### Quick Start
This works to make a csv file with all of the from insta_scrape.py. 
Installation: Clone this repo and cd into it. Make sure geckodriver the Firefox Selenium Driver is executable in project path.
Edit the make.py file with your desired username. 
Then run `python3 make.py` to compile your CSV. 
