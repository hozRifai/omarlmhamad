from django.shortcuts import render
#from django.views.generic import Listview , DetailView , CreateView , UpdateView

# Create your views here.
def home(request):
	return render(request , "index.html", {} )

def contact(request):
	return render(request , "contact.html" , {} )



