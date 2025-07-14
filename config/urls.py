"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import SignUpView, CustomLogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('', include('trip.urls')),
    path ('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', SignUpView.as_view(),  name='signup'),
    path('logout/', CustomLogoutView.as_view(next_page='login'), name='logout'),
]

#accounts/login/ [names='login']
#accounts/logout/ [name='logout']
#accounts/password_change/ [name='password_change']
#accounts/password_change/done/ [name=password_change_done']
#accounts/password_reset/ [name='password_reset']
#accounts/password_reset/done/ [name='password_reset_done']
#accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm' ]
#accounts/reset/done/ [names='password_reset_complete']
# dante-321-super user
# jay-!@#$1234-normal user

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
