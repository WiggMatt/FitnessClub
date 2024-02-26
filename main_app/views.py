from django.shortcuts import render


# Create your views here.

def main_page(request):
    return render(request, 'main_app/main.html', {"title": "Home Page"})


def abonements_page(request):
    return render(request, 'main_app/abonements.html',{"title": "Abonements Page"})