from django.db import models


class Myapp(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    is_enable = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True, blank=True)
    published_date = models.DateTimeField(null=True)

    def __str__(self):
        # return self.title
        return '{}-{}'.format(self.pk, self.title)


class Comment(models.Model):
    Myapp = models.ForeignKey(Myapp, on_delete=models.CASCADE)
    text = models.TextField(blank=True)
    pub_date = models.DateTimeField(null=True)
    updated = models.DateTimeField(auto_now=True)


