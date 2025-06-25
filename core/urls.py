from django.urls import path

from .views import (
    LandingPageView,
    ModulesListView,
    AboutPageView,
    ContactPageView,
    ModuleDetailView,
    SectionDetailView,
    SignUpView,
)

urlpatterns = [
    path("", LandingPageView.as_view(), name="home"),
    path("modulos/", ModulesListView.as_view(), name="modules"),
    path("quienes-somos/", AboutPageView.as_view(), name="about"),
    path("contacto/", ContactPageView.as_view(), name="contact"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("modulo/<int:pk>/", ModuleDetailView.as_view(), name="module_detail"),
    path("seccion/<int:pk>/", SectionDetailView.as_view(), name="section_detail"),
] 