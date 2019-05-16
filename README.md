

```python
import pandas as pd
import urllib.request
from collections import Counter
from insta_scrape import recent_25_posts, insta_details
```

### Corgis of Instagram!
For a fun scraping project, I decided to pull the most recent posts from a bunch of prominent Corgis of Instagram to see their comparative performance and some of the hastags they used to help promote their posts. 

#### The functions being used do the following:
* recent_10_posts: scrapes the most recent 10 Instagram posts and grabs their urls
* links_to_details: takes the list of links and returns a list of dictionaries with details for each post, including:
    - age - when posted
    - comment - initial comment from poster
    - likes/views - count of likes or views for photo or video
    - link - the original link of the post

#### Sneakers (135k followers)


```python
sneakers_urls = recent_25_posts('sneakersthecorgi')
```


```python
print(sneakers_urls)
```

    ['https://www.instagram.com/p/BxY3nKoHKbV/', 'https://www.instagram.com/p/BxC7C0hhbFz/', 'https://www.instagram.com/p/Bw9uXwCh8KG/', 'https://www.instagram.com/p/Bw2EuhcBMQN/', 'https://www.instagram.com/p/Bwkj9-AhZqp/', 'https://www.instagram.com/p/Bwh-lzQB_T7/', 'https://www.instagram.com/p/BwddyHrBsM2/', 'https://www.instagram.com/p/BwV3f2UhVkf/', 'https://www.instagram.com/p/BwNyX_chT7L/', 'https://www.instagram.com/p/BwLLNjhh1Y7/', 'https://www.instagram.com/p/BwIzjUzBzXL/', 'https://www.instagram.com/p/BwF8r-Uhtvi/', 'https://www.instagram.com/p/BwDkrWehN6J/', 'https://www.instagram.com/p/Bv-oUTiBfTE/', 'https://www.instagram.com/p/Bv72GgfBB3M/', 'https://www.instagram.com/p/Bv2lW1_BYje/', 'https://www.instagram.com/p/Bvz8ZgMBokH/', 'https://www.instagram.com/p/BvxjvP4gOS_/', 'https://www.instagram.com/p/BvuIBdlhsYA/', 'https://www.instagram.com/p/BvryFSbB3fh/', 'https://www.instagram.com/p/Bvm_7KLhhVA/', 'https://www.instagram.com/p/Bvh6O-LhRKJ/', 'https://www.instagram.com/p/BvfNb8rBS8-/', 'https://www.instagram.com/p/Bvc_iYoBj5t/', 'https://www.instagram.com/p/BvaVEdYhPWL/']



```python
sneakers_post_info = insta_details(sneakers_urls)
```


```python
sneakers = pd.DataFrame(sneakers_post_info)
sneakers['hashtags'] = sneakers['comment'].apply(lambda x: find_hashtags(x))
```


