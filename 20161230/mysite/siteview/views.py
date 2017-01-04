from django.shortcuts import render_to_response
from django.db.models import Q
from django.http import HttpResponse
from models import Book
import datetime
from forms import ContactForm

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def hours_ahead(request, offset):
    offset = int(offset)
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)

def search(request):
    query = request.GET.get('q','')
    if query:
        qset = (
           Q(title__icontains = query) |
           Q(authors__first_name__icontains = query) |
           Q(authors__last_name_icontains = query)
        )
        results = Book.objects.filter(qset).distinct()
    else:
        results = []
    return render_to_response('search.html',{
        'results':results,
        'query':query
    })

def contact(request):
    form = ContactForm()
    return render_to_response('contact.html',{'form':form})
# Create your views here.
