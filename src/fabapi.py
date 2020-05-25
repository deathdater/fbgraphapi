import facebook
def search_fb_places():
    # app_token='531028137803440|MTAZ6dDOtX4irhfEflpyVjnOuXM'
    app_token_1='716290055861545|QXtyO5mxb51n4C79LOeQMLsfVrE'
    app_token='284080672994426|lzRAr-vt3f9POl17RDL3SI_Nssc'
    # working in Facebook Graph API explorer

    place_name=input("Enter a Place to Search ?")
    graph = facebook.GraphAPI(access_token=app_token, version = 3.1)
    fields='name, ' \
           'category_list,' \
           'single_line_address'
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
    # print(places.keys())
    # print(places['paging'].keys())
    # print(places['data'][0]['category_list'][0]['name'])
    # places_data_all.update(places['data'])
    category_groups={}
    # try:
    # for place in places['data']:
    #     if (place['category_list'][0]['name'] in category_groups.keys()):
    #         # add id to the internal list
    #         category_groups[str(place['category_list'][0]['name'])].append(place['id'])
    #
    #     else:
    #         category_groups[str(place['category_list'][0]['name'])] = [place['id']]
    #     # print(place['category_list'][0]['name'])
    # print(category_groups)
    page=1

    while (len(places['data']) > 0 and 'paging'in places.keys() ):

        if ('next' in places['paging'].keys()):
            print('fetched page #'+str(page))
            page+=1

            after_str = str(places['paging']['cursors']['after'])
            # api_endpoint = 'search?type=place&q=' + str(place_name) + '&fields=' + str(fields) + '&access_token=' + str(
            #     app_token) + '&after=' + str(after_str)
            api_endpoint=str(places['paging']['next']).replace('https://graph.facebook.com/v7.0/','')
            places = graph.request(api_endpoint)
            # print(places)
            for place in places['data']:
                # print(place['category_list'][0]['name'])
                if (place['category_list'][0]['name'] in category_groups.keys()):
                    # add id to the internal list
                    category_groups[str(place['category_list'][0]['name'])].append(place['id'])

                else:
                    category_groups[str(place['category_list'][0]['name'])] = [place['id']]

        else:
            print('Kaam Hua Poora!!  Taking a Break!!')
            break
    else:
        print('Total Pages searched: '+str(page))
        after_str = ''
        api_endpoint = 'search?type=place&q=' + str(place_name) + '&fields=' + str(fields) + '&access_token=' + str(app_token) + '&after=' + str(after_str)
        places = graph.request(api_endpoint)
       # print(places)
        for place in places['data']:
            #print(place['category_list'][0]['name'])
            if(place['category_list'][0]['name'] in category_groups.keys()):
                #add id to the internal list
                category_groups[str(place['category_list'][0]['name'])].append(place['id'])

            else:
                category_groups[str(place['category_list'][0]['name'])]=[place['id']]



    totalresults=0
    for key in category_groups.keys():
        totalresults+=len(category_groups[key])
        print(str(key)+' : '+str(len(category_groups[key])))

    print('TOTAL Number OF RESULTS FETCHED :'+str(totalresults))


    # print(category_groups)


    # except(KeyError):
    #     print('Last Page reached!!')
    #
    # except():
    #     print('Some Error Occurred!!')
