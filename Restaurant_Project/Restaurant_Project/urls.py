"""
URL configuration for Restaurant_Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from Base_App.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HomeView,name="Home"),
    path('about',AboutView,name="About"),
    path('menu',MenuView,name="Menu"),
    path('book_table',BookTableView,name="Book_Table"),   
    path('feedback',FeedbackView,name="Feedback_Form"),
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT) 
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)