from django.shortcuts import render
from .models import Post
# Create your views here.


#handle from home page of blog
def home(request):
    '''
    templates in a subdirectory of the templates folder to avoid
    issues when there multple apps with templates sicne
    django will look at all template folders when the render function
    is called
    '''
    context = {
        'posts':Post.objects.all()
    }
    return render(request,'blog/home.html',context)

#handles the about page
def about(request):
    return render(request,'blog/about.html',{'title':'About'})