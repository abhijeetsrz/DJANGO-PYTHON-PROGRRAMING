
from myproject02.settings import AUTH_PASSWORD_VALIDATORS
from django.shortcuts import render


posts = [
    {
        'author': 'CoreyMs',
        'title': 'calc post 1',
        'content': 'First post content',
        'date_posted': 'May 12, 2021'
    },
    {
          
        'author': 'Abhijeet kumar',
        'title': 'calc post 2',
        'content': 'Second post content',
        'date_posted': 'May 13, 2021'
    
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request,'calc/home.html',context)


def about(request):
     return render(request,'calc/about.html', {'title':'About'})

