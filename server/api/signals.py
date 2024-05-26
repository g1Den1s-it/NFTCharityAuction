from django.db.models.signals import post_save
from django.dispatch import receiver
from api.models import NetworkTransaction, Auction


@receiver(post_save, sender=NetworkTransaction)
def handler_transaction_for_auction(sender, instance, created, **kwargs):
    if created:
        try:
            auction = Auction.objects.get(wallet=instance.to_address)
            auction.collected += (int(instance.value) / 10 ** 18)
            auction.save()

        except Auction.DoesNotExist:
            print(f"No Auction found with this wallet: {instance.to_address}")
