from django.urls import path, include
from myaande.views import AandeView
from myaande import views

urlpatterns = [
    path('', AandeView.as_view(), name='seeposts'),
    path('addapost', views.post_myaande, name='addpost'),
    path('edit/<post_id>', views.edit_myaande, name='editpost'),
    path('delete/<post_id>', views.delete_myaande, name='delete'),
    path('comment/', views.CommentView, name='comment'),
]