from django.urls import include, re_path

from . import views


urlpatterns = [

    re_path( r'^$', 
             views.TestingHomeView.as_view(), 
             name='testing_home'),

    re_path( r'^ui/', include('jt.testing.ui.urls' )),
    re_path( r'^devtools/', include('jt.testing.devtools.urls' )),

]
