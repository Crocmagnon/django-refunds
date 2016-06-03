from django.conf.urls import url
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^login/$',
        login,
        {'template_name': 'authentication/login.html'},
        name='auth_login'
        ),
    url(r'^logout/$',
        logout,
        {'next_page': 'home'},
        name='auth_logout'
        ),
]
