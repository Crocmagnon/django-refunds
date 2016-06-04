from authentication.views import password_change_done
from django.conf.urls import url
from django.contrib.auth.views import login, logout, password_change

urlpatterns = [
    url(
        r'^login/$',
        login,
        {
            'template_name': 'authentication/auth_form.html',
            'extra_context': {
                'title': 'Login',
                'action': 'Login'
            }
        },
        name='auth_login'
    ),
    url(
        r'^logout/$',
        logout,
        {'next_page': 'home'},
        name='auth_logout'
    ),
    url(
        r'^password/change/$',
        password_change,
        {
            'template_name': 'authentication/auth_form.html',
            'extra_context': {
                'title': 'Change password',
                'action': 'Change password'
            }
        },
        name='password_change'
    ),
    url(r'^password/change/done/$', password_change_done, name='password_change_done'),
]
