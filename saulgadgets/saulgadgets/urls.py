
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.contrib.auth import views

from apps.cart.webhook import webhook
from apps.cart.views import cart_detail,success
from apps.core.views import frontpage,contact,about
from apps.store.views import product_detail,category_detail,search
from apps.userprofile.views import signup,myaccount

from apps.coupon.api import api_can_use
from apps.store.api import api_add_to_cart,api_remove_to_cart,api_checkout,create_checkout_session

from .sitemaps import StaticViewSitemap,CategorySitemap,ProductSitemap

sitemaps={'static':StaticViewSitemap,'product':ProductSitemap,'category':CategorySitemap}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',frontpage,name="frontpage"),
    path('search/',search,name="search"),
    path('cart/',cart_detail,name='cart'),
    path('hooks/',webhook,name='webhook'),
    path('cart/success/',success,name='success'),
    path('contact/',contact,name="contact"),
    path('about/',about,name="about"),

    # Auth
    path('myaccount/',myaccount,name="myaccount"),
    path('signup/',signup,name="signup"),
    path('login/',views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',views.LogoutView.as_view(),name='logout'),

    path('sitemap.xml',sitemap,{'sitemaps':sitemaps},name='django.contrib.sitemaps.views.sitemaps'),

    # API
    path('api/can_use/',api_can_use,name="api_can_use"),
    path('api/create_checkout_session/',create_checkout_session,name="create_checkout_session"),
    path('api/add_to_cart/',api_add_to_cart,name='api_add_to_cart'),
    path('api/remove_from_cart/',api_remove_to_cart,name='api_remove_to_cart'),
    path('api/checkout/',api_checkout,name='api_checkout'),

    # Store

    path('<slug:category_slug>/<slug:slug>/',product_detail,name="product_detail"),
    path('<slug:slug>/',category_detail,name="category_detail"),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
