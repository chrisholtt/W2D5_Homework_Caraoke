import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song


class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room1 = Room("Disco room", 5, 10)
        self.room2 = Room("Rock room", 10, 10)

        self.guest1 = Guest("Christopher", 50, "Billie Jean")
        self.guest2 = Guest("Nathan", 50, "She Wolf")

        self.song1 = Song("Dirty Dancing")
        self.song2 = Song("She Wolf")

    def test_room_has_name(self):
        self.assertEqual("Disco room", self.room1.room_name)

    def test_room_has_capacity(self):
        self.assertEqual(5, self.room1.capacity)

    def test_room_has_entry_fee(self):
        self.assertEqual(10, self.room1.entry_fee)

    def test_can_check_in_guest(self):
        self.room1.check_in(self.guest1)
        self.assertEqual([self.guest1], self.room1.guest_list)

    def test_can_check_out_guest(self):
        self.room1.check_in(self.guest1)
        self.room1.check_out(self.guest1)
        self.assertEqual([], self.room1.guest_list)

    def test_can_add_song_to_room(self):
        self.room1.add_song(self.song1)
        self.assertEqual([self.song1], self.room1.song_list)

    def test_when_room_is_full(self):
        self.room1.check_in(self.guest1)
        self.room1.check_in(self.guest1)
        self.room1.check_in(self.guest1)
        self.room1.check_in(self.guest1)
        self.room1.check_in(self.guest1)
        self.assertEqual("Room is full, please try another room",
                         self.room1.check_in(self.guest1))

    def test_revenue_increases(self):
        self.guest1.pay_entry(self.room1)
        self.assertEqual(10, self.room1.revenue)

    def test_favourite_song_in_song_list(self):
        self.room1.check_in(self.guest2)
        self.room1.add_song(self.song1)
        self.room1.add_song(self.song2)
        self.assertEqual("Whoo", self.guest2.find_my_song(self.room1))

    def test_favourite_song_is_not_in_list(self):
        self.room2.add_song(self.song1)
        self.room2.add_song(self.song2)
        self.assertEqual("My favourite song is not here",
                         self.guest1.find_my_song(self.room1))
