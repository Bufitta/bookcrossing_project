from django.urls import path
from catalog.views import index_view, categories_view, category_detail_view, book_detail_view

app_name = 'catalog'

urlpatterns = [
    path('', index_view, name='index'),
    path('categories/', categories_view, name='categories'),
    path('categories/<int:id>/', category_detail_view, name='category_detail'),
    path('book/<int:id>/', book_detail_view, name='book_detail'),
]
