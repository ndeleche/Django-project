from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Member


def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))


def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))


def main(request):
    return render(request, 'main.html')


def testing(request):
    template = loader.get_template('testing.html')
    context = {
        'first_name': 'Linux',
    }
    return HttpResponse(template.render(context, request))
