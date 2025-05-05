# Create your views here.
from django.shortcuts import render


def features_view(request):
    context = {'exclude_auth_buttons': True}
    return render(request, 'features_page.html', context)

def home_view(request):
    return render(request, 'home.html') # No exclude_auth_buttons here, so they will show