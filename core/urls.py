from django.urls import path

from .views import (
    HomePageView,
    AboutPageView,
    ModuleDetailView,
    SectionDetailView,
    SignUpView,
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("quienes-somos/", AboutPageView.as_view(), name="about"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("modulo/<int:pk>/", ModuleDetailView.as_view(), name="module_detail"),
    path("seccion/<int:pk>/", SectionDetailView.as_view(), name="section_detail"),
] 