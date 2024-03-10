from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.mains, name='home'),
    path('search/', views.search, name='search'),
    path('prodsaree/', views.prodsaree, name='prodsaree'),
    path('prodsuit/', views.prodsuit, name='prodsuit'),
    path('prodfabric/', views.prodfabric, name='prodfabric'),
    path('check_out/', views.checkout, name='check_out'),
    path('story/', views.story, name='story'),
    path('privacypolicy/', views.privacy, name='privacy'),
    path('shipping/', views.shipping, name='shipping'),
    path('termsandcondition/', views.terms, name='termsandcondition'),
    path('cancel/', views.cancel, name='cancel'),
    path('product/<str:productId>/', views.product, name='product'),
    path('payment/<int:order_id>/', views.payment, name='payment'),
    path('delete/<int:order_id>/', views.deleteorder, name='delete'),
    path('success/<int:order_id>/', views.successorder, name='success'),
    path('sorry/<int:order_id>/', views.sorrymsg, name='sorry')
    #path('navi/',views.navi, name='navi'),
    #path('blog/',views.blog, name='blog'),
    #path('bestseller/',views.bestseller, name='bestseller'),
    #path('category/',views.category, name='category'),
    #path('about/',views.about, name='about')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT) 
