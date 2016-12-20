from django.shortcuts import render_to_response,HttpResponseRedirect

# Create your views here.

def add(request):
    return render_to_response('add.html')

