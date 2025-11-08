from django.urls import path
from . import views


urlpatterns = [
    path('costumers/list/', views.CostumerListView.as_view(), name='costumer_list'),
    path('costumers/create/', views.CostumerCreateView.as_view(), name='costumer_create'),
    path('costumers/<int:pk>/detail/', views.CostumerDetailView.as_view(), name='costumer_detail'),
    path('costumers/<int:pk>/update/', views.CostumerUpdateView.as_view(), name='costumer_update'),
    path('costumers/<int:pk>/delete/', views.CostumerDeleteView.as_view(), name='costumer_delete'),
    path("costumers/export/", views.costumers_export, name="costumers_export"),

    path('api/v1/costumers/', views.CostumerCreateListAPIView.as_view(), name='costumer-create-list-api-view'),
    path('api/v1/costumers/<int:pk>/', views.CostumerRetrieveUpdateDestroyAPIView.as_view(), name='costumer-detail-api-view'),
]
