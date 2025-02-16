import random

lENGHT = 35

                            #Book Object
#-----------------------------------------------------------------
class book:
    def __init__(self, title, author, year_published, description, rating):
        self.title = title
        self.author = author
        self.year_published = year_published
        self.description = description
        self.rating = rating

    def __str__(self):
        return f"{self.title}\nby {self.author}, published in {self.year_published}\nRating: {self.rating}\n\n{self.description}\n"
    
                        #Program Fucntions
#-----------------------------------------------------------------
#Main menu
def menu():
    for count in range(lENGHT):
        print("-", end="")
    print()
    print("Pick your favorite fiction genre")
    print("\n 0. Exit\n 1. Mystery\n 2. Fantasy\n 3. Thriller\n 4. Romance")
    print(" 5. Science Fiction\n 6. Horror\n 7. Adventure\n 8. Dystopain\n")

    for count in range(lENGHT):
        print("-", end="")
    print()

#Random Number Engine
def random_int():
    return random.randint(0, 3)

def text_files(genre, file_name):
    with open(f"Python/Book_Recommendation/Books/{genre}/{file_name}", 'r') as file:
        file_contents = file.read()
    return file_contents
                        #Book genres Functions
#-----------------------------------------------------------------
#Mystery Genre
def mystery():
    mystery_books = []
    novel_one = book("Gone Girl", "Gillian Flynn", 2012, text_files("Mystery", "GoneGirl.txt"), "9.8/10" )
    mystery_books.append(novel_one)

    novel_two = book("House of Leaves", "Mark Z. Danielewski", 2000, text_files("Mystery", "HouseOfLeaves.txt"), "9.1/10")
    mystery_books.append(novel_two)

    novel_three = book("The Paper Palace", "Miranda Cowley Heller", 2021, text_files("Mystery", "ThePaperPalace.txt"), "8/10")
    mystery_books.append(novel_three)

    novel_four = book("The Girl on the Train", "Paula Hawkins", 2015, text_files("Mystery", "TheGirlOnTheTrain.txt"), "7.5/10")
    mystery_books.append(novel_four)

    #Random Book picker
    results = random_int()
    book_rec = mystery_books[results]
    return book_rec
#-----------------------------------------------------------------
#Fantasy Genre
def fantasy():
    fantasy_books = []
    novel_one = book("The Hobbit", "J.R.R. Tolkien", 1937, text_files("Fantasy", "TheHobbit.txt"), "8.3/10" )
    fantasy_books.append(novel_one)

    novel_two = book("The Way of Kings", "Brandon Sanderson", 2010, text_files("Fantasy", "TheWayOfKings.txt"), "9.5/10")
    fantasy_books.append(novel_two)

    novel_three = book("A Song of Ice and Fire", "George R.R. Martin", 1996, text_files("Fantasy", "ASongOfIceAndFire.txt"), "9/10" )
    fantasy_books.append(novel_three)

    novel_four = book("Between Two Fires", "Christopher Buehlman", 2019, text_files("Fantasy", "BetweenTwoFires.txt"), "7.2/10")
    fantasy_books.append(novel_four)

    #Random Book picker
    results = random_int()
    book_rec = fantasy_books[results]
    return book_rec
#-----------------------------------------------------------------
#Thriller Genre
def thriller():
    thriller_books = []
    novel_one = book("The Silent Patient", " Alex Michaelides", 2019, """
A psychological thriller about a woman who shoots her husband 
and then stops speaking. A psychotherapist becomes obsessed 
with unraveling the mystery behind her silence.""", "8.7/10" )
    thriller_books.append(novel_one)

    novel_two = book("The Last House on Needless Street", "Catriona Ward", 2021, """
A psychological horror thriller about a man who lives in isolation 
at the edge of a forest. As the story unfolds, hidden truths emerge,
and the boundaries between reality and illusion blur.""", "9.8/10")
    thriller_books.append(novel_two)

    novel_three = book("The Outsider", "Stephen King", 2018, """
A compelling crime thriller with supernatural elements, following a 
brutal murder investigation where the evidence points to an upstanding 
citizen, but strange circumstances suggest something more sinister.""", "7/10" )
    thriller_books.append(novel_three)

    novel_four = book("Shutter Island", "Dennis Lehane", 2003, """
Set in a mental institution on a remote island, this psychological 
thriller follows U.S. Marshal Teddy Daniels as he investigates the 
disappearance of a patient. As he digs deeper, reality begins to unravel, 
and he questions everything around him.""", "8.4/10")
    thriller_books.append(novel_four)

    #Random Book picker
    results = random_int()
    book_rec = thriller_books[results]
    return book_rec
    
