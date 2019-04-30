import unittest
from comdb.main import rotten_ratings

OMDB_TEST = { 'Title': 'FOSS',
              'Year': '2016',
              'Rated': 'PG',
              'Released': '',
              'Runtime': '',
              'Genre': '',
              'Director': '',
              'Writer': '',
              'Actors': '',
              'Plot': '',
              'Language': '',
              'Country': '',
              'Awards': '',
              'Ratings': [{'Source': 'Internet Movie Database', 'Value': '7.3/10'},
                          {'Source': 'Rotten Tomatoes', 'Value': '77%'},
                          {'Source': 'Metacritic', 'Value': '62/100'}],
              'Metascore': '',
              'imdbRating': '',
              'imdbVotes': '',
              'imdbID': '',
              'Type': 'movie',
              'DVD': '',
              'BoxOffice': '',
              'Production': '',
              'Website': '',
              'Response': 'True'}

class TestRotten(unittest.TestCase):

    def test_rotten_equals(self):
        self.assertEqual(rotten_ratings(OMDB_TEST), "FOSS 77%", "Expected FOSS 77%")


if __name__ == '__main__':
    unittest.main()
