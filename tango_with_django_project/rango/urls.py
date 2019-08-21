app_name = "rango"
from django.conf.urls import url
from rango import views

app_name = "rango"
urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(
        r"^category/(?P<category_name_slug>[\w\-]+)/$",
        views.show_category,
        name="category",
    ),
    url(r"^greet/$", views.greet, name="greet"),
    url(r"^add_category/$", views.add_category, name="add_category"),
    url(r"^register/$",views.register,name="Register"),
    url(r"^login/$",views.user_login,name="Login"),
    url(r"^logout/$",views.user_logout,name="logout")
]
