from django.shortcuts import render

def stats(request):
    pages = ['home','learn','gems','inbox','groups','stats','user profile']
    icons = ['home','school','diamond','mail','groups','insights','person']
    links = ['index','learn','gems','inbox','groups','stats','profile']
    
    ctx = {
        'pages':pages,
        'icons':icons,
        'links':links,
        'active':'stats',
    }
    return (render(request, 'stats/stats.html',context=ctx))
# Create your views here.
