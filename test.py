# @author: ak
# @since: 22.3.2023
# @version: 1.0
# @change: ak

import random
import string
import unittest

def generate_password():
    nouns = ['omena','dinosaurus','pallo','paahdin','vuohi','lohikäärme',
            'vasara','sorsa','panda','puhelin','banaani','opettaja']

    adjectives = ['uninen', 'hidas', 'haiseva', 'märkä', 'lihava', 'punainen', 
                'oranssi', 'keltainen', 'vihreä','sininen', 'purppura', 
                'pörröinen','valkoinen', 'leuhka', 'uljas']

while True:

    # valitaan satunnaisesti adjectives listalta
    adjective = random.choice(adjectives)

    # valitaan satunnaisesti nouns listalta
    noun = random.choice(nouns)

    # satunnainen numero väliltä 0...99
    number = random.randrange(0, 100)
    special_char= random.choice(string.punctuation)

    # rakennetaan salasana
    password = adjective + noun + str(number) + special_char

    print(' Uusi salasanasi on: %s' % password)

    # response = input("Haluatko toisen salasanan? Vastaa k tai e ")

    # if response == 'e':

    # break

    # else:
    return password

class TestGeneratePassword(unittest.TestCase) :
    def test_generate_password_success(self) :
        actual = len(generate_password())
        expected = [11,12,13,14,15,16,17,18,19,20]
        print('actual= ',actual)
        self.assertIn(actual,expected)
