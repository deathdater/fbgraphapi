import facebook

app_token='531028137803440|MTAZ6dDOtX4irhfEflpyVjnOuXM'
# working in Facebook Graph API explorer

place_name=input("Enter a Place to Search ?")
graph = facebook.GraphAPI(access_token=app_token, version = 3.1)
fields='name, ' \
       'category_list'
       # 'checkins,' \
       # 'website,' \
       # 'link,' \
       # 'cover,' \
       # 'description,' \
       # 'overall_rating,' \
       # 'about,' \
       # 'category_list' \
       # 'engagement' \
       # 'hours' \
       # 'is_always_open' \
       # 'is_permanently_closed' \
       # 'is_verified' \
       # 'overall_star_rating' \
       # 'page' \
       # 'parking' \
       # 'payment_options' \
       # 'phone' \
       # 'price_range' \
       # 'rating_count' \
       # 'restaurant_services' \
       # 'restaurant_specialities' \
       # 'temporary_status'
after_str=''
api_endpoint='search?type=place&q='+str(place_name)+'&fields='+str(fields)+'&access_token='+ str(app_token)+'&after='+str(after_str)
places_data_all={}
places = graph.request(api_endpoint)
print(places)
# print(places['data'][0]['category_list'][0]['name'])
# places_data_all.update(places['data'])
try:
    for place in places['data']:
        print(place['category_list'][0]['name'])

    while(places['paging']['next']!=None):
       after_str=str(places['paging']['cursors']['after'])
       api_endpoint = 'search?type=place&q=' + str(place_name) + '&fields=' + str(fields) + '&access_token=' + str(app_token) + '&after=' + str(after_str)
       places = graph.request(api_endpoint)
       print(places)
       for place in places['data']:
           print(place['category_list'][0]['name'])
except(KeyError):
    print('Last Page reached!!')