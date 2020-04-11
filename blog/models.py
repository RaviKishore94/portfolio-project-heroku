from django.db import models

class Blog(models.Model):
	title = models.CharField(max_length=100)
	pub_date = models.DateTimeField()
	body = models.TextField()
	image = models.ImageField(upload_to='images/')

	def __str__(self):
		return self.title

	def body_pretty(self):
		if len(self.body)>50:
			return self.body[:50]+'...'
		else:
			return self.body

	def pub_date_pretty(self):
		return self.pub_date.strftime('%b %d %Y')