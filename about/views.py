from django.shortcuts import render
from .models import Story
from .models import hopitalStats
# Create your views here.


def aboutview(request):
    story = Story.objects.order_by('-id').first()
    hospitalstats= hopitalStats.objects.order_by('-id').first()
    data={
        'story':story,
        'hospitalstats': hospitalstats
    }

    return render (request, 'about.html',data)