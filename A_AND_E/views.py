from django.shortcuts import render
from django.template import RequestContext


def handler404(request, *args, **argv):
    return render(request, "404.html", {})

def handler500(request, *args, **argv):
    return render(request, "500.html", {})