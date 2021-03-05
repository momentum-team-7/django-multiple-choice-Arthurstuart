from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Snippet
from .forms import SnippetForm
from django.http import HttpResponseRedirect

# Create your views here.
def snippet_list(request):
    snippets = Snippet.objects.all()
    return render(request, 'index.html', {"snippets":snippets})


def add_snippet(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = SnippetForm()
    return render(request, 'add_snippet.html', {'form': form})


def edit_snippet(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    if request.method == 'POST':
        form = SnippetForm(request.POST, instance=snippet)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    else:
        form = SnippetForm(instance=snippet)
    return render(request, 'edit_snippet.html', {'form': form, 'snippet':snippet })


def delete_snippet(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    snippet.delete()
    return HttpResponseRedirect('/')