
from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView

urlpatterns = [
    path('bootstrap/',TemplateView.as_view(template_name='bootstrap/example.html')),
    path('admin/', admin.site.urls),
    path('items/',include('web_page.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('social/', include('allauth.urls')),
    path('social-auth/', include('social_django.urls', namespace="social")),
    path('tweets/',include('tweets.urls'))
]
