from django.shortcuts import render

# Create your views here.
def learn(request):
    pages = ['home','learn','gems','inbox','groups','stats','profile']
    icons = ['home','school','diamond','mail','groups','insights','person']
    links = ['index','learn','gems','inbox','groups','stats','profile']
    ctx = {
        'pages':pages,
        'icons':icons,
        'links':links,
        'active':'learn',
    }
    return (render(request, 'learn/learn.html',context=ctx))