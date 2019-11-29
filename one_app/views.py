from django.shortcuts import render

# Create your views here.

def index(request):
    my_dict = {'insert_content':"Hello, I'm from one_app!!!"}
    return render(request, 'one_app/index.html', context=my_dict)