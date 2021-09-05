from rest_framework import routers
from api import views as rental_views

# router de DRF, va gerer les differents url du api
router = routers.DefaultRouter()

# url pour l'app rental
router.register(r'friends',rental_views.FriendViewset)
router.register(r'belongings', rental_views.BelongingViewset)
router.register(r'borrowings', rental_views.BorrowedViewset)