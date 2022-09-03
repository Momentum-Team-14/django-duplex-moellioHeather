from django.shortcuts import render, redirect, get_object_or_404
from .models import Snippet
from .forms import SnippetForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def search_snippets(request):
    query = request.GET.get('query')
    qs = Snippet.objects.all()
    if query is not None:
        qs = Snippet.object.search(query)
    context = {
        'snippets_list': qs
    }
    return render(request, 'snippets/search_snippets.html', context)


# @login_required
# def user_profile(request):
#     snippets = Snippet.objects.filter(
#         users=request.user) | Snippet.objects.filter(author=request.user)
#     return render(request, 'snippets/profile.html', {"snippets": snippets})


def snippets_list(request):
    snippets = Snippet.objects.all()
    return render(request, 'snippets/snippets_list.html', {'snippets': snippets})


def snippet_detail(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    return render(request, 'snippets/snippet_detail.html', {'snippet': snippet})

    return redirect('snippets_list')


@login_required
def newSnippet(request):
    if request.method == "POST":  # form submitted
        form = SnippetForm(request.POST)  # defining the form
        if form.is_valid():  # checking if form field are filled out as required
            # so form is not yet saved to the database without the required author, which is set as the user
            snippet = form.save(commit=False)
            # author of new snippet is the user that made the request
            snippet.author = request.user
            snippet.save()
            return redirect('snippets_list')

    form = SnippetForm()  # this is the form to fill out
    context = {'form': form}
    return render(request, 'snippets/new_snippet.html', context)


@login_required
def editSnippet(request, pk):
    snippet = Snippet.objects.get(pk=pk)
    form = SnippetForm(instance=snippet)

    if request.method == "POST":
        form = SnippetForm(request.POST, instance=snippet)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'snippets/new_snippet.html', context)


@login_required
def forkSnippet(request, pk):
    snippet = Snippet.objects.get(pk=pk)
    form = SnippetForm(instance=snippet)

    if request.method == "POST":
        form = SnippetForm(request.POST, instance=snippet)
        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.author = request.user
            snippet.parent = Snippet.objects.get(pk=pk)
            snippet.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'snippets/new_snippet.html', context)


@login_required
def deleteSnippet(request, pk):
    context = {}
    return render(request, 'snippets/delete.html', context)


@login_required
def user_profile(request):
    snippets = Snippet.objects.filter(
        users=request.user) | Snippet.objects.filter(author=request.user)
    return render(request, 'snippets/profile.html', {"snippets": snippets})


def snippet_copy(request, pk):  # or snippets_favorite
    snippet = get_object_or_404(Snippet, pk=pk)
    snippet.pk = None  # pk is which snippet is being worked on, pk = none sets it as a brand new snippet in the database
    snippet.author = request.user
    snippet.save()
