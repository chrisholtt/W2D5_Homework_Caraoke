import unittest
from classes.song import Song


class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Billie Jean")

    def test_song_has_name(self):
        self.assertEqual("Billie Jean", self.song.name)
