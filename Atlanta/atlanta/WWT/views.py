from django.shortcuts import render


def WWT(request):
    return render(request, 'WWT/main.html')
