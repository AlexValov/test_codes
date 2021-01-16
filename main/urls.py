from django.urls import path


from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    # path('change_mode', csrf_exempt(views.change_mode), name='change_mode'),
    # path('about-us', views.about_us, name='about_us'),
    # path('about-us/', views.about_us, name='about_us'),
    # path('category', views.category, name='category'),
    # path('category/', views.category, name='category'),
    # path('subcategory/<str:pk>', views.subcategory, name='subcategory'),
    # path('subcategory/<str:pk>/', views.subcategory, name='subcategory'),
    # path('service/<str:pk>', views.service, name='service'),
    # path('service/<str:pk>/', views.service, name='service'),
    # path('promotii', views.promotii, name='promotii'),
    # path('promotii/', views.promotii, name='promotii'),
    # path('promo-details/<str:pk>', views.promo_details, name='promo_details'),
    # path('promo-details/<str:pk>/', views.promo_details, name='promo_details'),
    # path('events', views.events, name='events'),
    # path('events/', views.events, name='events'),
    # path('event-details/<str:pk>', views.events_details, name='events_details'),
    # path('event-details/<str:pk>/', views.events_details, name='events_details'),
    # path('blog', views.blog, name='blog'),
    # path('blog/', views.blog, name='blog'),
    # path('blog-details/<str:pk>', views.blog_details, name='blog_details'),
    # path('blog-details/<str:pk>/', views.blog_details, name='blog_details'),
    # path('appoint_modal', views.appoint_modal, name='appoint_modal'),
    # path('callback_modal', views.callback_modal, name='callback_modal'),
]
