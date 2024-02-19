# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4
#
# Copyright (C) 2015-2017 GEM Foundation
#
# OpenQuake is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# OpenQuake is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with OpenQuake. If not, see <http://www.gnu.org/licenses/>.

from django.urls import re_path
from openquakeplatform_taxtweb import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

app_name = 'taxtweb'
urlpatterns = [
    re_path(r'^explanation(?P<taxonomy>[^?]*)',
            views.explanation, name='explanation'),
    re_path(r'^checker(?P<taxonomy>[^?]*)', views.checker, name='checker'),
    re_path(r'^(?P<taxonomy>[^?]*)', views.index, name='index'),
    re_path('', views.index, name='home'),
]
