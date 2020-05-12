from django.shortcuts import render, get_object_or_404
from jobs.models import Job
# Create your views here.
def home(request):
    jobs=Job.objects
    return render(request, 'jobs/home.html',{'jobs':jobs})
def detail(request,jid):
    detailjob=get_object_or_404(Job, pk=jid)
    return render(request, 'jobs/detail.html',{'job':detailjob})