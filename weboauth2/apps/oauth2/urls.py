from django.conf.urls import url

from . import views
from .views.api import v1

# API endpoints
urlpatterns = [
    url(r'^api/v1/ping/$', v1.ping_view),
    url(r'^api/v1/authorized-user-info/$', v1.get_user_view),
    url(r'^api/v1/token-info/$', v1.get_access_token),
]

# OAuth2 provider endpoints
urlpatterns += [
    url(
        r'^o/application-choose/$',
        views.ApplicationChooseView.as_view(),
        name='application-choose'
    ),
    url(
        r'^o/application/(?P<client_id>[0-9A-Za-z]{,40})/choose/confirm/$',
        views.ApplicationChooseConfirm.as_view(),
        name='application-choose-confirm'
    ),
    url(
        r'^o/redirect-to-authorize/(?P<pk>\d+)/$',
        views.RedirectToAuthorizationView.as_view(),
        name='redirect-to-authorize'
    ),
    url(
        r'^o/application/(?P<pk>\d+)/scope-not-found/$',
        views.ScopeNotFoundView.as_view(),
        name='application-scope-not-found'
    ),

    url(
        r'^o/authorize/$',
        views.AuthorizationView.as_view(),
        name="authorize"
    ),
    url(
        r'^o/token/$',
        views.TokenView.as_view(),
        name="token"
    ),
    url(
        r'^o/revoke-token/$',
        views.RevokeTokenView.as_view(),
        name="revoke-token"
    ),
]

# OAuth2 Application Management endpoints
urlpatterns += [
    url(
        r'^applications/$',
        views.ApplicationList.as_view(),
        name="application_list"
    ),

    url(
        r'^applications/register/$',
        views.ApplicationRegistration.as_view(),
        name="application_register"
    ),

    url(
        r'^applications/(?P<pk>\d+)/$',
        views.ApplicationDetail.as_view(),
        name="application_detail"
    ),

    url(
        r'^applications/(?P<pk>\d+)/delete/$',
        views.ApplicationDelete.as_view(),
        name="application_delete"
    ),

    url(
        r'^applications/(?P<pk>\d+)/update/$',
        views.ApplicationUpdate.as_view(),
        name="application_update"
    ),
]
