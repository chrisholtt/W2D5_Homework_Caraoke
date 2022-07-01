class Guest:
    def __init__(self, _name, _wallet, _favourite_song):
        self.name = _name
        self.wallet = _wallet
        self.favourite_song = _favourite_song

    def pay_entry(self, room):
        self.wallet -= room.entry_fee
        room.revenue += room.entry_fee

    def find_my_song(self, room):
        for song in room.song_list:
            if song.name == self.favourite_song:
                return "Whoo"
        return "My favourite song is not here"
