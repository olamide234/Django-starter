from django.shortcuts import render

# Create your views here.
# Functions below handle requests passed along by _djgproject/urls.py
def home_view(request):
    return render(request, 'allpages/index.html', {'title': 'Home'}) #template wasn't used because template is assumed

def about_view(request):
    return render(request, 'allpages/about.html', {'title': 'About Us'}) #template wasn't used because template is assumed

def privacy_view(request):
    return render(request, 'allpages/privacy.html', {'title': 'Privacy Policy'}) #template wasn't used because template is assumed