from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:id>', views.view, name='view'),
    path('add_product', views.add_product, name='add_product') ,
    path('edit_product/<int:id>', views.edit_product, name='edit_product'),
    path('delete_product/<int:id>', views.delete_product, name='delete_product'),
    path('pos', views.pos, name='pos')
]
