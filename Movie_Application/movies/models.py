from django.db import models

# Create your models here.
class Movie(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField()
	body = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	thumb = models.ImageField(default='default.png',blank=True)
	videofile= models.FileField(upload_to='videos/', null=True, verbose_name="")

	def __str__(self):
		return self.title

	def snippet(self):
		return self.body[:50] + '.....'

	def video(self):
		return self.videofile