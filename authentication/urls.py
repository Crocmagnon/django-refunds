from django.conf.urls import url
from django.contrib.auth.views import login, logout, password_change
from authentication.views import password_change_done

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
    url(r'^password/change/$', password_change, {'template_name': 'authentication/change_password.html'}, name='password_change'),
    url(r'^password/change/done/$', password_change_done, name='password_change_done'),
]
