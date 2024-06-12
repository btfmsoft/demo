from django.shortcuts import render
from django.http import JsonResponse
import json

def stats(request):
    pages = ['home','learn','gems','inbox','groups','stats','user profile']
    icons = ['home','school','diamond','mail','groups','insights','person']
    links = ['index','learn','gems','inbox','groups','stats','profile']
    
    charts = ['Towbacks','Standard 12','Average Call Duration','Adherence/Pacesetter','AME Monitoring']
    types = [['line','line','line','line'],['line','line'],['line','line'],['line','line','line','line'],['line','line'],]
    datasets = [
        'type'
    ]
    
    labels = "['Jan', 'Feb', 'March', 'April', 'May', 'June','July','Aug','Sep','Oct','Nov','Dec']"
    chart1 = {'data': {
          'labels': ['Jan', 'Feb', 'March', 'April', 'May', 'June','July','Aug','Sep','Oct','Nov','Dec'],
          'datasets': [
          {
            'type': 'line',
            'label': 'Overall Towback',
            'data': [10.3, 15.0, 10.7, 11.7, 7.6, 9.6,10.5,8.4,11.3,11.7,8.3,12.9],
            'borderWidth': 4,
            'borderColor':'#420696',
            'borderDash':[1,0]
            
          },
          {
            'type': 'line',
            'label': 'Overall goal',
            'data': [8.1, 8.1, 8.1, 8.1, 8.1, 8.1,8.1, 8.1, 8.1, 8.1, 8.1, 8.1],
            'borderWidth': 2,
            'borderColor': '#420696',
            'borderDash':[5,10],
          },
          {
            'type': 'line',
            'label': 'Cor Towback',
            'data': [10.4,12.8,9.4,9.66,5.1,7.35,7.73,5.81,8.81,6.38,7.29,10.89],
            'borderWidth': 4,
            'borderColor':'#bfc0ee',
            'borderDash':[1,0]
          },
          {
            'type': 'line',
            'label': 'Cor goal',
            'data': [5.5, 5.5, 5.5, 5.5, 5.5, 5.5,5.5, 5.5, 5.5, 5.5, 5.5, 5.5],
            'borderWidth': 2,
            'borderColor': '#bfc0ee',
            'borderDash':[10,5],
          },
          ]
        },
        'options': "{plugins:{legend:{labels:{boxHeight:0,}}},scales:{y: {beginAtZero: false}}}"
    }
    chart2 = {
        
        'data': {
        'labels': ['Jan', 'Feb', 'March', 'April', 'May', 'June','July','Aug','Sep','Oct','Nov','Dec'],
        'datasets': [
        {
            'type': 'line',
            'label': 'STD 12',
            'data':  [59.8,72.7,82.2,90.5,68.6,82.6,82.1,80,68,72.4,74.1,75],
            'borderWidth': 4,
            'borderColor':'#420696',
            'borderDash':[1,0]
            
        },
        {
            'type': 'line',
            'label': 'STD 12 goal',
            'data': [82, 82, 82, 82, 82, 82,82, 82, 82, 82, 82, 82],
            'borderWidth': 2,
            'borderColor': '#420696',
            'borderDash':[5,10],
        },
        ]
        },
        'options': "{plugins:{legend:{labels:{boxHeight:0,}}},scales: {y: {beginAtZero: false,min:65,max:100,}}}"
    }
    chart3 = {'data':{
                'labels': ['Jan', 'Feb', 'March', 'April', 'May', 'June','July','Aug','Sep','Oct','Nov','Dec'],
                'datasets': [{
                    'label':'Average Call Duration',
                    'data': [362,358,358,379,368,338,393,370,393,368,377,369],
                },{
                    'label':'ACD Goal',
                    'data': [296,296,296,296,296,296,296,296,296,296,296,296],
                    'borderDash':[5,10],
                }],
            },
            'options': "{plugins:{legend:{labels:{boxHeight:0,}}},scales: {y: {beginAtZero:false}}}"
            }
    chart4 = {
        
        'data': {
        'labels': ['Jan', 'Feb', 'March', 'April', 'May', 'June','July','Aug','Sep','Oct','Nov','Dec'],
        'datasets': [
        {
            'type': 'line',
            'label': 'Adherence',
            'data': [94,94,90,93,94,94,89,93,91,93,95,93],
            'borderWidth': 4,
            'borderColor':'#420696',
            
        },
        {
            'type': 'line',
            'label': 'Adherence goal',
            'data': [92,92,92,92,92,92,92,92,92,92,92,92],
            'borderWidth': 2,
            'borderColor': '#420696',
            'borderDash':[5,10],
        },
        {
          'type': 'line',
          'label': 'Pacesetter',
          'data': [92,89,89,85,89,90,90,91,91,96,88.5,90],
          'borderWidth': 4,
          'borderColor':'#bfc0ee'
        },
        {
          'type': 'line',
          'label': 'Pacesetter goal',
          'data': [92,92,92,92,92,92,92,92,92,92,92,92],
          'borderWidth': 2,
          'borderColor': '#bfc0ee',
          'borderDash':[10,5],
        },
        ]
        },
        'options': "{plugins:{legend:{labels:{boxHeight:0,}}},scales: {y: {beginAtZero: false,}}}"
    }
    chart5 = {
        
        'data': {
        'labels': ['Jan', 'Feb', 'March', 'April', 'May', 'June','July','Aug','Sep','Oct','Nov','Dec'],
        'datasets': [
        {
            'type': 'line',
            'label': 'AME',
            'data': [1,1,1,1,1,1,1,1,1,0,1,1],
            'borderWidth': 4,
            'borderColor':'#420696',
            
        },
        {
            'type': 'line',
            'label': 'AME goal',
            'data': [1,1,1,1,1,1,1,1,1,1,1,1,1],
            'borderWidth': 2,
            'borderColor': '#420696',
            'borderDash':[5,10],
        },
        ]
        },
        'options': "{plugins:{legend:{labels:{boxHeight:0}}},scales: {y: {beginAtZero: true,min:0,max:3,ticks:{stepSize:1,callback: ((context, index) => {let response;if(context==1) {response = 'Intermediate'} else if (context==2) {response = 'High Intermediate'} else if (context ==3) {response = 'Expert'} else {response = 'Foundational'} return response})}}}}"
    }
    ctx = {
        'pages':pages,
        'icons':icons,
        'links':links,
        'active':'stats',
        'cds':[chart1,chart2,chart3,chart4,chart5],
    }
    return (render(request, 'stats/stats.html',context=ctx))
# Create your views here.
#