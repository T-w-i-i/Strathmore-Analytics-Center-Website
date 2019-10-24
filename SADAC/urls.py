from django.urls import path
from . import views
from .views import HomeView, AboutView, IndustryView
from .views import contact
from django.conf.urls.static import static
from django.conf import settings

app_name = 'SADAC'
urlpatterns = [
    path('', HomeView.as_view(), name = 'home'),
    path('about/', AboutView.as_view(), name = 'about'),
    path('industry', IndustryView.as_view(), name = 'industry'),
    path('contact', contact, name = "contact"),
    path('articles', views.allblogs , name='allblogs'),
    path('<int:blog_id>/', views.detail, name="detail"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
