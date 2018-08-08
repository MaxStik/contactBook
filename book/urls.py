from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main-page'),
    path('ajax-add-contact', views.add_contact, name='ajax-add-contact'),
    path('ajax-edit-contact', views.edit_contact, name='ajax-edit-contact'),
    path('ajax-delete-contact', views.delete_contact, name='ajax-delete-contact'),
    path('ajax-get-contact', views.get_contact, name='ajax-get-contact'),
]