```python
sneakers.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>age</th>
      <th>comment</th>
      <th>likes/views</th>
      <th>link</th>
      <th>hashtags</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1 DAY AGO</td>
      <td>sneakersthecorgi\nYou could give your mom frag...</td>
      <td>3,074 likes</td>
      <td>https://www.instagram.com/p/BxY3nKoHKbV/</td>
      <td>[#HappyMothersDay]</td>
    </tr>
    <tr>
      <th>1</th>
      <td>MAY 4</td>
      <td>sneakersthecorgi\nMay you chew your toys with ...</td>
      <td>2,438 likes</td>
      <td>https://www.instagram.com/p/BxC7C0hhbFz/</td>
      <td>[#MayThe, #sneakersthecorgi]</td>
    </tr>
    <tr>
      <th>2</th>
      <td>MAY 2</td>
      <td>sneakersthecorgi\nCaption this photo.\n#sneake...</td>
      <td>4,452 likes</td>
      <td>https://www.instagram.com/p/Bw9uXwCh8KG/</td>
      <td>[#sneakersthecorgi]</td>
    </tr>
    <tr>
      <th>3</th>
      <td>APRIL 29</td>
      <td>sneakersthecorgi\nI hereby declare that Monday...</td>
      <td>4,096 likes</td>
      <td>https://www.instagram.com/p/Bw2EuhcBMQN/</td>
      <td>[#sneakersthecorgi]</td>
    </tr>
    <tr>
      <th>4</th>
      <td>APRIL 22</td>
      <td>sneakersthecorgi\nSTILL my favorite planet. 🌎 ...</td>
      <td>2,045 likes</td>
      <td>https://www.instagram.com/p/Bwkj9-AhZqp/</td>
      <td>[#HappyEarthDay, #sneakersthecorgi]</td>
    </tr>
  </tbody>
</table>
</div>



#### Ralph the Corgi (315k followers)


```python
ralph_urls = recent_25_posts('ralphthecorgi')
```


```python
ralph_post_info = insta_details(ralph_urls)
```


```python
ralph = pd.DataFrame(ralph_post_info)
ralph['hashtags'] = ralph['comment'].apply(lambda x: find_hashtags(x))
ralph.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>age</th>
      <th>comment</th>
      <th>likes/views</th>
      <th>link</th>
      <th>hashtags</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1 DAY AGO</td>
      <td>ralphthecorgi\nI heard that moms LOVE spa trea...</td>
      <td>11,890 likes</td>
      <td>https://www.instagram.com/p/BxYTUpoAFST/</td>
      <td>[#NothingLikeAGoodTasteBudExfoliation, #Always...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4 DAYS AGO</td>
      <td>ralphthecorgi\nWARNING: if you look too deeply...</td>
      <td>14,085 likes</td>
      <td>https://www.instagram.com/p/BxQj4jWgTAC/</td>
      <td>[#CantSayIDidntWarnYa, #TakeoverByGeorge, #Gor...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>MAY 5</td>
      <td>ralphthecorgi\nThat time I drank Georgie’s bee...</td>
      <td>11,985 likes</td>
      <td>https://www.instagram.com/p/BxF_w57AtOX/</td>
      <td>[#CorgoDeMayo, #OldieButAGoodie, #RalphandGeorge]</td>
    </tr>
    <tr>
      <th>3</th>
      <td>MAY 3</td>
      <td>ralphthecorgi\n[Tap for Sound] We were born fo...</td>
      <td>17,514 views</td>
      <td>https://www.instagram.com/p/BxARXIwAe16/</td>
      <td>[#LeftCheekRightCheek, #RalphandGeorge]</td>
    </tr>
    <tr>
      <th>4</th>
      <td>APRIL 30</td>
      <td>ralphthecorgi\nGeorge be like: I find a loaf, ...</td>
      <td>6,954 likes</td>
      <td>https://www.instagram.com/p/Bw4rYNTAU2k/</td>
      <td>[#TakeoverByGeorge, #GorgeousGeorge, #Ralphand...</td>
    </tr>
  </tbody>
</table>
</div>



#### Geordi La Corgi (393k followers)


```python
lacorgi_urls = recent_25_posts('lacorgi')
```


```python
lacorgi_post_info = insta_details(lacorgi_urls)
```


```python
lacorgi = pd.DataFrame(lacorgi_post_info)
lacorgi['hashtags'] = lacorgi['comment'].apply(lambda x: find_hashtags(x))
lacorgi.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>age</th>
      <th>comment</th>
      <th>likes/views</th>
      <th>link</th>
      <th>hashtags</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1 HOUR AGO</td>
      <td>lacorgi\nGeordi rates our new bed a solid 💯⁣⁣\...</td>
      <td>6,924 likes</td>
      <td>https://www.instagram.com/p/BxczbKag_kX/</td>
      <td>[#avocadomattress]</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4 DAYS AGO</td>
      <td>lacorgi\nHe stood like this for almost 2 whole...</td>
      <td>13,443 likes</td>
      <td>https://www.instagram.com/p/BxSSReLg3ox/</td>
      <td>[#corgilife]</td>
    </tr>
    <tr>
      <th>2</th>
      <td>7 DAYS AGO</td>
      <td>lacorgi\nThe golden corgi ratio: ears &amp; stumps...</td>
      <td>16,150 likes</td>
      <td>https://www.instagram.com/p/BxJIFKGAO7s/</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>3</th>
      <td>MAY 2</td>
      <td>lacorgi\nTaking name suggestions for our new k...</td>
      <td>16,102 likes</td>
      <td>https://www.instagram.com/p/Bw94Nz4Bibk/</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>4</th>
      <td>APRIL 30</td>
      <td>lacorgi\nHappy National Bubble Tea Day!\nEnjoy...</td>
      <td>9,487 likes</td>
      <td>https://www.instagram.com/p/Bw5GYlYggp4/</td>
      <td>[]</td>
    </tr>
  </tbody>
</table>
</div>



#### Tibby (242k followers)


```python
tibby_urls = recent_25_posts('tibbythecorgi')
```


```python
tibby_post_info = insta_details(tibby_urls)  
```


```python
tibby = pd.DataFrame(tibby_post_info)
tibby['hashtags'] = tibby['comment'].apply(lambda x: find_hashtags(x))
tibby.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>age</th>
      <th>comment</th>
      <th>likes/views</th>
      <th>link</th>
      <th>hashtags</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2 DAYS AGO</td>
      <td>tibbythecorgi\nMe When I See Free Samples 😲😲 #...</td>
      <td>21,327 views</td>
      <td>https://www.instagram.com/p/BxVkb9jHSGE/</td>
      <td>[#WouldYouLikeToTryASampleOfThis, #FurkIDontCa...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6 DAYS AGO</td>
      <td>tibbythecorgi\nIt’s Exhausting Being This Furb...</td>
      <td>8,741 likes</td>
      <td>https://www.instagram.com/p/BxLhuHPHYjI/</td>
      <td>[#SheNeedsHerBootyIMeanBeautyRest, #LookAtHerL...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>MAY 5</td>
      <td>tibbythecorgi\nTibby Doing Her Best Drogon Imp...</td>
      <td>9,731 likes</td>
      <td>https://www.instagram.com/p/BxGhGLzHpNT/</td>
      <td>[#ThatIsOneDerpyDragon, #GoT, #ThatThirdPhotoK...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>MAY 3</td>
      <td>tibbythecorgi\nMe Waiting For The Clock To Hit...</td>
      <td>11,296 likes</td>
      <td>https://www.instagram.com/p/BxAvfApHf-9/</td>
      <td>[#SorryICantDoThatPowerpoint, #ImBusyAlready, ...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>MAY 2</td>
      <td>tibbythecorgi\nCan’t Say No To This Puppy Face...</td>
      <td>6,245 likes</td>
      <td>https://www.instagram.com/p/Bw-8B8On2iq/</td>
      <td>[#LookAtHer, #ABallOfSassFromTheBeginning, #TBT]</td>
    </tr>
  </tbody>
</table>
</div>



#### Winston, The White Corgi (232k followers)


```python
winston_urls = recent_25_posts('winstonthewhitecorgi')
```


```python
winston_post_info = insta_details(winston_urls)
```


```python
winston = pd.DataFrame(winston_post_info)
winston['hashtags'] = winston['comment'].apply(lambda x: find_hashtags(x))
winston.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>age</th>
      <th>comment</th>
      <th>likes/views</th>
      <th>link</th>
      <th>hashtags</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1 DAY AGO</td>
      <td>winstonthewhitecorgi\nGrandmas came to visit N...</td>
      <td>12,277 likes</td>
      <td>https://www.instagram.com/p/BxYB8rZH-WR/</td>
      <td>[#MothersDay, #HappyMothersDay]</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5 DAYS AGO</td>
      <td>winstonthewhitecorgi\n🔈CORGI B #winstonsroadto...</td>
      <td>34,972 views</td>
      <td>https://www.instagram.com/p/BxOLD2enM-h/</td>
      <td>[#winstonsroadtofetch]</td>
    </tr>
    <tr>
      <th>2</th>
      <td>MAY 4</td>
      <td>winstonthewhitecorgi\nHappy #May4th from your ...</td>
      <td>30,025 views</td>
      <td>https://www.instagram.com/p/BxCwBIsnyTi/</td>
      <td>[#May, #maythe, #starwars]</td>
    </tr>
    <tr>
      <th>3</th>
      <td>MAY 3</td>
      <td>winstonthewhitecorgi\n🎥🍿😴 #friyay</td>
      <td>6,813 likes</td>
      <td>https://www.instagram.com/p/BxBfdXbHE_H/</td>
      <td>[#friyay]</td>
    </tr>
    <tr>
      <th>4</th>
      <td>APRIL 30</td>
      <td>winstonthewhitecorgi\nAre you scrolling throug...</td>
      <td>8,890 likes</td>
      <td>https://www.instagram.com/p/Bw5nHdinPfw/</td>
      <td>[#MothersDay, #venusetfleur]</td>
    </tr>
  </tbody>
</table>
</div>



### Looking at all hashtags across corgis:


```python
def all_hashtags(col):
    all_h = []
    for sublist in col:
        for item in sublist:
            all_h.append(item)
    return all_h
```


```python
all_corgi_hastags = all_hashtags(sneakers['hashtags']) + all_hashtags(ralph['hashtags']) + \
                        all_hashtags(lacorgi['hashtags']) + all_hashtags(winston['hashtags']) + all_hashtags(tibby['hashtags'])

hashtag_values = dict(Counter(all_corgi_hastags))
for k,v in hashtag_values.items():
    if v > 5:
        print(k + ": " + str(v))
```

    #sneakersthecorgi: 24
    #shopsneakersthecorgi: 6
    #TakeoverByGeorge: 6
    #RalphandGeorge: 10
    #winstonsroadtofetch: 10


Temporarily saving to CSV:


```python
sneakers.to_csv('csv/sneakers.csv')
lacorgi.to_csv('csv/lacorgi.csv')
ralph.to_csv('csv/ralph.csv')
tibby.to_csv('csv/tibby.csv')
winston.to_csv('csv/winston.csv')
```

### Bonus: How to extract the photo:


```python
browser = Chrome()
corg = browser.get(sneakers_urls[1])
img = '//*[@id="react-root"]/section/main/div/div/article/div[1]/div/div/div[1]/div[1]/img'
# The srcset attribut contains 3 different links of different sizes, the firth being 640w
image_1 = browser.find_element_by_xpath(img).get_attribute('srcset').split(' ')[0]
# Exporting the photo:
#urllib.request.urlretrieve(image_1, "sneakers_1.jpg")
```




    ('sneakers_1.jpg', <http.client.HTTPMessage at 0x1045b4390>)



