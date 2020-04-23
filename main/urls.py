#
# Copyright (c) 2019- Representable Team (Theodor Marcu, Lauren Johnston, Somya Arora, Kyle Barnes, Preeti Iyer).
#
# This file is part of Representable
# (see http://representable.org).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
from django.urls import include, path

from . import views
from representable.settings.base import MAPBOX_KEY

app_name = "main"
urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("timeline/", views.Timeline.as_view(), name="timeline"),
    path("map/", views.Map.as_view(), name="map"),
    path("thanks/", views.Thanks.as_view(), name="thanks"),
    path("entry/", views.EntryView.as_view(), name="entry"),
    path("main/", views.MainView.as_view(), name="main_test"),
    path("about/", views.About.as_view(), name="MeetTheTeam"),
    path("review/", views.Review.as_view(), name="review"),
    path("privacy/", views.Privacy.as_view(), name="privacy"),
    path("terms/", views.Terms.as_view(), name="terms"),
    path("submission/", views.Submission.as_view(), name="submission"),
    path("partners/create/", views.CreateOrg.as_view(), name="create_org"),
    path(
        "partners/<slug:slug>-<int:id>/",
        include(
            [
                path("thanks/", views.ThanksOrg.as_view(), name="thanks_org"),
                path("", views.HomeOrg.as_view(), name="home_org"),
                path("edit/", views.EditOrg.as_view(), name="edit_org"),
                path(
                    "upload/whitelist",
                    views.WhiteListUpdate.as_view(),
                    name="upload_whitelist",
                ),
            ]
        ),
    ),
]
