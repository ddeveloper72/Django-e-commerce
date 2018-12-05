from django.shortcuts import render

# Create your views here.
def index(request):
    """Display and index page"""
    return render(request, "index.html")
