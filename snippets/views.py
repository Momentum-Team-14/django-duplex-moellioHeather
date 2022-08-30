from django.shortcuts import render, redirect, get_object_or_404
from .models import Snippet
from .forms import SnippetForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def snippets_list(request):
    snippets = Snippet.objects.all()
    return render(request, 'snippets/snippets_list.html', {'snippets': snippets})

# def album_detail(request, pk):
#     album = get_object_or_404(Album, pk=pk)
#     return render(request, 'albums/album_detail.html', {'album': album})


def newSnippet(request):
    form = SnippetForm()
    if request.method == "POST":
        # print(request.POST)
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('snippets_list')

    context = {'form': form}
    return render(request, 'snippets/new_snippet.html', context)


def editSnippet(request, pk):
    snippet = Snippet.objects.get(pk=pk)
    form = SnippetForm(instance=snippet)

    if request.method == "POST":
        form = SnippetForm(request.POST, instance=snippet)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'snippet/new_snippet.html', context)


# def createLanguage(request, pk):
#     snippet = Snippet.objects.get(pk=pk)

#     if request.method == "POST":
#         form = SnippetForm(request.POST, instance=snippet)
#         if form.is_valid():
#             form.save()
#             return redirect('/')

#     context = {'form': form}
#     # def deleteAlbum(request, pk):
#     return render(request, 'snippet/new_snippet.html', context)
# #     context = {}
# #     return render(request, 'albums/delete.html', context)
