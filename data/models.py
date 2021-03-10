from django.db import models

# Create your models here.
class Data(models.Model):
    nama = models.CharField(max_length=30)
    nim = models.CharField(max_length=10)
    alamat = models.TextField()
    status = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True)
    def __str__(self):
        return "{}.{}".format(self.id, self.nama)
