import unittest
from models import movie

Movie = movie.Movie

class MovieTest(unittest.TestCase):
    '''
    Test class to test the behaviours of Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''

        self.new_movie = Movie(1234,'Python Must Be Crazy','A thrilling new Python Series','/khsjha27hbs',8.5,129993)

    def test_instance(self):
        '''
        Test the instance of Movie class
        '''

        self.assertTrue( isinstance( self.new_movie, Movie) )

    def test_init(self):
        '''
        Test initalisation of Movie class
        '''

        self.assertEqual( self.new_movie.id, 1234)
        self.assertEqual( self.new_movie.title, 'Python Must Be Crazy' )
        self.assertEqual( self.new_movie.overview, 'A thrilling new Python Series' )
        self.assertEqual( self.new_movie.image, '/khsjha27hbs' )
        self.assertEqual( self.new_movie.vote_average, 8.5 )
        self.assertEqual( self.new_movie.vote_count, 129993 )

if __name__ == '__main__':
    unittest.main()
