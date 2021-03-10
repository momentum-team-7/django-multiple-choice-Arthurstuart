from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView
from django.db.models import Q, Count
from .models import Snippet, User
from .forms import SnippetForm #,Userform
from django.http import HttpResponseRedirect

# Create your views here.
def snippet_list(request):
    snippets = Snippet.objects.all()
    return render(request, 'index.html', {"snippets":snippets})

def homepage_render(request):
    snippets = Snippet.objects.all()    
    return render(request, 'user_home.html', {"snippets":snippets})    

# def page_appender(request): #Eventually you can have input var url
#     users = User.objects.all()
#     teststr  = "testing this out"
#     return render(request, 'profile.html', {"users":users})
#     # return render(request, 'profile.html', {"users":users})


@login_required
def add_snippet(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return HttpResponseRedirect('/submitted/')
    else:
        form = SnippetForm()
    return render(request, 'add_snippet.html', {'form': form})


def edit_snippet(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    if request.method == 'POST':
        form = SnippetForm(request.POST, instance=snippet)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/user_home/')

    else:
        form = SnippetForm(instance=snippet)
    return render(request, 'edit_snippet.html', {'form': form, 'snippet':snippet })


def delete_snippet(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    snippet.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def snippet_user_submitted(request):
    user = request.user
    snippets = Snippet.objects.filter(user=user)
    return render(request, 'submitted.html',  {"snippets": snippets})


# def snippet_networkfeed(request):
#     user = request.user.all
#     snippets = Snippet.objects.all
#     return render(request, 'network-feed.html', {"user": user} {"snippets": snippets})

def user_list(request):
    users = User.objects.all()
    return render(request, 'network-feed.html', {"users":users})

def top_user(request):
    top_user = User.objects.all() \
        .annotate(num_snippets=Count('snippet')) \
        .order_by('-num_snippets')
    return render(request, 'network-feed.html', {"top_user": top_user})

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


def user_list_count(request):
    top_users = User.objects.all() \
    .annotate(num_snippets=Count('snippet')) \
    .order_by("-num_snippets")
    top_users = top_users[:5]
    return render(request, 'user_list.html', {"top_users": top_users})




def save_snippet(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    snippet.pk = None
    snippet.user = request.user
    snippet.save()
    return render(request, 'snippet_added.html')
