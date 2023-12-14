from django.urls import path, include
from myaande.views import AandeView, PostAande, EditAande
from myaande import views

urlpatterns = [
    path('', AandeView.as_view(), name="seeposts"),
    path('addapost', PostAande.as_view(), name='addpost'),
    path("edit/<int:pk>/", EditAande.as_view(), name='editpost'),
    path('delete/<post_id>', views.delete_myaande, name='delete'),
    path('comment/', views.CommentView, name='comment'),
]