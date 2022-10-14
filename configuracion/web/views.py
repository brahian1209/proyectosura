from django.shortcuts import render

# Create your views here.
# Renderizar es pintar 

def Home (request):
        return render(request,'index.html')