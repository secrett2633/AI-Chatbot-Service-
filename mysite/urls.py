from django.contrib import admin
from django.urls import include, path, re_path

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
    re_path(r'^webpush/', include('webpush.urls'))
]