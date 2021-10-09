from django.urls import path
from main.views import detail, main, signup, signin, signout, cart, contact, cartAdd, cartRem, get_by_category, sendMessage



urlpatterns = [
    path("", main, name="main"),
    path("cart/", cart, name="cart"),
    path("contact/", contact, name="contact"),

    path("signup/", signup, name="signup"),
    path("signout/", signout, name="signout"),
    path("signin/", signin, name="signin"),

    path("detail/<int:pk>", detail, name="detail"),

    path("cartAdd/<int:pk>", cartAdd, name='cartAdd'),
    path("cartRem/<int:pk>", cartRem, name='cartRem'),

    path("getByCat/<int:pk>", get_by_category, name="getByCat"),

    path("sendMessage/", sendMessage, name="sendMessage"),
]
