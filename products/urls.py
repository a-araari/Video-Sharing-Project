from django.urls import path
from . import views


urlpatterns = [
	path('', views.product_list, name='product_list'),
	path('add/', views.add, name='product_add'),
	path('<int:pk>/detail/', views.ProductDetail.as_view(), name='product_detail'),
	path('<int:pk>/update/', views.update, name='product_update'),
	path('<int:pk>/delete/', views.delete, name='product_delete'),

]