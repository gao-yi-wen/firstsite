from django.shortcuts import render,HttpResponse
from firstapp.models import People,Articles
from django.template import Context,Template
# Create your views here.

def first_try(request):
    person=People(name='Spock',job='officer')
    html_string="""
    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="utf-8">
            <title></title>
        </head>
        <body>
            <div class="child" id="child1">{{person.name}}</div>
            <div class="child" id="child2">{{person.job}}</div>
        </body>
        
    </html>
    """
    t=Template(html_string)
    c=Context({'person':person})
    web_page=t.render(c)

    return HttpResponse(web_page)

def index(request):
    article_list=Articles.objects.all() #取出所有文章
    context={}
    context['article_list']=article_list
    web_page=render(request,'first_landing_page.html',context)
    return web_page