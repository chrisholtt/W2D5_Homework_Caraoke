import unittest
from classes.guest import Guest
from classes.room import Room


class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest1 = Guest("Christopher", 50, "Billie Jean")
        self.room1 = Room("Disco room", 5, 10)

    def test_guest_has_name(self):
        self.assertEqual("Christopher", self.guest1.name)

    def test_guest_has_wallet(self):
        self.assertEqual(50, self.guest1.wallet)

    def test_guest_has_favourite_song(self):
        self.assertEqual("Billie Jean", self.guest1.favourite_song)

    def test_guest_pays_entry(self):
        self.guest1.pay_entry(self.room1)
        self.assertEqual(40, self.guest1.wallet)

    def test_guest_pays_entry(self):
        self.guest1.pay_entry(self.room1)
        self.assertEqual(40, self.guest1.wallet)
