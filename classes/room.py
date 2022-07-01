class Room:
    def __init__(self, _room_name, _capacity, _entry_fee):
        self.room_name = _room_name
        self.capacity = _capacity
        self.entry_fee = _entry_fee
        self.guest_list = []
        self.song_list = []
        self.revenue = 0.0

    def check_in(self, guest):
        if len(self.guest_list) >= self.capacity:
            return "Room is full, please try another room"
        else:
            self.guest_list.append(guest)

    def check_out(self, guest):
        self.guest_list.remove(guest)

    def add_song(self, song):
        self.song_list.append(song)

    def increase_revenue(self, amount):
        self.revenue += amount

    # def check_for_fav_songs(self):
    #     for guest in self.guest_list:
    #         for song in self.song_list:
    #             if guest.favourite_song == song.name:
    #                 return "My fav song is here"
    #     return "My fav song is not here"

    def check_for_fav_songs(self):
        woos = []
        for guest in self.guest_list:
            for song in self.song_list:
                if guest.favourite_song == song.name:
                    woos.append(f"{guest.name} says Whoo!")
        return woos
