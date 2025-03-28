import pymongo

from typing import List, Optional

from app.model.book import Book

"""
Δημιουργούμε ένα μοναδικό αντικείμενο για αυτή τη κλάσση. Ο τρόπος που το δημιουργούμε είναι βασισμένος σε ένα pattern που ονομάζεται Singlenton Pattern.
Το πολύ γνωστή βιβλίο Design Patterns: Elements of Reusable Object-Oriented Software (1994) που έχει γραφτεί από τους συγγραφείς  Erich Gamma, Richard Helm, Ralph Johnson, και John Vlissides (γνωστούς και ως Gang of Four) είναι το πρώτο βιβλίο που χρησιμοποιεί design patterns για σχεδιασμό λογισμικού.
"""
class Repository:
    _instance = None  # Repository object


    @classmethod
    def instance(cls):
        """
        Κάθε φορά που θέλουμε να χρησιμοποιήσουμε ένα αντικείμενο τύπου Repository δεν θα φτιάχνουμε καινούργιο, αλλά θα χρησιμοποιείται αυτό που έχει ήδη δημιουργηθεί την πρώτη φορά. Για τον λόγο αυτό θα καλούμε τη συνάρτηση instance() της κλάσης.
        """
        if cls._instance is None:
            cls._instance = cls.__new__(cls)  # Create the object
            client = pymongo.MongoClient("localhost", 27017)
            cls._instance.db = client["bookstore"]  # Set the db attribute
        return cls._instance


    def __init__(self) -> None:
        """
        Αυτή η υλοποίηση δεν επιτρέπει στον προγραμματιστή να δημιουργήσει νέο αντικείμενο από τον constructor της python.  
        """
        raise RuntimeError('Call instance() instead')

    def get_books(self, from_index:Optional[str]=None, to_index:Optional[str]=None)-> list[Book]:
        '''
        Args:
            from_index (str | None): Δείκτης για να ξεκινήσει η αναζήτηση
            to_index (str | None): Δείκτης για να ολοκληρωθεί η αναζήτηση
        Returns:
            List[Book]: Λίστα με βιβλία. 
        '''
        if from_index is not None and to_index is not None:
            # TODO Υλοποιήστε μηχανισμό ώστε να επιστρέφει κατάλληλο μήνυμα όταν το from_index είναι μεγαλύτερο από το to_index ή όταν υπάρχει 
            # αρνητικός αριθμός.
            # ...
            results = self.db["books"].find()[int(from_index):int(to_index)]
        else:
            results = self.db["books"].find()
        books:list[Book] = []  # Exercise
        for r in results:
            books.append(Book.from_dict(r))
        return books
    
    def get_book_by_id(self, id:str) -> Book | None:
        result = self.db["books"].find_one({"id":id})
        if len(list(result)) > 0:
            return Book.from_dict(result)
        return None

    def get_books_by_author(self, name:str) -> List[Book]:
        # Να βρίσκει όλα τα βιβλία που ο συγγραφέας έχει ακριβώς το ίδιο όνομα με το name.
        pass

    def get_books_by_title(self, title:str)-> List[Book]:
        # Ο τίτλος να περιέχεται στο βιβλίο. Πχ να επιστρέφει όλα τα βιβλία που στον τίτλο περιέχεται
        # η λέξη "Plastic". Η συνάρτηση δεν είναι case sensitive.
        pass

    def get_books_by_genre(self, genre:str) -> List[Book]:
        # Να βρίσκει τα βιβλία που περιέχουν στο attribute genre την τιμή της παραμέτρου genre.
        # Παράδειγμα genre="Non-fiction" και το genre κάποιου βιβλίου είναι "Non-fiction,Romance novel"
        pass

    def get_books_by_rating(self, min_r:float, max_r:float) -> List[Book]:
        # Να είναι μεταξύ του [min_r και max_r).
        pass

    def get_books_by_date(self, from_date:int, to_date:int)-> List[Book]:
        # Να είναι μεταξύ του [from_date και to_date).
        pass

    def get_books_by_items(self, max_items:Optional[int], min_items:Optional[int]) -> List[Book]:
        # Να είναι μεταξύ του [min_items και max_items].
        pass
    
    def get_books_by_comments(self, comments_min:int, comments_max:int) -> List[Book]:
        # Να είναι μεταξύ του [comments_min και comments_max).
        pass

    def add_book(self, book_dict:dict) -> str:
        pass

    def update_items(self, book_id:str, new_items:int) -> None:
        pass

    def update_price(self, book_id:str, new_price:float) -> None:
        pass
        

