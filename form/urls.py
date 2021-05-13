from django.conf.urls import url
from . import views


urlpatterns = [
    url(
        r'^api/v1/forms/(?P<pk>[0-9]+)$',
        views.get_delete_update_forms,
        name='get_delete_update_forms'
    ),
    url(
        r'^api/v1/forms/$',
        views.get_post_forms,
        name='get_post_forms'
    )
]