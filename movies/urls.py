from django.conf.urls import url

from movies.views import MoviesOfCollectionView

urlpatterns = [url("test/", view=MoviesOfCollectionView.as_view(), name="index")]
