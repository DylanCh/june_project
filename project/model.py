from django.db import models
from django.conf import settings
class Record(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1)
    title = models.CharField(max_length=120)
    slug = model.SlugField(max_length=120, unique=True)
    image = models.ImageField(upload_to='records')
    content = models.TextField()
    draft = models.BooleanField(default=False)
    updated = mdoel.DateField(auto=True,auto_now_add=False)
    published = models.DateField(auto_now=False,auto_now_add=True)

    class Meta:
        ordering = ['-published']
    
    def _str_(self):
        return self.title

    def _unicode_(self):
        return str(self.title)

