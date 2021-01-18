from . import views
from django.urls import path

urlpatterns = [
    path('home/',views.order_list,name='home'),
    path('create',views.order_create_view,name="create"),
    path('manager/',views.manager_view,name='manager_module'),
    path('kitchen/',views.kitchen_page,name='kitchen'),


]