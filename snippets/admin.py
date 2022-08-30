from django.contrib import admin
from .models import User, Snippet, Language

# Register your models here.
admin.site.register(User)
admin.site.register(Snippet)
admin.site.register(Language)


# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ('last_name', 'first_name',
#                     'date_of_birth', 'date_of_death')

#     fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]


# # Register the admin class with the associated model
# admin.site.register(Author, AuthorAdmin)
