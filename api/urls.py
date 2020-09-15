from rest_framework.routers import DefaultRouter

from api.views import ProductSetModelViewSet, RecipientModelViewSet, EditRecipientAddressViewSet, \
    EditRecipientSurnameViewSet

router = DefaultRouter()
router.register('set', ProductSetModelViewSet, basename='set')
router.register('recipient', RecipientModelViewSet, basename='recipient')
router.register('edit_address', EditRecipientAddressViewSet, basename='edit_address')
router.register('edit_surname', EditRecipientSurnameViewSet, basename='edit_surname')
urlpatterns = router.urls
