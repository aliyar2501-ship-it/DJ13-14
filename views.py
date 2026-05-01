from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse

def hello_html(request):
    return HttpResponse("<h1>Урок 7</h1><p>Это <b>HTML-строка</b> на фронтенд.</p>")

def get_data(request):
    data = [
        {"id": i, "value": i * 10}
        for i in range(1, 11)
    ]
    return JsonResponse(data, safe=False)