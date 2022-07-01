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
        self.guest3 = Guest("Daria", 50, "Dirty Dancing")

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
        self.room1.increase_revenue(self.room1.entry_fee)
        self.assertEqual(10, self.room1.revenue)

    def test_favourite_song_in_song_in_ist(self):
        self.room1.add_song(self.song1)
        self.room1.add_song(self.song2)
        self.room1.check_in(self.guest2)
        self.assertEqual(["Nathan says Whoo!"],
                         self.room1.check_for_fav_songs())

    def test_someone_does_not_have_favourite_song_in_list(self):
        self.room1.add_song(self.song1)
        self.room1.add_song(self.song2)
        self.room1.check_in(self.guest1)
        self.assertEqual([],
                         self.room1.check_for_fav_songs())

    def test_multiple_people_have_favourite_songs_in_list(self):
        self.room1.add_song(self.song1)
        self.room1.add_song(self.song2)
        self.room1.check_in(self.guest2)
        self.room1.check_in(self.guest3)
        self.assertEqual(["Nathan says Whoo!", "Daria says Whoo!"],
                         self.room1.check_for_fav_songs())
