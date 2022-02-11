from django.shortcuts import render

# Create your views here.
def index(request):
  
    return render(request, 'main/index.html')

def camping_detail(request):
  
    return render(request, 'main/camping_detail.html')