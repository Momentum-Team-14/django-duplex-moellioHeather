from django.urls import path
from . import views

urlpatterns = [
    path('', views.snippets_list, name='snippets_list'),
    # path('snippet_title/<int:pk>', views.snippet_detail, name='snippet_detail'),
    path('new_snippet/', views.newSnippet, name="new_snippet"),
    path('edit_snippet/<int:pk>', views.editSnippet, name="edit_snippet"),
    path('fork_snippet/<int:pk>', views.forkSnippet, name="fork_snippet"),
    path('delete_snippet/<int:pk>', views.deleteSnippet, name="delete_snippet"),
    path('user_profile', views.user_profile, name='user_profile'),
    path('search_snippets', views.search_snippets, name='search_snippets'),

]
