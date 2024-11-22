from django.shortcuts import render, redirect
from .models import Task
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,  logout, login





# Create your views here.

def index(request):
    return render(request, 'index.html')

class TaskListView(ListView):
    model = Task

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['object_list'] = context['object_list'].filter(user=self.request.user)
        return context

class TaskDetailView(DetailView):
    model = Task

class TaskCreateView(CreateView):
    model = Task
    fields =['title', 'description', 'is_done']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreateView, self).form_valid(form)
    

class TaskUpdateView(UpdateView):
    model = Task
    fields =['title', 'description', 'is_done']
    success_url = reverse_lazy('tasks')

class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('tasks')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username exists')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email exists')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=pass1)
                user.save()
                return redirect('login')
        else:
            messages.info(request, "passwords don't match")
            return render(request, 'signup.html')
    else:
        return render(request, 'signup.html')
    

def log_in(request):
     if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('tasks')
        else:
            return render(request, 'login.html')
     else:
         return render(request, 'login.html')
    

def log_out(request):
    logout(request)
    return redirect('/')


    
