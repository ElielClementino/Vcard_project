from django.shortcuts import render


def introducao(request):
    return render(request, 'introducao.html')
