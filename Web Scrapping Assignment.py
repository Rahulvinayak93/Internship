#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests


# 1) Write a python program to display all the header tags from wikipedia.org

# In[3]:


page = requests.get ('https://en.wikipedia.org/wiki/Main_Page')
page


# In[5]:


soup = BeautifulSoup(page.content)
soup


# In[41]:


tags = ['h1','h2','h3','h4','h5','h6']

#for t in tags:
#    for i in soup.find_all(True):
#            print(i.name,'-',i.text)


#test = soup.find('h1')
#test

#print(test.name,'-',test.text)

for i in soup.find_all(tags):
    print(i.name,'-',i.text)


# 2) Write a python program to display IMDB’s Top rated 100 movies’ data (i.e. name, rating, year of release)
# and make data frame.
# 

# In[43]:


page = requests.get ('https://www.imdb.com/chart/top/?ref_=nv_mv_250')
page

soup = BeautifulSoup (page.content)
soup


# In[69]:


movie_details = soup.find_all('td',class_="titleColumn")


movie_list = [i.text.replace('\n','').replace(' ','').split('.')[1][:-6] for i in soup.find_all('td',class_="titleColumn")]
movie_list


# In[70]:


year = [i.text.replace('\n','').replace(' ','').split('.')[1][-6:] for i in soup.find_all('td',class_="titleColumn")]
year


# In[82]:


rating_details = soup.find('td',class_="ratingColumn")

rating_list = []

for i in soup.find_all('td',class_="ratingColumn"):
    if i.text.replace('\n\n\n\n\xa012345678910 \n\n\n\nNOT YET RELEASED\n \n\nSeen\n\n\n','') == "":
        continue
    rating_list.append(i.text.replace('\n',''))
    
rating_list


# In[84]:


import pandas as pd
data_IMDB_100 = {'movie':movie_list[:100],'Year_of_release':year[:100],'rating':rating_list[:100]}

#data_IMDB_100

DF_data_IMDB_100 = pd.DataFrame(data_IMDB_100, index = range(1,101))
DF_data_IMDB_100


# 3) Write a python program to display IMDB’s Top rated 100 Indian movies’ data (i.e. name, rating, year of
# release) and make data frame.

# In[86]:


page = requests.get('https://www.imdb.com/india/top-rated-indian-movies/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=461131e5-5af0-4e50-bee2-223fad1e00ca&pf_rd_r=SN0GVZ5TZCYZSM2M30WT&pf_rd_s=center-1&pf_rd_t=60601&pf_rd_i=india.toprated&ref_=fea_india_ss_toprated_india_tr_india250_sm')
page

soup  = BeautifulSoup(page.content)
soup


# In[87]:


movie_name = []

for i in soup.find_all('td',class_="titleColumn"):
    movie_name.append(i.a['title'])
    
movie_name = movie_name[0:100]


year = []
year = year[:100]

for i in soup.find_all('span',class_='secondaryInfo'):
    year.append(i.text[1:-1])
    
year = year[:100]

rating = []

for i in soup.find_all('td',class_='ratingColumn imdbRating'):
#   print(i)
    rating.append(i.text.replace('\n',''))
    
rating = rating[:100]


rank = list(range(100))


# In[88]:


top_100_indian_movie_list = {'rank':rank,'movie_name':movie_name,'year_of_release':year,'rating':rating}
top_100_indian_movie_list


# In[89]:


import pandas as pd

DF_top_100_indian_movie_list = pd.DataFrame(top_100_indian_movie_list)
DF_top_100_indian_movie_list


# In[90]:





# 4) Write a python program to scrape product name, price and discounts from https://meesho.com/bagsladies/pl/p7vbp .

# In[92]:


page = requests.get('https://meesho.com/bags-ladies/pl/p7vbp')
page

soup=BeautifulSoup(page.content)
soup


# In[94]:


title = soup.find_all('p',class_="Text__StyledText-sc-oo0kvp-0 cPgaBh NewProductCard__ProductTitle_Desktop-sc-j0e7tu-4 hofZGw NewProductCard__ProductTitle_Desktop-sc-j0e7tu-4 hofZGw")


