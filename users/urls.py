from django.conf.urls import url
import users.views as views

urlpatterns = [
    url(r"^register/$", view=views.register_user, name="register_user"),
    url(r"^login/$", view=views.login_user, name="login"),
    url(r"^logout/$", view=views.logout_user, name="logout"),

]