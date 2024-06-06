from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
@login_required
def home(request):
    return render(request, "home.html", {})


@login_required
def view_lists(request):
    return render(request, "view_lists.html", {})
