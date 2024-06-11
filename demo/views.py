from django.shortcuts import render
pages = ['home','learn','gems','inbox','groups','stats','user profile']
icons = ['home','school','diamond','mail','groups','insights','person']
links = ['index','learn','gems','inbox','groups','stats','profile']
# Create your views here.
def index(request):
    ctx = {'pages':pages,
           'links':links,
           'icons':icons,
           'active':'home'
        }
    return(render(request, 'demo/home.html', context=ctx))
# def learn(request):
#     ctx = {'pages':pages,
#            'links':links,
#            'icons':icons,
#            'active':'learn'
#         }
#     return(render(request, 'demo/base.html', context=ctx))
# def groups(request):
#     ctx = {'pages':pages,
#            'links':links,
#            'icons':icons,
#            'active':'groups'
#         }
#     return(render(request, 'demo/base.html', context=ctx))
# def gems(request):
#     ctx = {'pages':pages,
#            'links':links,
#            'icons':icons,
#            'active':'gems'
#         }
#     return(render(request, 'demo/base.html', context=ctx))
# def inbox(request):
#     ctx = {'pages':pages,
#            'links':links,
#            'icons':icons,
#            'active':'inbox'
#         }
#     return(render(request, 'demo/base.html', context=ctx))
# def stats(request):
#     ctx = {'pages':pages,
#            'links':links,
#            'icons':icons,
#            'active':'stats'
#         }
#     return(render(request, 'demo/base.html', context=ctx))
# def profile(request):
#     ctx = {'pages':pages,
#            'links':links,
#            'icons':icons,
#            'active':'user profile'
#         }
#     return(render(request, 'demo/base.html', context=ctx))