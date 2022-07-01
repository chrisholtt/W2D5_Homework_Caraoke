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
