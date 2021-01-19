from django.contrib.admin import site as admin
from django.contrib.admin.sites import AdminSite
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.admin import ModelAdmin
from django.forms import fields

class LibrarianSite(AdminSite):
    site_header = 'library staff'
    site_title = 'library staff site'

librarian = LibrarianSite(name='librarian')
