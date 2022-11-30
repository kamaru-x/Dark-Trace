from django.urls import path
from api import views

urlpatterns = [
    path('',views.home),
    path('about',views.about_us),
    path('contact',views.contact_us),
    # path('feedback/',views.feedback),
    # path('enquiry/',views.enquiry),
    # path('footer/',views.footer),
    path('header',views.header),
    path('theme',views.theme),
    # path('banner/',views.banner),
    path('blog',views.blog),
    path('blog/<int:id>',views.blog_details),
    path('album',views.album),
    path('album/<int:id>',views.album_images),
    # path('clients/',views.goc),
    path('products',views.products),
    path('products/<int:id>',views.product_details),
    path('services',views.services),
    path('services/<int:id>',views.service_details),
    # path('testimonial/',views.testimonials),
]