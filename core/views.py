from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, FormView

from .models import Module, Section


class HomePageView(ListView):
    """Página principal que lista los módulos disponibles."""

    model = Module
    template_name = "core/home.html"
    context_object_name = "modules"


class AboutPageView(TemplateView):
    """Página estática de información sobre el proyecto."""

    template_name = "core/about.html"


class ModuleDetailView(DetailView):
    """Muestra las secciones de un módulo."""

    model = Module
    template_name = "core/module_detail.html"
    context_object_name = "module"


class SectionDetailView(DetailView):
    """Muestra el contenido de una sección."""

    model = Section
    template_name = "core/section_detail.html"
    context_object_name = "section"


class SignUpView(FormView):
    """Registro de usuario."""

    template_name = "registration/signup.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
