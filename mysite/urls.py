from django.contrib import admin
from django.urls import include, path, re_path

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    re_path(r'^webpush/', include('webpush.urls'))
]