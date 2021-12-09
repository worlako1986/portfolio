from django.http.response import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from jobs.models import Job, Person


# Create your views here.

class HomeView(TemplateView):
    template_name = "jobs/index.html"
    jobs =  Job.objects.all()
    extra_context = {"jobs":jobs}


def home(request):

    try:

        person = Person.objects.get(pk = 1)
        jobs = Job.objects.filter(person = person)
        return render(request, "jobs/index.html", {
            "jobs": jobs,
            "person":person
            })

    except Exception as e:
        raise Http404


def detail(request, job_id:int):
    job = get_object_or_404(Job, pk = job_id)
    return render(request, "jobs/detail.html", {"job":job})
