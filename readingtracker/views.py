from django.shortcuts import render
import pyjokes


def home(request):
    context = {
        'page_title': 'Workshop',
        'message': 'A message',
        'jokes': pyjokes.get_jokes()[:10]
    }
    return render(request, 'index.html', context)
