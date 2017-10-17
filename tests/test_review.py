import unittest
from app.models import Review

class ReviewTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Review class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        
        self.new_review = Review(12345,'Review for movies',"https://image.tmdb.org/t/p/w500/jdjdjdjn",'This movie is the best thing since sliced bread')

    def tearDown(self):
        '''
        Using clear_reviews method to delete reviews from all_reviews list
        '''
        Review.clear_reviews()

    def test_instance(self):
        self.assertTrue( isinstance( self.new_review, Review) )

    def test_init(self):
        '''
        Test initialisation of Review class
        '''
        self.assertEqual( self.new_review.movie_id, 12345)
        self.assertEqual( self.new_review.title, 'Review for movies')
        self.assertEqual( self.new_review.imageurl, "https://image.tmdb.org/t/p/w500/jdjdjdjn")
        self.assertEqual( self.new_review.review, 'This movie is the best thing since sliced bread')

    def test_save_review(self):
        '''
        Test if reveiws are saving
        '''
        self.new_review.save_review()

        # self.assertEqual( len(Review.all_reviews) , 1)
        self.assertTrue( len(Review.all_reviews) > 0)

    def test_get_reviews(self):
        '''
        Test if reviews for a specific movie gotten by the id
        '''
        self.new_review.save_review()

        test_review = Review(67890, 'Review for Why', "https://image.tmdb.org/t/p/w500/ghighighi", 'The aswesome Why on a journey')
        test_review.save_review()

        gotten_reviews = Review.get_reviews(67890)

        # self.assertEqual( len(gotten_reviews), 1)
        self.assertTrue( len(gotten_reviews) == 1)
