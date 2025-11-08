from django.urls import path
from . import views


urlpatterns = [
    path('costumers/list/', views.SupplierListView.as_view(), name='costumer_list'),
    path('costumers/create/', views.SupplierCreateView.as_view(), name='costumer_create'),
    path('costumers/<int:pk>/detail/', views.SupplierDetailView.as_view(), name='costumer_detail'),
    path('costumers/<int:pk>/update/', views.SupplierUpdateView.as_view(), name='costumer_update'),
    path('costumers/<int:pk>/delete/', views.SupplierDeleteView.as_view(), name='costumer_delete'),

    path('api/v1/costumers/', views.SupplierCreateListAPIView.as_view(), name='costumer-create-list-api-view'),
    path('api/v1/costumers/<int:pk>/', views.SupplierRetrieveUpdateDestroyAPIView.as_view(), name='costumer-detail-api-view'),
]
