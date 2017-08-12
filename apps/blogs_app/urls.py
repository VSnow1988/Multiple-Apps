from django.conf.urls import url #this gives us access to the function url
from . import views #this imports views.py from the current folder. Python documents to be imported don't need the file ending here.

#Very similar to setting an @app.route in Flask. The r'^$' is a regex that tells Python to interpret the following as a raw string so it won't escape special characters.
#the second parameter here runs a function from the views document.
urlpatterns = [
    url(r'^new$', views.new), #name a subroute and give it a method(view) to run.
    url(r'^{{number}}$', views.show),
    url(r'^{{number}}/edit$', views.show),
    url(r'^{{number}}/delete$', views.destroy),
    url(r'^create$', views.create),
  ]
