from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from .models import Case

# Create your views here.


def home(request):
    context = {
        'cases': Case.objects.all()
    }
    return render(request, 'myapp/home.html', context)


def about(request):
    return render(request, 'myapp/about.html')


def login(request):
    return render(request, 'admin.site.urls')

# our generic class based view are going to be looking at a template with this naming
# convention : <app>/<model>_<viewtype>.html


class PostListView(ListView):
    model = Case
    template_name = 'myapp/home.html'
    context_object_name = 'cases'
    ordering = ['-date_posted']
    paginate_by = 3


class PostDetailView(DetailView):
    model = Case
