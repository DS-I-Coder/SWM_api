from django.urls import path,include,re_path

app_name = 'theapp'
urlpatterns = [
    path('', include('rest_framework.urls', namespace='rest_framework_category')),
]