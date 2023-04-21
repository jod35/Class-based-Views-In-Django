from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Task
from .forms import TaskCreateForm
from django.views import View
from django.views.generic import(
    #display
    TemplateView,
    ListView,
    DetailView,


    #edit 
    FormView,
    CreateView,
    UpdateView,
    DeleteView
)

# Create your views here.
class HomePageView(ListView):
    template_name = 'index.html'
    model = Task
    context_object_name = 'tasks'


class TaskCreateView(CreateView):
    template_name = 'add.html'
    model = Task
    success_url = '/'
    fields = ['name','description']

class TaskDetailView(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'detail.html'


class TaskUpdateView(UpdateView):
    template_name = 'update.html'
    model = Task
    fields = ['name','description']
    success_url = '/'


class TaskDeleteView(DeleteView):
    template_name ='delete.html'
    model = Task
    success_url ='/'


class SettingsViews(View):
    template_name = 'settings.html'
    def get(self,request):
        return render(request,self.template_name)