from django.shortcuts import render, redirect
from .models import Artiles
from .forms import ArtilesForm
from django.views.generic import DetailView

# Create your views here.
def news_home(request):
    news = Artiles.objects.order_by('-date')
    return render(request, 'news/news_file.html', {'news': news})

class NewDetailView(DetailView):
    model = Artiles
    template_name = 'news/details_view.html'
    context_object_name = 'article '

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArtilesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news')
        else:
            error = 'Форма была неверной'

    form = ArtilesForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)
