from django.urls import path
from . import views
urlpatterns = [

    path('details/<int:id>', views.DetailPostView.as_view(), name = "detail_view"),
    path('purchase_car/<int:id>', views.purchase_car, name = "purchase_car"),
    
]
