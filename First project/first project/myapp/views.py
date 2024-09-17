from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Myapp, Comment
from .form import MyappForm


def home(request):
    return HttpResponse('<h1>welcome</h1>')


# Create your views here.


def myapp_list(request):
    myapps = Myapp.objects.all()
    context = {'myapps': myapps}
    return render(request, 'myapps/myapp_list.html', context=context)


def myapp_detail(request, myapp_id):
    myapp = Myapp.objects.get(pk=myapp_id)
    comments = Comment.objects.filter(Myapp=myapp)
    context = {'myapp': myapp, 'comments': comments}
    return render(request, 'myapps/myapp_detail.html', context=context)


def myapp_create(request):
    if request.method == 'POST':
        form = MyappForm(request.POST)
        if form.is_valid():
            print(type(form.cleaned_data))
            print(form.cleaned_data)
            Myapp.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/myapps/')
    else:
        form = MyappForm()

    return render(request, 'myapps/myapp_create.html', {'form': form})
