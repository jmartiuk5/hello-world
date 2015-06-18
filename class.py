class Song(object):

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line



def _init_(self, lyrics):
        self.lyrics = lyrics


happy_bday = Song(["Happy birthday to you", "I dont want to get sued", "So i'll stop right there"])

bulls_on_parade = Song(["they rally around the family",
                        "with a pocket full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()