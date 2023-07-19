from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("category", views.category, name="category"),
    path("category/<str:key>", views.category_second, name="category2"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("create", views.creator, name="creator"),
    path("open/<int:number>", views.open, name="open"),
    path("open/comment", views.add_comment, name="comment"),
    path("Pdelete", views.page_delete, name="Pdelete"),
    path("Wadd", views.watchlist_add, name="Watch+"),
    path("Wdel", views.watchlist_delete, name="Watch-"),
    path("mine", views.mine_list, name="mine"),
    path("end", views.ending, name="ending"),
    path("check", views.checking, name="check"),
    path("bid", views.biding, name="bid"),
    path("witch", views.witching, name="witch")
]
