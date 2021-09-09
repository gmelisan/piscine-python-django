from django.db import models
from django.contrib.auth.models import User

class Upvote(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class Downvote(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class Tip(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    upvotes = models.ManyToManyField(Upvote)
    downvotes = models.ManyToManyField(Downvote)


    def vote(self, user, up):
        upvoted = self.upvotes.filter(author=user).exists()
        downvoted = self.downvotes.filter(author=user).exists()
        
        if up:
            if upvoted:
                self.upvotes.get(author=user).delete()

            if downvoted:
                self.downvotes.get(author=user).delete()
                self._add_upvote(user)
            
            if not upvoted and not downvoted:
                self._add_upvote(user)
                
        else: # down
            if downvoted:
                self.downvotes.get(author=user).delete()
                
            if upvoted:
                self.upvotes.get(author=user).delete()
                self._add_downvote(user)
            
            if not upvoted and not downvoted:
                self._add_downvote(user)
                

    def _add_upvote(self, user):
        v = Upvote(author=user)
        v.save()
        self.upvotes.add(v)

        
    def _add_downvote(self, user):
        v = Downvote(author=user)
        v.save()
        self.downvotes.add(v)
