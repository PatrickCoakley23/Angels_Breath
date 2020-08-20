from django.db import models
from profiles.models import UserProfile

# Create your models here.


class Whiskey_club(models.Model):
    name = models.CharField(max_length=254)
    comment = models.CharField(max_length=254)
    description = models.TextField()
    tasting_notes = models.TextField()
    rating = models.DecimalField(max_digits=6, decimal_places=2,
                                 null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Subscription_type(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2,
                                null=True, blank=True)
    whiskey_clubs = models.ManyToManyField(
        Whiskey_club,
        through='Subscriptions',
        related_name="whiskey_clubs"
    )
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Subscriptions(models.Model):
    class Meta:
        verbose_name_plural = "Subscriptions"

    user_profile = models.ForeignKey(UserProfile,
                                     on_delete=models.CASCADE,
                                     null=True)
    whiskey_club = models.ForeignKey(Whiskey_club, on_delete=models.CASCADE,
                                     related_name="club_subs")
    subscription_type = models.ForeignKey(Subscription_type,
                                          on_delete=models.CASCADE,
                                          related_name="club_subs")

    def __str__(self):
        return f'{self.user_profile}_{self.subscription_type.name}_on_{self.whiskey_club.name}'
