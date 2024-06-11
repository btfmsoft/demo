from django.shortcuts import render

# Create your views here.
def groups(request):
    pages = ['home','learn','gems','inbox','groups','stats','profile']
    icons = ['home','school','diamond','mail','groups','insights','person']
    links = ['index','learn','gems','inbox','groups','stats','profile']
    ctx = {
        'pages':pages,
        'icons':icons,
        'links':links,
        'active':'groups',
    }
    return (render(request, 'peerGroup/groups.html',context=ctx))