#-----------------------------------------------------------------
#Romance Genre
def romance():
    romance_books = []
    novel_one = book("Yours Truly", " Abby Jimenez", 2023, """
A heartfelt romance about Briana, who finds comfort and healing 
in Jacob, a kind-hearted man she meets at work. As they bond over 
shared struggles, their connection grows, offering both love and 
a second chance at happiness.""", "9.5/10" )
    romance_books.append(novel_one)

    novel_two = book("It Ends with Us", "Colleen Hoover", 2016, """
A powerful and emotional romance that follows Lily Bloom, who falls 
in love with a man named Ryle. As the relationship grows, Lily must 
navigate the complexities of love, loyalty, and painful personal history.""", "9/10")
    romance_books.append(novel_two)

    novel_three = book("Beach Read", "Emily Henry", 2020, """
Two authors, January and Gus, struggling with writer's block, 
swap genres and spend the summer challenging each other. 
What starts as a professional agreement blooms into a 
romance full of humor, vulnerability, and emotional depth.""", "Unread" )
    romance_books.append(novel_three)

    novel_four = book("Icebreaker", "Hannah Grace", 2022, """
Anastasia, a figure skater, and Nate, a hockey player, are 
forced to share the ice at college. What starts as rivalry 
turns into a fiery romance filled with humor, chemistry, 
and emotional depth. (Waringing very Smutty)""", "8.5/10")
    romance_books.append(novel_four)

    #Random Book picker
    results = random_int()
    book_rec = romance_books[results]
    return book_rec

#-----------------------------------------------------------------
#Scienece Fiction Genre
def science():
    science_books = []
    novel_one = book("Dune", "Frank Herbert", 1965, """
A sweeping epic set on the desert planet of Arrakis, Dune 
explores themes of politics, religion, and ecology, following 
Paul Atreides as he navigates the struggle for control of 
the planet's spice, a powerful resource.""", "9/10" )
    science_books.append(novel_one)

    novel_two = book("Altered Carbon", "Richard K. Morgan", 2002, """
A gritty cyberpunk noir set in a future where consciousness 
can be transferred between bodies. Altered Carbon follows 
ex-soldier Takeshi Kovacs as he investigates a wealthy man's 
apparent suicide. It's a fast-paced, action-packed mystery 
with existential themes.""", "8.1/10")
    science_books.append(novel_two)

    novel_three = book("Project Hail Mary", "Andy Weir", 2021, """
A gripping science fiction novel that follows Ryland Grace, 
a lone astronaut who wakes up on a spaceship with no memory 
of who he is or how he got there. He learns that he's on a 
mission to save humanity from an extinction-level threat. 
The story blends hard science, problem-solving, and humor.""", "9.3/10" )
    science_books.append(novel_three)

    novel_four = book("The Left Hand of Darkness", "Ursula K. Le Guin", 1969, """
Set on the planet Gethen, The Left Hand of Darkness is one of 
the most influential works in science fiction, addressing themes 
of gender, power, and identity. It's a slow-burn exploration of 
cultural differences and the complexities of human nature.""", "9/10")
    science_books.append(novel_four)

    #Random Book picker
    results = random_int()
    book_rec = science_books[results]
    return book_rec

#-----------------------------------------------------------------
#Horror Genre
def horror():
    horror_books = []
    novel_one = book("The Fisherman", "John Langan", 2016, """
A dark, slow-burn horror novel about two widowers who take up 
fishing to cope with their grief, only to find themselves drawn 
into a supernatural and malevolent force lurking in the waters. 
It blends folk horror with psychological terror.""", "7.9/10" )
    horror_books.append(novel_one)

    novel_two = book("The Haunting of Hill House", "Shirley Jackson", 1959, """
A chilling novel about a group of people who spend time in the 
eerie Hill House, where one of them begins to experience terrifying 
supernatural phenomena. It's a masterclass in psychological horror 
and tension.""", "9/10")
    horror_books.append(novel_two)

    novel_three = book("The Stand", "Stephen King", 1978, """
A post-apocalyptic novel about the remnants of humanity struggling 
to survive after a plague wipes out most of the population. 
It's a grand, sweeping narrative about good versus evil, 
with unforgettable characters and an eerie sense of dread.""", "9.3/10" )
    horror_books.append(novel_three)

    novel_four = book("The People Under the Stairs", "Paul G. Tremblay", 2017, """
A couple living in a secluded mansion holds a dark and horrifying 
secret. The novel is full of unsettling twists, with themes of fear, 
paranoia, and the horrors that can be hidden beneath the surface 
of seemingly normal lives.""", "7.9/10")
    horror_books.append(novel_four)

    #Random Book picker
    results = random_int()
    book_rec = horror_books[results]
    return book_rec

