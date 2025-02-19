#import for randomness of traits and pairs
import random

class Matchmaker():
    '''
    -class containing all the methods to "match" all of the contestants to their "true love" given randomly assigned traits
    -once initialized nothing needs to be done
    '''

    def __init__(self, contestants):
        '''
        initializes the contestant pairs and assigns their traits
        '''

        #initialize th econtestants passed through
        self.contestants = list(contestants)
        
        #generate the pairs
        self.pairs = self.generate_pairs()
        
        #create a dictionary for name: trait mappings
        self.pair_traits = dict()

        #for every pair give them random similarities (at most 2 differences)
        for pair in self.pairs:

            self.give_similarities(pair)
        

    def generate_pairs(self):
        '''
        randomly generate pairs given the differnet names 
        '''

        #empty list for pairs
        pairs = []

        #iterate for 8 pairs
        for i in range(8):
            
            #randomly select 2 people and remove them from the contestant list so they can't be picked again
            person1 = self.contestants.pop(random.randrange(len(self.contestants)))
            person2 = self.contestants.pop(random.randrange(len(self.contestants)))
            pair = (person1, person2)
            
            #add to pair list as a tupple
            pairs.append(pair)

        #return list of pair tuples
        return pairs

    def give_similarities(self, pair):
        '''
        randomly assign 4 similar traits to the matches but at most 2 differences
        '''

        #break up the tuple so individuals can have different traits
        person1, person2 = pair

        #randomly get two numbers to decide which traits to make different
        random_trait1 = random.randint(1, 6)
        random_trait2 = random.randint(1, 6)


        #make the birth month different
        if random_trait1 == 1 or random_trait2 == 1:
            
            month1 = self.birth_month()
            month2 = self.birth_month()

        #keep birth month the same
        else:

            month1 = self.birth_month()
            month2 = month1
        
        #make favorite hobby different
        if random_trait1 == 2 or random_trait2 == 2:
            
            hobby1 = self.fav_hobby()
            hobby2 = self.fav_hobby()

        #keep favorite hobby the same
        else:

            hobby1 = self.fav_hobby()
            hobby2 = hobby1
        
        #make favorite color different
        if random_trait1 == 3 or random_trait2 == 3:
            
            color1 = self.fav_color()
            color2 = self.fav_color()

        #keep favorite color the same
        else:

            color1 = self.fav_color()
            color2 = color1
        
        #make favorite season different
        if random_trait1 == 4 or random_trait2 == 4:
            
            season1 = self.fav_season()
            season2 = self.fav_season()

        #keep favorite season the same
        else:

            season1 = self.fav_season()
            season2 = season1

        #make favorite movie genre different 
        if random_trait1 == 5 or random_trait2 == 5:
            
            movie_genre1 = self.fav_movie_genre()
            movie_genre2 = self.fav_movie_genre()

        #keep favorite movie genre the same
        else:

            movie_genre1 = self.fav_movie_genre()
            movie_genre2 = movie_genre1

        #make favorite music genre different
        if random_trait1 == 6 or random_trait2 == 6:
            
            music_genre1 = self.fav_music_genre()
            music_genre2 = self.fav_music_genre()
        
        #keep favorite music genre the same
        else:
            
            music_genre1 = self.fav_music_genre()
            music_genre2 = music_genre1
        
        #assign each person a key value mapping of the traits that was selected for them
        self.pair_traits[person1] = f'{month1}\n{hobby1}\n{color1}\n{season1}\n{movie_genre1}\n{music_genre1}'
        self.pair_traits[person2] = f'{month2}\n{hobby2}\n{color2}\n{season2}\n{movie_genre2}\n{music_genre2}'

    def birth_month(self):
        '''
        return a random birth month
        '''

        #possible months
        months = ['January', 'February', 'March',
                  'April', 'May', 'June',
                  'July', 'August', 'September',
                  'October', 'November', 'December']
        
        #random index for the list of months
        chosen_month = random.randrange(len(months))

        #return a string giving more description to the trait chosen
        return f'They were born in {months[chosen_month]}'

    def fav_hobby(self):
        '''
        return a random hobby
        '''

        #possible hobbies
        hobbies = ['Playing Video Games', 'Running', 'Watching TV',
                   'Building Legos', 'Collecting Cards', 'Swimming',
                   'Going To The Gym', 'Reading', 'Writing',
                   'Dancing', 'Singing', 'Playing An Instrument']
        
        #random index for the list of hobbies
        chosen_hobby = random.randrange(len(hobbies))

        #return a string giving more description to the trait chosen
        return f'They like {hobbies[chosen_hobby]}'
    
    def fav_color(self):
        '''
        return a random color
        '''

        #possible colors
        colors = ['Red', 'Green', 'Blue',
                  'Yellow', 'Orange', 'Indigo',
                  'Violet', 'Grey', 'Purple',
                  'Teal', 'Brown', 'Turquoise']
        
        #random index for the chosen color
        chosen_color = random.randrange(len(colors))

        #return a string giving more description to the trait chosen
        return f'Their favorite color is {colors[chosen_color]}'

    def fav_season(self):
        '''
        return a random season
        '''

        #possible seasons
        seasons = ['Winter', 'Spring', 'Summer', 'Fall']
        
        #random index for the chosen season
        chosen_season = random.randrange(len(seasons))

        #return a string giving more description to the trait chosen
        return f'Their favorite season is {seasons[chosen_season]}'

    def fav_movie_genre(self):
        '''
        return a random movie genre
        '''

        #possible movie genres
        movie_genres = ['Action', 'Comedy', 'Horror',
                        'Romance', 'Thriller', 'Sports',
                        'Documentary', 'Animation', 'Crime']

        #random index for the chosen genre
        chosen_movie_genre = random.randrange(len(movie_genres))

        #return a string giving more description to the trait chosen
        return f'They like watching {movie_genres[chosen_movie_genre]} movies'

    def fav_music_genre(self):
        '''
        return a random music genre
        '''

        #possible music genres
        music_genres = ['Rock', 'Pop', 'Classical',
                        'Country', 'LOFI', 'Video Game',
                        'Hip Hop', 'Rap', 'Metal']

        #random index for the chosen genre
        chosen_music_genre = random.randrange(len(music_genres))

        #return a string giving more description to the trait chosen
        return f'They like listening to {music_genres[chosen_music_genre]} music'
    
