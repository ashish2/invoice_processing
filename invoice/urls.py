"""plateiq URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
# router.register(r'invoice/', views.InvoiceViewSet)

router.register(r'invoice', views.InvoiceViewSet, basename="invoice")
router.register(r'vendor', views.VendorViewSet, basename="vendor")
router.register(r'purchaser', views.PurchaserViewSet, basename="purchaser")
router.register(r'invoicedetails', views.InvoiceDetailsViewSet, basename="invoicedetails")
router.register(r'lineitems', views.LineItemsViewSet, basename="lineitems")
router.register(r'invoice_otherstatus', views.Invoice_OtherStatusViewSet, basename="invoice_otherstatus")
# router.register(r'invoice', views.InvoiceViewSet)

urlpatterns = [
    # path('invoice/', include('invoice.urls')),

    # path('admin/', admin.site.urls),
    # path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls) )
]