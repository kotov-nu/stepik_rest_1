from django.contrib import admin
from django.urls import path

from api.views import get_recipients, get_recipient, get_food_boxes, get_box


urlpatterns = [
    path('admin/', admin.site.urls),
    path('recipients/', get_recipients),
    path('recipients/<int:recipient_pk>/', get_recipient),
    path('boxes/', get_food_boxes),
    path('boxes/<int:box_pk>/', get_box),
]
