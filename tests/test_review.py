import unittest
from app.models import Review,User
from app import db

class ReviewTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Review class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.user_James = User( username = "James", password = "potato", email = "james@ms.com" )

        self.new_review = Review(movie_id = 12345, movie_title = 'Review for movies', image_path = "https://image.tmdb.org/t/p/w500/jdjdjdjn", movie_review = 'This movie is the best thing since sliced bread', user = self.user_James)

    def tearDown(self):
        '''
        Using query.delete to delete elements in the database after each test
        '''
        Review.query.delete()
        User.query.delete()

    def test_instance(self):
        self.assertTrue( isinstance( self.new_review, Review) )

    def test_check_instance_variables(self):
        '''
        Test initialisation of Review class
        '''
        self.assertEqual( self.new_review.movie_id, 12345)
        self.assertEqual( self.new_review.movie_title, 'Review for movies')
        self.assertEqual( self.new_review.image_path, "https://image.tmdb.org/t/p/w500/jdjdjdjn")
        self.assertEqual( self.new_review.movie_review, 'This movie is the best thing since sliced bread')
        self.assertEqual( self.new_review.user, self.user_James)


    def test_save_review(self):
        '''
        Test if reveiws are saving
        '''
        self.new_review.save_review()

        # self.assertEqual( len(Review.query.all()) , 1)
        self.assertTrue( len(Review.query.all()) > 0)

    def test_get_reviews(self):
        '''
        Test if reviews for a specific movie gotten by the id
        '''
        self.new_review.save_review()

        test_review = Review(movie_id = 67890, movie_title = 'Review for Why',  image_path = "https://image.tmdb.org/t/p/w500/ghighighi", movie_review = 'The aswesome Why on a journey', user = self.user_James)
        test_review.save_review()

        gotten_reviews = Review.get_reviews(67890)

        # self.assertEqual( len(gotten_reviews), 1)
        self.assertTrue( len(gotten_reviews) == 1)





