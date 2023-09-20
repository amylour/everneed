from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User


def article_list(request):
    """ A view to return the articles page """
    articles = Article.objects.all()

    context = {
        'articles': articles,
    }

    return render(request, 'article/article_list.html', context)


def article(request, slug):
    """ View individual articles """
    # Get  the article based on the slug
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'article/article.html', {'article': article})


@login_required
def add_article(request):
    """ Create an Article """
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            #  don't save data immediately, instead creat an instance
            article = form.save(commit=False)
            article.author = request.user
            if request.user.is_superuser and 'post_now' in request.POST:
                article.status = Article.PUBLISHED
            else:
                article.status = Article.DRAFT
            article.save()
            if article.status == Article.DRAFT:
                messages.success(request, 
                 'Your article has been saved as a draft.') 
            else:
                messages.success(request,
                 f'Your article {article.title} has been posted.')
            return redirect('article_list')
    else:
        form = ArticleForm()
    return render(request, 'articles/add_article.html', {'form': form})


@login_required
def edit_article(request, slug):
    """ Edit an Article """
    article = get_object_or_404(Article, slug=slug)
    if request.user != article.author:
        raise PermissionDenied
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article) 
        if form.is_valid(): 
            form.save()
            messages.success(request,
              f'Your article {article.title} has been updated.')
            return redirect ('article_page', slug=slug)
    else: 
        form = ArticleForm(instance=article)
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'article/edit_article.html', context)


@login_required
def delete_article(request, slug):
    """ Delete an Article """
    article = get_object_or_404(Article, slug=slug)
    if request.user != article.author: 
        raise PermissionDenied
    if request.method == 'POST':
        article.delete()
        messages.success(request,
         f'Article {article.title} deleted successfully.')
    return redirect ('article_list')