product_name = [i.text for i in title]
product_name


# In[95]:


# price for 1 item

price = soup.find('div',class_="Card__BaseCard-sc-b3n78k-0 fVRkfg NewProductCard__PriceRow-sc-j0e7tu-5 dYYUrF NewProductCard__PriceRow-sc-j0e7tu-5 dYYUrF")
price


price_all = soup.find_all('div',class_="Card__BaseCard-sc-b3n78k-0 fVRkfg NewProductCard__PriceRow-sc-j0e7tu-5 dYYUrF NewProductCard__PriceRow-sc-j0e7tu-5 dYYUrF")

product_price = [i.text for i in price_all]
product_price


##sell_price = [i[1:4] for i in product_price]
##sell_price - this is method is not so good

##list_price = [*product_price, sep='₹']
##list_price

offer_price = [i.split('₹')[1] for i in product_price]
offer_price


discount = [i[-7:-4] for i in product_price]
discount

original_price = [i.split('₹')[2][:3] for i in product_price]
original_price


# In[96]:


# using sep in string to find the price

product_price

original_price = [i.split('₹')[2][:3] for i in product_price]
original_price


# In[97]:


import pandas as pd

product_list = {'product_name':product_name,'offer_price':offer_price,'discount':discount,'original_price':original_price}

product_data = pd.DataFrame(data = product_list, index = (range(1,21)))
product_data


# 5) Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape:
#     a) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.
#     b) Top 10 ODI Batsmen along with the records of their team and rating.
#     c) Top 10 ODI bowlers along with the records of their team and rating.

# a)

# In[100]:


page = requests.get('https://www.icc-cricket.com/rankings/mens/team-rankings/odi')
page

soup = BeautifulSoup(page.content)
soup


# In[101]:


teams = [i.text for i in soup.find_all('span',class_='u-hide-phablet')]
teams


# In[102]:


matches = soup.find('td',class_='rankings-block__banner--matches')
matches


# In[103]:


number_of_matches_1 = [i.text for i in soup.find_all('td',class_='rankings-block__banner--matches')]
number_of_matches_1


# In[104]:


number_of_matches_10= [i.text for i in soup.find_all('td',class_='table-body__cell u-center-text')]
number_of_matches_10


# In[105]:


matches_played = number_of_matches_1 + [number_of_matches_10[i] for i in range(0,len(number_of_matches_10),2)]
matches_played


# In[106]:


number_of_points_1 = [i.text for i in soup.find_all('td',class_='rankings-block__banner--points')]
number_of_points_1


# In[107]:


total_points= number_of_points_1 + [number_of_matches_10[i] for i in range(1,len(number_of_matches_10),2)]
total_points


# In[108]:


rating_1 = soup.find('td',class_='rankings-block__banner--rating u-text-right')
rating_1


# In[109]:


rating_10 = soup.find_all('td',class_='table-body__cell u-text-right rating')
rating_10

rating_top_10 = [i.text.split('\n                            ')[1] for i in soup.find_all('td',class_='rankings-block__banner--rating u-text-right')] + [i.text for i in rating_10]
rating_top_10


# In[110]:


men_cricket_data = {'team':teams[0:10],'matches':matches_played[0:10],'points':total_points[0:10],'rating':rating_top_10[0:10]}
men_cricket_data


# In[111]:


import pandas as pd

Mens_cricket_DF = pd.DataFrame(data = men_cricket_data, index = list(range(1,11)))
Mens_cricket_DF['Rank'] = list(range(1,11))

Mens_cricket_DF


# b)

# In[112]:


page2 = requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi')
page2

soup2 = BeautifulSoup(page2.content)


# In[113]:


first_player = soup2.find('div',class_='rankings-block__banner--name').text
first_player


# In[114]:


player_2_10 = [i.text.replace('\n','') for i in soup2.find_all('td',class_='table-body__cell name')]
player_2_10 = player_2_10[:9]
player_2_10