#-----------------------------------------------------------------
#Adventure Genre
def adventure():
    adventure_books = []
    novel_one = book("The Secret Garden", "Frances Hodgson Burnett", 1911, """
While not traditionally an "adventure" in the action-packed sense, 
this novel follows Mary Lennox as she uncovers a hidden, magical 
garden and embarks on a journey of emotional and personal transformation.""", "7.5/10" )
    adventure_books.append(novel_one)

    novel_two = book("A Wrinkle in Time", "George Orwell", 1949, """
A chilling portrayal of a totalitarian regime that uses surveillance, 
mind control, and language manipulation to maintain power. 
1984 explores themes of freedom, oppression, and the consequences 
of absolute control.""", "8.6/10")
    adventure_books.append(novel_two)

    novel_three = book("Hatchet", "Gary Paulsen", 1987, """
A story of survival, Hatchet follows 13-year-old Brian Robeson, who 
is stranded in the Canadian wilderness after a plane crash. Alone 
and without any survival gear, Brian must learn to live off the land. 
It's a compelling tale of determination and personal growth.""", "7/10" )
    adventure_books.append(novel_three)

    novel_four = book("The Odyssey", "Homer", "Circa 8th Century BC", """
In this epic poem, Odysseus embarks on a ten-year voyage back home from 
the Trojan War, encountering gods, monsters, and other challenges along 
the way. One of the most famous adventure stories of all time, The Odyssey 
is a cornerstone of Western literature""", "9.1/10")
    adventure_books.append(novel_four)

    #Random Book picker
    results = random_int()
    book_rec = adventure_books[results]
    return book_rec

#-----------------------------------------------------------------
#Dystopian Genre
def dystopian():
    dystopian_books = []
    novel_one = book("The Handmaid's Tale", "Margaret Atwood", 1985, """
In a dystopian future, women have been stripped of their rights and forced 
into servitude. The Handmaid's Tale is a powerful critique of patriarchy, 
reproductive rights, and the dangers of a theocratic state.""", "8.9/10" )
    dystopian_books.append(novel_one)

    novel_two = book("1984", "Madeleine L'Engle", 1962, """
Meg Murry and her brother Charles embark on an extraordinary adventure 
through time and space to rescue their father. A Wrinkle in Time is a 
science fantasy adventure that mixes adventure with themes of love, 
courage, and destiny.""", "9.5/10")
    dystopian_books.append(novel_two)

    novel_three = book("The Giver", "Lois Lowry", 1993, """
In a world where emotions, choices, and memories are suppressed for the 
greater good, Jonas is selected to inherit the role of "Receiver" of 
memories. The book explores the consequences of a perfectly controlled 
society.""", "8/10" )
    dystopian_books.append(novel_three)

    novel_four = book("The Man in the High Castle", "Philip K. Dick", 1962, """
In an alternate history where the Axis powers won World War II, the U.S. 
is divided between Japan and Nazi Germany. This mind-bending novel explores 
alternate realities, authoritarian regimes, and the nature of reality itself.""", "8.2/10")
    dystopian_books.append(novel_four)

    #Random Book picker
    results = random_int()
    book_rec = dystopian_books[results]
    return book_rec

#-----------------------------------------------------------------
#Main Program

def main():

    print("Welcome to the book recommendation program")
    exit = False
    while exit == False:
        menu()

        user_choice = int(input("Enter number of your selection: "))
        while (user_choice > 8 and user_choice < 1):
            user_choice = input("(INVALID) Enter number of your selection: ")
        
        if user_choice == 0:
            exit = True

        if user_choice == 1:
            print()
            book_rec = mystery()
            print(book_rec)
            print()

        elif user_choice == 2:
            print()
            book_rec = fantasy()
            print(book_rec)
            print()
    
        elif user_choice == 3:
            print()
            book_rec = thriller()
            print(book_rec)
            print()
        
        elif user_choice == 4:
            print()
            book_rec = romance()
            print(book_rec)
            print()

        elif user_choice == 5:
            print()
            book_rec = science()
            print(book_rec)
            print()

        elif user_choice == 6:
            print()
            book_rec = horror()
            print(book_rec)
            print()

        elif user_choice == 7:
            print()
            book_rec = adventure()
            print(book_rec)
            print()

        elif user_choice == 8:
            print()
            book_rec = dystopian()
            print(book_rec)
            print()
        
        #Chekc if user hasn't already tried to exit
        #Then ask the user if they want to contuine the program
        if exit != True:
            again = input("would you like another book recommendation (y/n): ")
            if ((again.upper() == "Y") or (again.upper() == "YES")):
                exit = False
            else:
                exit = True
main()