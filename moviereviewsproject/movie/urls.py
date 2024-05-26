from django.urls import path
from . import views


urlpatterns = [
    path('<int:movie_id>', views.detail, name='detail'),
    path('<int:movie_id>/createreview', views.create_review, name='createreview'),
]