# In[115]:


player_list = [first_player] + [i for i in player_2_10]
player_list


# In[116]:


first_player_team = soup2.find('div',class_='rankings-block__banner--nationality').text.replace('\n','')[:3]
first_player_team


# In[117]:


player_team_2_10 = [i.text.replace('\n','')[:3] for i in soup2.find_all('span',class_='table-body__logo-text')]
player_team_2_10 = player_team_2_10[:9]

player_team_2_10 


# In[118]:



team_list = [first_player_team] + [i for i in player_team_2_10 ]
team_list


# In[119]:


first_player_rating = soup2.find('div',class_='rankings-block__banner--rating').text
first_player_rating


# In[120]:


player_rating_2_10 = [i.text for i in soup2.find_all('td',class_='table-body__cell u-text-right rating')]
player_rating_2_10 = player_rating_2_10[:9]
player_rating_2_10


# In[121]:


rating_list = [first_player_rating] + [i for i in player_rating_2_10]
rating_list


# In[123]:


ODI_batsmen_data = {'player_name':player_list,'team':team_list,'rating':rating_list}
ODI_batsmen_data


# In[124]:


import pandas as pd
ODI_Batsmen_DF = pd.DataFrame(ODI_batsmen_data, index = list(range(1,11)))
ODI_Batsmen_DF


# c)

# In[125]:


page3 = requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi')
page3


# In[126]:


soup3 = BeautifulSoup(page3.content)
soup3


# In[136]:


#first_player = soup3.find('div',class_='rankings-block__banner--name')
first_player = [i for i in soup3.find_all('div',class_='rankings-block__banner--name')[1]]
first_player


# In[151]:


player_2_10 = [i.text.replace('\n','') for i in soup3.find_all('td',class_='table-body__cell name')][9:18]
player_2_10


# In[155]:


ODI_bowlers_list = [i for i in first_player]+[i for i in player_2_10]
ODI_bowlers_list


# In[ ]:





# In[180]:


#ODI_bowler_team_1 = soup.find('div',class_='rankings-block__banner--nationality')
ODI_bowler_team_1 = [i.text.replace('\n','') for i in soup3.find_all('div',class_='rankings-block__banner--nationality')]
ODI_bowler_team_1 = ODI_bowler_team_1[1][:3]
ODI_bowler_team_1


# In[187]:


ODI_bowler_team_2_9 = [i.text for i in soup3.find_all('span',class_='table-body__logo-text')[9:18]]
ODI_bowler_team_2_9

ODI_bowlers_list = [ODI_bowler_team_1] + [i for i in ODI_bowler_team_2_9]
ODI_bowlers_list


# In[197]:


ODI_bolwer_list_1_rating = [i.text for i in soup3.find_all('div',class_='rankings-block__banner--rating')]
ODI_bolwer_list_1_rating = ODI_bolwer_list_1_rating [1]
ODI_bolwer_list_1_rating

ODI_bolwer_list_2_9_rating = [i.text for i in soup3.find_all('td',class_='table-body__cell u-text-right rating')[9:18]]
ODI_bolwer_list_2_9_rating

ODI_bowler_rating = [ODI_bolwer_list_1_rating] + [i for i in ODI_bolwer_list_2_9_rating]
ODI_bowler_rating


# In[198]:


data_ODI_bowler_list = {'player_list':ODI_bowlers_list, 'Country':ODI_bowlers_list,'Rating':ODI_bowler_rating}

ODI_bowler_data = pd.DataFrame(data_ODI_bowler_list, index = range(1,11))
ODI_bowler_data


# In[ ]:





# 6) Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape:
# a) Top 10 ODI teams in women’s cricket along with the records for matches, points and rating.
# b) Top 10 women’s ODI Batting players along with the records of their team and rating.
# c) Top 10 women’s ODI all-rounder along with the records of their team and rating.

# In[200]:


# 6a

page = requests.get ('https://www.icc-cricket.com/rankings/womens/team-rankings/odi')
page

soup = BeautifulSoup(page.content)
soup


