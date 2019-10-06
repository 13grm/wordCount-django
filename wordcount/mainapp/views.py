from django.shortcuts import render

def home(request):
    context = {

    }
    return render(request, "mainapp/home.html", context=context)


def count(request):
    context = {

    }
    return render(request, 'mainapp/count.html', context=context)