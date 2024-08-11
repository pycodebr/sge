from django.db import models


class AIResult(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    result = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']
