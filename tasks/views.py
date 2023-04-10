from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Task
from .forms import TaskCreateForm
from django.views import View

# Create your views here.


class HomePageView(View):
    template_name = 'index.html'

    def get(self, request):
        tasks = Task.objects.all()
        context = {
            'tasks': tasks
        }
        return render(request, 'index.html', context)


class TaskCreateView(View):
    template_name = 'add.html'
    form_class = TaskCreateForm
    initial = {'key': 'value'}

    def get(self, request):
        return render(request, self.template_name,
                      {'form': self.form_class(initial=self.initial)})

    def post(self, request):
        form = self.form_class(data=request.POST)

        if form.is_valid():
            form.save()

            return redirect(reverse('homepage'))

        return render(request, self.template_name,
                      {'form': self.form_class(initial=self.initial)})


class TaskDetailView(View):
    template_name = 'detail.html'

    def get(self, request, task_id):
        task = Task.objects.get(id=task_id)
        return render(request, self.template_name, {'task': task})


class TaskUpdateView(View):
    template_name = 'update.html'
    form_class = TaskCreateForm

    def get(self, request, task_id):
        task = Task.objects.get(id=task_id)
        form = self.form_class(instance=task)

        return render(request, self.template_name, {'form': form})

    def post(self, request, task_id):
        task = Task.objects.get(id=task_id)
        form = self.form_class(instance=task, data=request.POST)

        if form.is_valid():
            form.save()

            return redirect(reverse('homepage'))

        return render(request, self.template_name, {'form': form})



class TaskDeleteView(View):

    def get(self, request, task_id):
        task = Task.objects.get(id=task_id)

        task.delete()

        return redirect(reverse('homepage'))
