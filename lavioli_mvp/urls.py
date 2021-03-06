from django.conf.urls import url, include
from django.contrib import admin

import lavioli_mvp.views 
import team.views 

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r"^$", lavioli_mvp.views.home, name="home"),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^dashboard$', team.views.dashboard, name='dashboard'),
    url(r'^create_team$', team.views.create_team, name='create_team'),
    url(r'^invite_user$', team.views.invite_user, name='invite_user'),    
    url(r'^plan$', team.views.plan, name='plan'),    
    url(r'^team/(?P<id>\d+)$', team.views.team_info, name='team_info'),
    url(r'^myteam/(?P<id>\d+)$', team.views.myteam_info, name='myteam_info'),
    url(r'^update_account$', team.views.update_account, name='update_account'),
    url(r'^add_service/(?P<id>\d+)$', team.views.add_service, name='add_service'),
    url(r'^add_service_real/(?P<s_name>.+)/(?P<t_id>\d+)$', team.views.add_service_real, name='add_service_real'),
    url(r'^remove_service$', team.views.remove_service, name='remove_service'),
    url(r'^remove_member$', team.views.remove_member, name='remove_member'),
    url(r'^accept_invitation/(?P<m_id>\d+)/(?P<t_id>\d+)$', team.views.accept_invitation, name='accept_invitation'),
    url(r'^charge_account$', team.views.charge_account, name='charge_account'),
    url(r'^cancel_account$', team.views.cancel_account, name='cancel_account'),    
    url(r'^stripe_webhook$', team.views.stripe_webhook, name='stripe_webhook'),    
]
