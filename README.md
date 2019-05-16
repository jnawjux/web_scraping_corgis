
### Corgis of Instagram!
For a fun scraping project, I decided to pull the most recent posts from a bunch of prominent Corgis of Instagram to see their comparative performance and some of the hastags they used to help promote their posts. 

#### The functions being used do the following:
* recent_10_posts: scrapes the most recent 10 Instagram posts and grabs their urls
* links_to_details: takes the list of links and returns a list of dictionaries with details for each post, including:
    - age - when posted
    - comment - initial comment from poster
    - likes/views - count of likes or views for photo or video
    - link - the original link of the post

### Bonus: How to extract the photo:

Function included in notebook to extract photos.
