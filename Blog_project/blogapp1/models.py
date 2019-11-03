from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    body = models.TextField()

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e, %Y')

    def __str__(self):
        return self.title

class Showdata(models.Model):
    bookno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    author=models.CharField(max_length=30)
    file=models.FilePathField()
    price=models.FloatField(max_length=20)
    date=models.DateField()

'''class Post(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField()
    author = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return f'{self.text} ~ {self.author}'

class Like(models.Model):
    user = models.ForeignKey('User')
    post = models.ForeignKey(Post)
    timestamp = models.DateTimeField()

    def __str__(self):
            return f'{self.user.username} likes \'{self.post.text}\ '''