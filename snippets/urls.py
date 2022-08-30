from django.urls import path
from . import views

urlpatterns = [
    path('', views.snippets_list, name='snippets_list'),
    # path('snippet_title/<int:pk>', views.snippet_detail, name='snippet_detail'),
    path('new_snippet/', views.newSnippet, name="new_snippet"),
    # path('edit_snippet/<int:pk>', views.editSnippet, name="edit_snippet"),
]


# urlpatterns = [
#     path('', views.list_albums, name='list_albums'),
#     path('album_title/<int:pk>', views.album_detail, name='album_detail'),
#
#     # path('delete_item/<int:pk>/', views.deleteItem, name="delete_item"),
#     path('create_album/', views.createAlbum, name="create_album"),
#     path('edit_album/<int:pk>', views.editAlbum, name="edit_album"),
#     path('delete_album/<int:pk>', views.deleteAlbum, name="delete_album"),
