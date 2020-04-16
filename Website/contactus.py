from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from pages.models import ContactUsQuery

def contactus(request):
    """Render a simple contactus page"""
    if request.method =='POST':
        query = ContactUsQuery()
        query.name = request.POST.get('name')
        query.org_name = request.POST.get('org_name')
        query.email = request.POST.get('email')
        query.state = request.POST.get('state')
        query.query = request.POST.get('query')
        query.save()
        return render(request, 'contactus_dashboard.html',
        {'message' : 'Thanks for your query, we will respond shortly.'})

    
    return render(request, 'contactus_dashboard.html')
