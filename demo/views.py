from django.shortcuts import render

# Create your views here.
def index(request):
    pages = ['home','learn','gems','inbox','groups','performance','user profile']
    icons = ['home','school','diamond','mail','groups','insights','person']
    links = ['index.html','learn.html','gems.html','inbox.html','groups.html','stats.html','profile.html']
        # {
    #     'home':{
    #         'icon':'home',
    #         'link':'index.html',
    #         'tooltip':'home',
    #     },
    #     "school":{
    #         "icon":'school',
    #         'link':'learn.html',
    #         'tooltip':'Learn',
    #     },
    #     'diamond':{
    #         'icon':'diamond',
    #         'link':'gems.html',
    #         'tooltip':'Gem rewards'  
    #     },
    #     'mail':{
    #         'icon':'email',
    #         'link':'inbox.html',
    #         'tooltip':'Internal mail'  
    #     },
    #     'groups':{
    #         'icon':'groups',
    #         'link':'groups.html',
    #         'tooltip':'Peer Groups'  
    #     },
    #     'insights':{
    #         'icon':'insights',
    #         'link':'stats.html',
    #         'tooltip':'Metrics'  
    #     },
    #     'person':{
    #         'icon':'person',
    #         'link':'profile.html',
    #         'tooltip':'User Profile'  
    #     }
    # }
    ctx = {'pages':pages,
           'links':links,
           'icons':icons,
           'active':'home'
        }
    return(render(request, 'demo/base.html', context=ctx))