# In[207]:


W_ODI_10= soup.find_all('span',class_='u-hide-phablet')
W_ODI_10_list = [i.text for i in W_ODI_10]
W_ODI_10_list = W_ODI_10_list [:10]
W_ODI_10_list


# In[252]:


W_ODI_Matches_1 = soup.find('td',class_='rankings-block__banner--matches').text
#W_ODI_Matches_1

W_ODI_points_1 = soup.find('td',class_='rankings-block__banner--points').text

W_ODI_details_2_9 = [i.text for i in soup.find_all('td',class_='table-body__cell u-center-text')]
#W_ODI_details_2_9



W_ODI_matches_2_9 = [W_ODI_details_2_9[i] for i in range(0,len(W_ODI_details_2_9),2)]
#W_ODI_matches_2_9

W_ODI_matches =[ W_ODI_Matches_1] + [i for i in W_ODI_matches_2_9 ]  

W_ODI_points_2_9 = [W_ODI_details_2_9[i] for i in range(1,len(W_ODI_details_2_9),2)]
W_ODI_points_2_9

W_ODI_points = [W_ODI_points_1] + [i for i in W_ODI_points_2_9]  
W_ODI_points

W_ODI_rating_1 = [i.text.replace('\n','').replace(' ','') for i in soup.find_all('td',class_='rankings-block__banner--rating u-text-right')]
W_ODI_rating_1

W_ODI_rating_2_10 = [i.text for i in soup.find_all('td',class_='table-body__cell u-text-right rating')]
W_ODI_rating_2_10 = W_ODI_rating_2_10 [:9]
W_ODI_rating_2_10

W_ODI_rating = [i for i in W_ODI_rating_1] + [i for i in W_ODI_rating_2_10 ]
W_ODI_rating  

#W_ODI_rating_1


# In[256]:


W_ODI_data = {'Teams':W_ODI_10_list[:10],'Matches[:10]':W_ODI_matches[:10],'Points':W_ODI_points[:10],'Rating':W_ODI_rating[:10]}
W_ODI_data

W_ODI_DF = pd.DataFrame(W_ODI_data, index = range(1,11))
W_ODI_DF


# b)

# In[259]:


#Womens ODI batting

page2 = requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi')
page2

soup = BeautifulSoup(page2.content)
soup


# In[284]:


batting_1_name = soup.find('div',class_='rankings-block__banner--name').text
batting_1_name

batting_2_10_name = [i.text.replace('\n','') for i in soup.find_all('td',class_='table-body__cell name')]
batting_2_10_name = batting_2_10_name[:9]

batting_list = [batting_1_name] + [i for i in  batting_2_10_name]

#batting_2_10_name

team_1_name = (soup.find('div',class_='rankings-block__banner--nationality').text).replace('\n','')[:3]
team_1_name 

team_2_10_name = [i.text for i in soup.find_all('span',class_='table-body__logo-text')]
team_2_10_name = team_2_10_name[:9]
team_2_10_name

team_list = [team_1_name ] + [i for i in team_2_10_name]

rating_1 = soup.find('div',class_='rankings-block__banner--rating').text
rating_1

rating_2_10 = [i.text for i in soup.find_all('td',class_='table-body__cell u-text-right rating')]
rating_2_10 =rating_2_10[:9]
rating_2_10

rating_list = [rating_1]+[i for i in rating_2_10]
rating_list


# In[287]:


W_batting_data = {'Name':batting_list,'team_list':team_list,'Rating':rating_list}
W_batting_data

W_batting_DF = pd.DataFrame(W_batting_data, index = range(1,11))
W_batting_DF


# c)

# In[289]:


page = requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi/all-rounder')
page


# In[290]:


soup = BeautifulSoup(page.content)
soup


# In[310]:


name1 = soup.find('div',class_='rankings-block__banner--name-large').text
name1

name2_10 = [i.text.replace('\n','') for i in soup.find_all('td',class_='table-body__cell rankings-table__name name')]
name2_10 = name2_10[:9]
name2_10

