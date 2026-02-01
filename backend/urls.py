from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from app.views import (
    ResgisterView,
    ProfileView,
    ProductCreateView,
    CategoryWiseProductView,
    CategoryCreateView,
   
)

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),

    path("register/", ResgisterView.as_view()),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("profile/", ProfileView.as_view()),

    path("products/create/", ProductCreateView.as_view()),
    path("products/category-wise/", CategoryWiseProductView.as_view()),
    path("categories/create/", CategoryCreateView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
