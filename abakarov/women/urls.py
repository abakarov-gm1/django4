from django.urls import path, register_converter

from . import views, converters
register_converter(converters.FourDigitYearConverter, "year4")


urlpatterns = [
    path('', views.index, name='/'),
    path('about/', views.about, name='about'),
    path('post/<int:id>', views.posts, name='post')

]









