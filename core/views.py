from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Snippet

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