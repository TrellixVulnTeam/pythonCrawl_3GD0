from django.conf.urls import include
from django.urls import path, re_path
from django.views.generic import TemplateView
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

import xadmin
from api.views import LoginViewset, UserViewset, AdminUserViewset, DayOrderViewset, RandomPWD, \
    UserAttrViewsets, UserBelongViewset
from qmf_api.views import QmfOrderViewsets, GenerateCodeViewsets, UpOrderViewsrts, AddOrderViewsets, StatisticsViewsets, \
    PaymentViewsets

router = DefaultRouter()
# router.register(r'order', OrderViewset, base_name='order')
# router.register(r'order1', PeaceBankOrderViewsets, base_name='order1')
router.register(r'dayorder', DayOrderViewset, base_name='dayorder')
# router.register(r'monthorder', MonthOrderViewset, base_name='monthorder')
router.register(r'login', LoginViewset, base_name='login')
router.register(r'users', UserViewset, base_name='users')
router.register(r'adminuser', AdminUserViewset, base_name='adminuser')
router.register(r'RandomPWD', RandomPWD, base_name='RandomPWD')
router.register(r'qmf_order', QmfOrderViewsets, base_name='qmf_order')
router.register(r'gcode', GenerateCodeViewsets, base_name='gcode')
router.register(r'uporder', UpOrderViewsrts, base_name='uporder')
router.register(r'addorder', AddOrderViewsets, base_name='addorder')
router.register(r'statistics', StatisticsViewsets, base_name='statistics')
router.register(r'payment', PaymentViewsets, base_name='payment')
router.register(r'userattr', UserAttrViewsets, base_name='userattr')
router.register(r'userbelong', UserBelongViewset, base_name='userbelong')

urlpatterns = [
    path('admin/', xadmin.site.urls),
    path('api/', include(router.urls)),
    path('docs/', include_docs_urls(title='API 与 狗', description='young api')),
    re_path('', TemplateView.as_view(template_name='index.html'), name='index'),

]
