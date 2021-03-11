"""snippetmaster URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.urls import include, path
from core import views
from core.views import SearchResultsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(), name= 'accounts-login'),
    path('', views.snippet_list, name="home"),
    path('user_home/', views.homepage_render, name="user-home"),
    path('snippets/new', views.add_snippet, name = 'add-snippet'),
    path('snippets/<int:pk>/edit', views.edit_snippet, name="edit-snippet"),
    path('snippets/<int:pk>/delete', views.delete_snippet, name="delete-snippet"),
    path('submitted/', views.snippet_user_submitted, name="submitted"),
    path('search/', SearchResultsView.as_view(), name='search-results'),
    path('network_feed/', views.user_list, name="network_feed"),
    path('user_list/', views.user_list_count, name="user-list-count"),
    path('snippets/<int:pk>/save', views.save_snippet, name="save-snippet"),
    path('snippets/<int:pk>/added', views.save_snippet , name="snippet-added"),
    path('userprofile/<int:pk>/', views.indivdual_user, name="userprofile"),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
