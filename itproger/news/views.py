from django.shortcuts import render, redirect
from .models import Articles, INews
from .forms import ArticlesForm
def news_home(request):
    news = Articles.objects.all()
    return render(request, 'news/news_home.html', {'news': news})

def INews_home(request):
    inews = INews.objects.all()
    return render(request,'news/iNews_home.html', {'inews': inews})

def create(request):
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')

    form = ArticlesForm()

    date = {
        'form': form,
    }
    return render(request, 'news/create.html', date)
