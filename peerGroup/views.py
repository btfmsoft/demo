from django.shortcuts import render

# Create your views here.
def groups(request):
    pages = ['home','learn','gems','inbox','groups','stats','profile']
    icons = ['home','school','diamond','mail','groups','insights','person']
    links = ['index','learn','gems','inbox','groups','stats','profile']
    groups = {
        'Racc Counselor':1,
        'MCC X Trained' :3,
        'Towback Experts': 7,
        'Third Shift': 2,
        'Team Bjorklund' : 4,
        'Peer Mentors' : 3,
        'Supervisor Peers':6
        
    }
    ctx = {
        'pages':pages,
        'icons':icons,
        'links':links,
        'active':'groups',
        'groups':groups,
    }
    return (render(request, 'peerGroup/groups.html',context=ctx))