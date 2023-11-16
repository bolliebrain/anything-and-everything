from django.shortcuts import render

# Create your views here.
def get_myaande(request):
    return render(request, 'myaande/aande.html')
