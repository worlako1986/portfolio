from django.shortcuts import render
from django.views.generic import TemplateView
from jobs.models import Job, Person


# Create your views here.

class HomeView(TemplateView):
    template_name = "jobs/index.html"
    jobs =  Job.objects.all()
    extra_context = {"jobs":jobs}


def home(request):

    person = Person.objects.get(pk = 1)
    jobs = Job.objects.filter(person = person)

    return render(request, "jobs/index.html", {
        "jobs": jobs,
        "person":person
    })