name_list = [name1] + [ i for i in name2_10 ]

team1 = soup.find('div',class_='rankings-block__banner--nationality').text.replace('\n','').replace(' ','')
team1

team2_10 = [i.text for i in soup.find_all('span',class_='table-body__logo-text')]
team2_10 = team2_10 [:9]
team2_10

team = [team1] + [i for i in team2_10]


rating1 = soup.find('div',class_='rankings-block__banner--rating').text
rating1

rating2_10 = [i.text for i in soup.find_all('td',class_='table-body__cell rating')]
rating2_10 = rating2_10[:9]
rating2_10

rating_list = [rating1] + [i for i in rating2_10]
rating_list


# In[314]:


all_rounder_data = {'Name':name_list,'team':team,'Rating':rating_list}
all_rounder_data

all_rounder_DF = pd.DataFrame(all_rounder_data, index = range(1,11))
all_rounder_DF


# 7) Write a python program to scrape details of all the posts from coreyms.com. Scrape the heading, date, content
# and the code for the video from the link for the youtube video from the post.

# In[378]:


from bs4 import BeautifulSoup
import requests

page = requests.get('https://coreyms.com/')
page

soup = BeautifulSoup(page.content)
soup


# In[379]:


headings = soup.find('a',class_='entry-title-link').text
headings


# In[380]:


headings = soup.find_all('a',class_='entry-title-link')
headings_list = [i.text for i in soup.find_all('a',class_='entry-title-link') ]
headings_list


# In[381]:


time_stamp = soup.find_all('time',class_='entry-time')
time_list = [i.text for i in soup.find_all('time',class_='entry-time')]
time_list


# In[382]:


content = soup.find_all('div',class_='entry-content')
content_list = [i.text.replace('\n','') for i in soup.find_all('div',class_='entry-content')]
content_list


# In[383]:


soup2 = BeautifulSoup(page.content, 'html.parser')
soup2


# In[397]:


video_tags = [i['src'] for i in  soup.find_all('iframe',class_='youtube-player')]
video_tags
#for i in  soup.find_all('iframe',class_='youtube-player'):
#    print(i['src'])

print(video_tags)


# In[395]:



Website_data = {'Heading':headings_list,'Date':time_list,'Content':content_list,'link':video_tags}

Website_data_DF = pd.DataFrame(Website_data)
Website_data_DF


# In[409]:


Website_data_DF['link']= video_tags
Website_data_DF

## final DF


# In[ ]:





# In[ ]:





# 8) Write a python program to scrape house details from mentioned URL. It should include house title, location,
# area, EMI and price from https://www.nobroker.in/ .Enter three localities which are Indira Nagar, Jayanagar, 
# Rajaji Nagar

# In[373]:


from bs4 import BeautifulSoup
import requests

page = requests.get('https://www.nobroker.in/property/sale/bangalore/multiple?searchParam=W3sibGF0IjoxMi45NzgzNjkyLCJsb24iOjc3LjY0MDgzNTYsInBsYWNlSWQiOiJDaElKa1FOM0dLUVdyanNSTmhCUUpyaEdEN1UiLCJwbGFjZU5hbWUiOiJJbmRpcmFuYWdhciJ9LHsibGF0IjoxMi45MzA3NzM1LCJsb24iOjc3LjU4MzgzMDIsInBsYWNlSWQiOiJDaElKMmRkbFo1Z1ZyanNSaDFCT0FhZi1vcnMiLCJwbGFjZU5hbWUiOiJKYXlhbmFnYXIifSx7ImxhdCI6MTIuOTk4MTczMiwibG9uIjo3Ny41NTMwNDQ1OTk5OTk5OSwicGxhY2VJZCI6IkNoSUp4Zlc0RFBNOXJqc1JLc05URy01cF9RUSIsInBsYWNlTmFtZSI6IlJhamFqaW5hZ2FyIn1d&radius=2.0&city=bangalore&locality=Indiranagar,&locality=Jayanagar,&locality=Rajajinagar')
page

soup = BeautifulSoup(page.content)
soup


