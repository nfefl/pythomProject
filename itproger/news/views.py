from django.shortcuts import render, redirect
from .models import Articles, INews
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView
def news_home(request):
    news = Articles.objects.all()
    return render(request, 'news/news_home.html', {'news': news})

class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'

class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/update.html'
    form_class = ArticlesForm

class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news'
    template_name = 'news/news-delete.html'

def INews_home(request):
    inews = INews.objects.all()
    return render(request,'news/iNews_home.html', {'inews': inews})



def create(request):
    if request.method == 'POST':
        form = ArticlesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('news_home')

    form = ArticlesForm()

    date = {
        'form': form,
    }
    return render(request, 'news/create.html', date)
