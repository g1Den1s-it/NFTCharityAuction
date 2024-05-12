from django.db import models
from eth_user.models import User


# Create your models here.

class MetadataNFT(models.Model):
    name = models.CharField(max_length=24)
    description = models.TextField()
    image = models.ImageField(upload_to="nft/metadata")
    # attributes
    value = models.IntegerField()

    def __str__(self):
        return self.name


class Auction(models.Model):
    name = models.CharField(max_length=124)
    description = models.TextField()
    image = models.ImageField(upload_to="auction/images")
    wallet = models.CharField(max_length=120)
    goal = models.IntegerField(default=0)
    collected = models.IntegerField(default=0)
    min_price = models.IntegerField(default=1)
    is_open = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class UserDonationAuctionTransaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    bet = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.bet)


class RewardList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    auction = models.OneToOneField(Auction, on_delete=models.PROTECT)
    chance = models.IntegerField(default=1)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.date)