# In[374]:


house_title = [i.text for i in soup.find_all('span',class_='overflow-hidden overflow-ellipsis whitespace-nowrap max-w-80pe po:max-w-full')]
house_title

Area =  [soup.find_all('div',class_='font-semi-bold heading-6')[i].text for i in range(0,len(soup.find_all('div',class_='font-semi-bold heading-6')),3)]
Area

EMI = [soup.find_all('div',class_='font-semi-bold heading-6')[i].text for i in range(1,len(soup.find_all('div',class_='font-semi-bold heading-6')),3)]
EMI

Price = [soup.find_all('div',class_='font-semi-bold heading-6')[i].text for i in range(2,len(soup.find_all('div',class_='font-semi-bold heading-6')),3)]
Price

Location = [i.text for i in soup.find_all('div',class_='mt-0.5p overflow-hidden overflow-ellipsis whitespace-nowrap max-w-70 text-gray-light leading-4 po:mb-0 po:max-w-95')]
Location


# In[375]:


Building_data = {'Title':house_title,'Area':Area,'EMI':EMI,'Price':Price,'Location':Location}
Building_data


# In[376]:


import pandas as pd

Building_DF = pd.DataFrame(Building_data)
Building_DF


# In[ ]:





# 9) Write a python program to scrape mentioned details from dineout.co.in :
# i) Restaurant name
# ii) Cuisine
# iii) Location
# iv) Ratings
# v) Image URL 

# In[356]:


from bs4 import BeautifulSoup
import requests

page = requests.get ('https://www.dineout.co.in/delhi-restaurants/buffet-special')


# In[357]:


soup = BeautifulSoup(page.content)
soup


# In[358]:


resturantname = soup.find_all('div',class_="restnt-info cursor")
resturant_name_list = [i.text for i in soup.find_all('div',class_="restnt-info cursor")]
resturant_name_list


# In[359]:


Cuisine = soup.find('span',class_='double-line-ellipsis').text.split('|')
Cuisine


# In[360]:


details = soup.find_all('span',class_='double-line-ellipsis')

cuisine_list = [i.text.split('|')[1] for i in details]
cuisine_list


# In[361]:


rating = soup.find_all('div',class_='restnt-rating rating-4')

rating_list = [i.text for i in rating]
rating_list


# In[362]:


location = soup.find_all('div',class_='restnt-loc ellipsis')

location_list = [i.text for i in location ]
location_list


# In[363]:


image = soup.find_all('img',class_='no-img')

image_list = [i['data-src'] for i in image]
image_list


# In[364]:


dineout_data = {'Resturant_Name':resturant_name_list,'Cuisine':cuisine_list,'Location':location_list,'Rating':rating_list,'Image_URL':image_list}
dineout_data

import pandas as pd 

dineout_DF = pd.DataFrame(dineout_data)
dineout_DF


# 10) Write a python program to scrape first 10 product details which include product name , price , Image URL from
# https://www.bewakoof.com/women-tshirts?ga_q=tshirts . 

# In[365]:


page = requests.get ('https://www.bewakoof.com/women-t-shirts')
page


# In[366]:


soup = BeautifulSoup (page.content)
soup


# In[367]:


name = soup.find('h3')

product_list = [i.text for i in soup.find_all('h3')]
product_list = product_list[:10]
product_list


# In[368]:


price = soup.find('b')
price


# In[369]:


price_list = [i.text for i in soup.find_all('b')]

price_details = [ soup.find_all('b')[i].text for i in range(0,len(soup.find_all('b')),2)]
price_details

price_details = price_details[:10]
price_details 


# In[370]:


##image = soup.find_all('img')['src']

image_details = [i['src'] for i in soup.find_all(('img'))]
image_details = image_details[:10]
image_details


# In[371]:


bewakoof_data = {'name':product_list,'price':price_details,'image_URL':image_details}
bewakoof_data


# In[372]:


import pandas as pd
bewakoof_df = pd.DataFrame(bewakoof_data, index = range(1,11,1))
bewakoof_df


# In[ ]:




