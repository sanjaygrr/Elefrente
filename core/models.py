from django.db import models

# Modelos para la estructura de aprendizaje


class Module(models.Model):
    """Representa un módulo de aprendizaje (A1, A2, B1, etc.)."""

    name = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Section(models.Model):
    """Secciones dentro de un módulo (Gramática, Vocabulario, etc.)."""

    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name="sections")
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="sections/images/", blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    resource = models.FileField(upload_to="sections/resources/", blank=True, null=True)

    class Meta:
        ordering = ["module", "title"]

    def __str__(self):
        return f"{self.module} - {self.title}"
