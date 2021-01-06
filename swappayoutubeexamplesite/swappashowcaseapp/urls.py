from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('<City>/', views.GetSite.as_view(template_name='site.html' ), name='Site View'),

]
