from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
from learning_logs.models import Topic
from .forms import TopicForm

def index(request):
    """Strona główna dla aplikacji Learning Log."""
    return render(request, 'learning_logs/index.html')


def topics(request):
    """Wyświetlenie wszystkich tematów."""
    topic_set = Topic.objects.order_by('date_added')
    context = {'topics': topic_set}
    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    """Wyświetla pojedyńczy temat i wszystkie powiązane z nim wpisy"""
    topic_entity = Topic.objects.get(id=topic_id)
    entries = topic_entity.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


def new_topic(request):
    """Dodaj nowy temat."""
    if request.method != 'POST':
        # Nie przekazano żadnych danych, należy utworzyć pusty formularz
        form = TopicForm()
    else:
        # Przekazano dane za pomocą żądania POST, należy je przetworzyć
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)
