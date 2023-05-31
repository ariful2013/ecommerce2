from django.shortcuts import render

# Create your views here.


def home(request):
    context = {'name': "Ariful"}
    return render(request, 'store/home.html', context)
