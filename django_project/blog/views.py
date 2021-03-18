from django.shortcuts import render
# Create your views here.

posts =[
    {
        'author':'Author 1',
        'title': 'Title 1',
        'content': 'Content 1',
        'date_posted':'Date 1'
    },
    {
        'author':'Author 2',
        'title': 'Title 2',
        'content': 'Content 2',
        'date_posted':'Date 2'
    },
    {
        'author':'Author 3',
        'title': 'Title 3',
        'content': 'Content 3',
        'date_posted':'Date 3'
    },
]

#handle from home page of blog
def home(request):
    '''
    templates in a subdirectory of the templates folder to avoid
    issues when there multple apps with templates sicne
    django will look at all template folders when the render function
    is called
    '''
    context = {
        'posts':posts
    }
    return render(request,'blog/home.html',context)

#handles the about page
def about(request):
    return render(request,'blog/about.html',{'title':'About'})