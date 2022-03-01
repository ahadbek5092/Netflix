from django.test import  TestCase, Client
from actor.models import Movie,Actor

class TestMovieviewset(TestCase):
    def setUp(self) -> None:
        self.actor = Actor.objects.create(
            name = 'testactor',
            birthday = '2022-02-02',
            gender= 'M')
        self.movie = Movie.objects.create(
            name = 'testmovie',
            year = '2022-02-02',
            imdb = 'ccc',
            genre = 'crime')
        self.movie.actors.add(self.actor)
        self.client = Client()



    def test_movies_can_list(self):
        response = self.client.get('/movies/')
        data = response.data
        self.assertEquals(len(data),1)
        self.assertEquals(data[0]['name'], 'testmovie')
        self.assertEquals(data[0]['year'], '2022-02-02')
        self.assertEquals(data[0]['imdb'], 'ccc')
        self.assertEquals(data[0]['genre'], 'crime')
        # print(data)
    def test_movie_can_search(self):
        response = self.client.get('/movies/?search=movie')
        data = response.data
        # print(data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(data), 1)
        self.assertEquals(data[0]['name'], 'testmovie')
        self.assertEquals(data[0]['year'], '2022-02-02')
        self.assertEquals(data[0]['genre'], 'crime')

    def test_movie_can_ordered(self):
        response = self.client.get('/movies/?ordering = imb')

        data = response.data
        self.assertEquals(data[0]['imdb'], 'ccc')
