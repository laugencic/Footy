from django.shortcuts import render


# these will be where the user interactions are handled 

# Create your views here.
def hello(request):
    return render(request,'random.html')