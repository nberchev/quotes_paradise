from django.shortcuts import render


def load_landing_page(request):
    return render(request, 'landing/landing_page.html')
