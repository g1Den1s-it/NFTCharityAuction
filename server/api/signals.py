from django.db.models.signals import post_save
from django.dispatch import receiver
from api.models import NetworkTransaction, Auction, RewardList
from eth_user.models import User


@receiver(post_save, sender=NetworkTransaction)
def handler_transaction_for_auction(sender, instance, created, **kwargs):
    if created:
        try:
            user = User.objects.get(public_key=instance.to_address)
            auction = Auction.objects.get(wallet=instance.to_address)

            donation = int(instance.value) / 10 ** 18

            auction.collected += donation
            auction.save()

            tickets = donation / auction.min_price

            RewardList.objects.create(
                user=user,
                transaction_block=instance,
                auction=auction,
                ticket=tickets
            ).save()

        except Auction.DoesNotExist:
            print(f"No Auction found with this wallet: {instance.to_address}")
