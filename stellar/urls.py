from django.contrib import admin
from django.urls import path
from stellar import views
urlpatterns = [

    path('emp', views.emp),
    path('show',views.show),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy),
]