from django.urls import path
from .views import HomePageView, ContactPageView, AboutPageView, PortfolioView, OurTeamPageView, MoreView
from . import views
app_name="home"
urlpatterns = [
    path('', HomePageView.as_view(),name="home"),
    # path('portfolio/', PortfolioView.as_view(),name="portfolio"),
    path('portfolio/', views.PortfolioView, name='portfolio'),
    path('more/', MoreView.as_view(),name="more"),
    path('team/', OurTeamPageView.as_view(),name="team"),
    path('contact-us/', ContactPageView.as_view(),name="contact-us"),
    path('about/', AboutPageView.as_view(),name="about"),
]