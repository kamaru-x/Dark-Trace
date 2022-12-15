from django.urls import path
from appbnr import views

urlpatterns = [
    path('appbnr/',views.appbnr,name='appbnr'),
    path('manage_appbnr/',views.manage_appbnr,name='manage_appbnr'),
    path('edit_appbnr/<int:bid>/',views.edit_appbnr,name='edit_appbnr'),
    path('remove_appbnr/<int:bid>/',views.remove_appbnr,name='remove_appbnr'),
    path('remove_appbnr_img/<int:bid>/',views.remove_appbnr_img,name='remove_appbnr_img')
]