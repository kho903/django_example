from django.urls import path

from bookmark import views
from bookmark.views import BookmarkLV, BookmarkDV

app_name = 'bookmark'
urlpatterns = [
    path('', BookmarkLV.as_view(), name='index'),
    path('<int:pk>', BookmarkDV.as_view(), name='detail'),

    # /bookmark/add/
    path('add/', views.BookmarkCreateView.as_view(), name='add'),
    path('change/', views.BookmarkChangeLV.as_view(), name='change'),
    path('<int:pk>/update/', views.BookmarkUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.BookmarkDeleteView.as_view(), name='delete'),
]