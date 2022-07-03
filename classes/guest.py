class Guest:
    def __init__(self, _name, _wallet, _favourite_song):
        self.name = _name
        self.wallet = _wallet
        self.favourite_song = _favourite_song
        self.purchased = []

    def pay_entry(self, room):

        if self.wallet > room.entry_fee:
            self.wallet -= room.entry_fee

        elif self.wallet <= room.entry_fee:
            return "You don't have enough funds bro"
