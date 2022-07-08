from django.urls import path
from app import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('allhospital/', views.AllhosView.as_view(), name='allhos'),
    path('kyuukyuuhospital/', views.KyuuhosView.as_view(), name='kyuuhos'),
    path('NewsView/', views.NewsView.as_view(), name='NewsView'),
    path('blog/', views.BlogView.as_view(), name='blog'),

]