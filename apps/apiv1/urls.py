from django.conf.urls import url, include
from rest_framework_jwt.views import verify_jwt_token, refresh_jwt_token, obtain_jwt_token

urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^auth/', obtain_jwt_token),
    url(r'^refresh/', refresh_jwt_token),
    url(r'^verify/', verify_jwt_token),

]