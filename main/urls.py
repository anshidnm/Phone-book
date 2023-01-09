from django.urls import path
from main import views

app_name = 'main'

urlpatterns = [
    path('',views.Home.as_view(),name="home"),
    path('create-contact/',views.Create_contact.as_view(),name="create_contact"),
    path('delete-contact/<int:id>/',views.Delete_contact.as_view(),name="delete_contact"),
    path('edit-contact/<int:id>/',views.Edit_contact.as_view(),name="edit_contact"),
    path('view-contact/<int:id>/',views.ViewContact.as_view(),name="view_contact"),
]
