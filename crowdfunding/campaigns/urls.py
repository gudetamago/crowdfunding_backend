from django.urls import path
from . import views
 
urlpatterns = [
    path('campaigns/', views.CampaignList.as_view()),
    path('campaigns/<int:pk>/', views.CampaignDetail.as_view()),
    path('pledges/', views.PledgeList.as_view()),
    # path('pledges/<int:pk>/', views.PledgeDetail.as_view()),
    path('stretches/<int:pk>/', views.StretchList.as_view()),
]