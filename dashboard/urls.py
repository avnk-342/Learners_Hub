from django.urls import path, include
from . import views

urlpatterns = [
path('',views.home , name="home"),
path('notes',views.notes , name="notes"),
path('delete_note/<int:pk>',views.delete_note , name="delete-note"),
path('notes_detail/<int:pk>',views.NotesDetailView.as_view() , name="notes-detail"),

path('homework',views.homework , name="homework"),
# path('updates_homework/<int:pk>',views.update_homework , name="homework"),
path('delete_homework/<int:pk>',views.delete_homework ,name="delete-homework"),

path ('youtube',views.youtube , name="youtube"),

path ('todo',views.todo , name="todo"),
]