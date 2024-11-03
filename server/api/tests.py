from django.test import TestCase
from rest_framework.test import APIClient, APITestCase
from api.models import Auction
from eth_user.models import User
# Create your tests here.


class APITestCaseView(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin_user = User.objects.create_superuser(
            username='admin',
            password='admin',
            public_key='0x2134dw1q1e23asd2e413w12s2e231d212ds12dd3w1'
        )
        self.admin_user.save()

    def test_static_data(self):
        res = self.client.get("/api/v1/statistic/")

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data, {
            "users": 1,
            "gifted_nfts": 0,
            "closed_auctions": 0,
            "money_collected": 0
        })


class RetrieveAPIViewAuctionTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin_user = User.objects.create_superuser(
            username='admin',
            password='admin',
            public_key='0x2134dw1q1e23asd2e413w12s2e231d212ds12dd3w1'
        )
        self.auction = Auction.objects.create(
            name="test-auction",
            description="testing...",
            image="img.png",
            wallet="0x31232131",
            goal=100,
            is_open=True,
            owner=self.admin_user,
            min_price=4
        )
        self.auction.save()

    def test_retrieve_auction_view(self):
        res = self.client.get(f"/api/v1/auction/{self.auction.id}/")


        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data["id"], self.auction.id)
        self.assertEqual(res.data["name"], self.auction.name)
        self.assertEqual(res.data["description"], self.auction.description)
        self.assertEqual(res.data["image"], f"http://testserver{self.auction.image.url}")
        self.assertEqual(res.data["goal"], self.auction.goal)
        self.assertEqual(res.data["collected"], self.auction.collected)
        self.assertEqual(res.data["wallet"], self.auction.wallet)
        self.assertEqual(res.data["min_price"], self.auction.min_price)
        self.assertEqual(res.data["owner"], self.auction.owner.id)
        self.assertEqual(res.data["date"], str(self.auction.date))

