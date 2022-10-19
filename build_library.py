'''
Library take two!
Follow the instructions below to fill out the missing parts of the Library class in library.py, 
then test each method in this file.
NOTE: ALL methods for the Library class go in the library.py script
'''

# 1.0 TODO: Import the Library class


# 2.1 TODO: In `library.py`:
#   Write the 'constructor' method of the Library class to have one attribute `books`, an empty list.
#   This function does not need any parameters other than self.


# 2.2 TODO: In this file:
#   Create an instance of the `Library` class called `my_library`.


# 2.3 TODO: In this file:
#   Print the `books` attribute of `my_library`. It should be an empty list.


# 2.4 TODO: In this file:
#   Also print out the `type` of `my_library` and the `type` of its `books` attribute


# 3.1 TODO: In `library.py`:
#   Fill out the `add()` method to add a book to an instance of the Library class.
#   - The method should take two parameters (other than self): `title` and `author`, both strings
#   - The method should create a `Book` object (it's already imported into the file) with those two attributes
#   - Then, the method should append this book to the `books` attribute of the `Library` object


# 3.2 TODO: In this file:
#   Once you have finished writing the `add_title()` method above, add the following books to your library:
#
#       The Body Keeps the Score - Bessel van der Kolk
#       Sapiens - Yuval Noah Harari
#       Braiding Sweetgrass - Robin Wall Kimmerer
#       The Warmth of Other Suns - Isabel Wilkerson


# 3.3 TODO: Print the `books` attribute of my_library again to make sure your books have been added.


# 3.4 TODO: Huh. That looks a little weird... Loop through the `books` attribute and print each
#   one out separately instead.


# 4.1 TODO: In `library.py`:
#   Fill out the `count_books` method to get the number of books in an instance of the `Library` class.
#   - The method should only take in the `self` parameter, no others
#   - The method should return the length of the `books` attribute as an integer


# 4.2 TODO: In this script:
#   Once you have finished the method, count the books in my_library and print out the result


# 5.1 TODO: In `library.py`:
#   Fill out the `remove_title` method to remove a book (by title) from an instance of the Library class.
#   - The method should take an additional parameter `title`, the title of the book to be removed
#   - The method should remove all books matching the input title from the `Library` instance.
#       NOTE: We know a `list` method that does something like this, but will it remove ALL matching books?
#   - The method does not need to return anything


# 5.2 TODO: In this script:
#   Once you have finished the method, remove 'Braiding Sweetgrass' from `my_library`.


# 5.3 TODO: In this script:
#   Repeat the loop you wrote in 3.4 to check if it worked.


# We've now used that loop twice, and any time we want to see the titles in our library,
#   we'll probably want to use it again. That tells us something: the loop code is a pretty good
#   candidate to turn into a method of the `Library` class. So let's do it!

# 6.1 TODO: In `library.py`:
#   Create a new method called `display_books`.
#   - This method should not take in any additional parameters (beyond `self`).
#   - Move your loop into this method, and edit the variable names so that it refers directly 
#       to the `books` attribute
#   - This method should not return anything


# 6.2 TODO: In this file:
#   This time, call your library's `display_books` method to see if it works.


# 7.1 TODO: In this script:
#   Instantiate another instance of the `Library` class called `nyt_bestsellers`


# 7.2 TODO: In this script:
#   Add two books of your choosing from the New York Times best sellers lists to nyt_bestsellers using the .add_title() method
#   You can find NYT books here: https://www.nytimes.com/books/best-sellers/


# 7.3 TODO: In this script:
#   Call the `display_books` method on the `nyt_bestsellers` Library object.


# BONUS .1 TODO: In `library.py`
#   Update the `display_books` method to sort the books in alphabetical order firs
#   NOTE: There is a quick way to sort a list in Python, google it!
#   Run this file again to see if it changed the output!
