from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),  # Vista principal
    path('serie/', views.SeriesView.as_view(), name='series'),  # Lista de series
    path('serie/<int:serie_id>/', views.SerieDetailView.as_view(), name='serie_detail'),  # Detalle de serie
    path('categoria/', views.CategoriaList.as_view(), name='categoria_list'),  # Listar y crear categorías
    path('producto/', views.ProductoList.as_view(), name='producto_list'),  # Listar y crear productos
]