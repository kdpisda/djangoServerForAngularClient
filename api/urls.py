"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from . import views

urlpatterns = [
    # path('profile/<profile_type>', views.profiles),
    # url(r'alumnies', views.alumnies_list),
    # url(r'students', views.students_list),
    # url(r'faculties', views.faculties_list),
    url('profile/(?P<profile_type>[\w-]+)', views.profile),
    url('section/achievements', views.achievements),
    url('section/projects', views.projects),
    url('section/activities', views.activities),
    url('section/team', views.team),
    url('section/announcements', views.announcements),
]