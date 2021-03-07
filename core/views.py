from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from .models import Snippet

# Create your views here.
def snippet_list(request):
    snippets = Snippet.objects.all()
    return render(request, 'index.html', {"snippets":snippets})

@login_required
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
        form = SnippetForm(request.POST, instace=snippet)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    else:
        form = SnippetForm(instace=snippet)
    return render(request, 'edit_snippet.html', {'form': form, 'snippet': snippet})


def delete_snippet(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    snippet.delete()
    return HttpResponseRedirect('/')


def user_snippet_list(request):
    pass

class SearchResultsView(ListView):
    model = Snippet
    template_name = 'search_results.html'    
    # queryset = Snippet.objects.filter(title__icontains='obo')
    # queryset = Snippet.objects.filter(language__icontains='obo')
    # queryset = Snippet.objects.filter(language__title__icontains='obo') ****having issues with joining names, tabling for now. 
   
    def get_queryset(self):
        query = self.request.GET.get('q')
        snippet_list = Snippet.objects.filter(
            Q(language__icontains= query) | Q(title__icontains= query) | Q(description__icontains = query)
            )
        return snippet_list    