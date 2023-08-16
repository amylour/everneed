from django.shortcuts import render

# Create your views here.


def article(request):
    """ A view to return the article page """

    return render(request, 'article/article.html')
