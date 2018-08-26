from django.urls import path
from . import views
from django.conf.urls import url, include
from rest_framework import routers
# from vue_rest_experiment.data_app import views

app_name = 'data_app' # for namespacing


router = routers.DefaultRouter()
router.register(r'sets', views.SetViewSet)
router.register(r'cards', views.CardViewSet)
router.register(r'images', views.ImageViewSet)
router.register(r'scores', views.ScoreViewSet)



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
app_name = 'data_app' # for namespacing
urlpatterns = [
	# path('', views.index, name='index'),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
