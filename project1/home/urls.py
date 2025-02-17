
from django.urls import path
from home.views import index, contact ,dynamic_routing,about

urlpatterns = [
    path('', index),
    path('contact/',contact),
    path('dynamic/<number>', dynamic_routing),
    path('about/', about),

]