"""techtest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from techtest.articles.views import ArticleView, ArticlesListView
from techtest.regions.views import RegionView, RegionsListView
from techtest.authors.views import AuthorView, AuthorsListView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("articles/", ArticlesListView.as_view(), name="articles-list"),
    path("articles/<int:article_id>/", ArticleView.as_view(), name="article"),
    path("articles/create/", ArticleView.as_view(), name="article-create"),
    path("articles/<int:article_id>/update/", ArticleView.as_view(), name="article-update"),
    path("articles/<int:article_id>/delete/", ArticleView.as_view(), name="article-delete"),

    path("regions/", RegionsListView.as_view(), name="regions-list"),
    path("regions/<int:region_id>/", RegionView.as_view(), name="region"),
    path("regions/create/", RegionView.as_view(), name="region-create"),
    path("regions/<int:region_id>/update/", RegionView.as_view(), name="region-update"),
    path("regions/<int:region_id>/delete/", RegionView.as_view(), name="region-delete"),

    path("authors/", AuthorsListView.as_view(), name="authors-list"),
    path("authors/<int:author_id>/", AuthorView.as_view(), name="author"),
    path("authors/create/", AuthorView.as_view(), name="author-create"),
    path("authors/<int:author_id>/update/", AuthorView.as_view(), name="author-update"),
    path("authors/<int:author_id>/delete/", AuthorView.as_view(), name="author-delete"),
]
