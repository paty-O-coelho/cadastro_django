"""pontoTel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from .views import hello
from django.urls import path, include
#mostrar as imagens em tempo de desenvolvimento (pequena gambiarra que so funciona em teste)
from django.conf import settings
from django.conf.urls.static import static
from usuarios import urls as usuarios_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello),
    path('person/',include(usuarios_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#ao final cocatena com o diretorio onde minhas imagens estão