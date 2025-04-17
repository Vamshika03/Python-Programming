1.Syntax
my_list = [1, 5, 10, 15, 20]
print(my_list)

print([True, False, False, "1"])

2.List constructor
my_list = list(["Lists", "are", "useful!"])
print(my_list)

3.List comprehension
my_list = [num for num in range (1,6)]
print(my_list)

4.Indexing single elements
my_list = [num for num in range (1,6)]
print(my_list)

element = my_list[2]
print(element)

5.Indexing portions of the list
#my_list = [num for num in range (1,6)]//
#my_list[start:end]

my_list = [1, 5, 10, 15, 20, 25, 30, 35, 40]
my_new_list = my_list[2:5]

print(my_new_list)

6.Negative indexing
my_list = [num for num in range (1,6)]

last_element = my_list[-1]
print(last_element)

7.Out of range index values
my_list = [num for num in range (1,6)]

try:
    element = my_list[10]
except IndexError:
    print("Index is out of range!")
  
7.Adding to a list
my_list = [12, 19, 26, 23]
my_list.append(30)
print(my_list)

8.The extend() method
python_datatypes = ["lists"]
python_datatypes.extend(["tuples", "sets"])
print(python_datatypes)

9.Modifying a single element
blue_shades = ['navy', 'sky blue', 'saphire', 'powder blue', 'teal', 'turquoise']
blue_shades[2] = 'sapphire'

print(blue_shades)

10.Modifying multiple elements
blue_shades = ['navy', 'sky blue', 'sapphire', 'powder blue', 'teal', 'turquoise']
blue_shades[0:2] = ['denim', 'aqua']

print(blue_shades)

11.Different number of elements than the specified range
blue_shades = ['navy', 'sky blue', 'sapphire', 'powder blue', 'teal', 'turquoise']
blue_shades[0:1] = ['denim', 'aqua']
print(blue_shades)

*blue_shades = ['navy', 'sky blue', 'sapphire', 'powder blue', 'teal', 'turquoise']
blue_shades[0:4] = ['denim', 'aqua']
print(blue_shades)

12.Reassigning a list
blue_shades = ['navy', 'sky blue', 'sapphire', 'powder blue', 'teal', 'turquoise']

blue_shades = ['cobalt', 'azure', 'ice blue']
print(blue_shades)

13.Deleting a single element
space_movies = ['Interstellar', 'Gravity', 'The Martian', 'Apollo 13', 'Star Wars']
print(space_movies)

del space_movies[2]
print(space_movies)

14.Deleting multiple elements
space_movies = ['Interstellar', 'Gravity', 'The Martian', 'Apollo 13', 'Star Wars']

del space_movies[1:3]
print(space_movies)

15.Removing by value
space_movies = ['Interstellar', 'Gravity', 'The Martian', 'Apollo 13', 'Star Wars']
print(space_movies)

space_movies.remove('Gravity')

16.Clearing the entire list
space_movies = ['Interstellar', 'Gravity', 'The Martian', 'Apollo 13', 'Star Wars']
space_movies.clear()
print(space_movies)

17.The pop() method
space_movies = ['Interstellar', 'Gravity', 'The Martian', 'Apollo 13', 'Star Wars']

removed_movie = space_movies.pop(2)
print("The removed movie is = " + removed_movie)
print(space_movies)

18.List Slicing
my_list = [1, 5, 10, 15, 20, 25, 30]
print(my_list[0:2])

*my_list = [1, 5, 10, 15, 20, 25, 30]

my_list[0:2] = 50, 55
print(my_list)

19.The step parameter
my_list = [1, 5, 10, 15, 20, 25, 30]

print(my_list[1:5:2])

20.Slicing from the beginning
my_list = [1, 5, 10, 15, 20, 25, 30]

slice_list_from_start = my_list[:4]
print(slice_list_from_start)

21.Slicing from a specific index till the end
my_list = [1, 5, 10, 15, 20, 25, 30]

slice_list_till_end = my_list[4:]
print(slice_list_till_end)

22.Negative slicing
my_list = [1, 5, 10, 15, 20, 25, 30]

last_three_elements = my_list[:-3]
print("Last three elements:", last_three_elements)

*my_list = [1, 5, 10, 15, 20, 25, 30]

skip_every_second_from_end = my_list[-1:-6:-2]
print(skip_every_second_from_end)

*my_list = [1, 5, 10, 15, 20, 25, 30]

reversed_list = my_list[::-1]
print(reversed_list)

23.Expression
numbers = [1, 2, 3, 4, 5]
squares = [num ** 2 for num in numbers]

print(squares)

24.Condition
numbers = [1, 2, 3, 4, 5]
odd_numbers = [num for num in numbers if num % 2 != 0]

print(odd_numbers)

*words = ["hoodie", "rivers", "cat", "monitor", "bag", "cup"]
short_words = [word for word in words if len(word) <= 5]

print(short_words)

25.Assignment to multiple variables
numbers = [1, 2, 3, 4, 5]
pairs = [(num, num * 2) for num in numbers]

26.Transforming elements
songs = ['Neon Lights', 'Pieces', 'Everything']
uppercase_songs = [song.upper() for song in songs]

print(uppercase_songs)

print(pairs)

27.Nested list comprehension(imp)
my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transpose = [[row[i] for row in my_matrix] for i in range(len(my_matrix[0]))]

print(transpose)


