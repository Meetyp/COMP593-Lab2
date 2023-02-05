def main():

    student_info = {
        'full_name' : 'Meet Patel',
        'student_id' : 10274542,
        'pizza_toppings' : [
            'TOMATO',
            'GREEN PEPPER',
            'ONION'
        ],
        'movies' : [
            {
                'title' : 'money heist', # student_info['movies'][0]['title']
                'genre' : 'heist'        # student_info['movies'][0]['genre']
            },
            {
                'title' : 'the return of rebel', # student_info['movies'][1]['title']
                'genre' : 'action'               # student_info['movies'][1]['genre']
            }
        ]
    }

    # Add another movie
    student_info['movies'].append({'title' : 'mr. robot', 'genre' : 'techno-thriller'})

    print_student_info(student_info)
    print_toppings(student_info)
    add_topping(student_info, ('mushroom', 'roasted garlic', 'brushetta'))
    print_toppings(student_info)
    print_movie_genres(student_info)
    print_movies(student_info)

    return

def print_movies(movie_list):

    print(f"Some of my favourite movies are ", end='')

    for i, name in enumerate(movie_list['movies']):
        if i < len(movie_list['movies']) - 1:
            print(name['title'].title(), end=', ')
        else:
            print("and " + name['title'].title(), end='!\n\n')

    return

def print_movie_genres(movie):

    print(f"I like to watch ", end='')

    for i, film in enumerate(movie['movies']):
        if i < len(movie['movies']) - 1:
            print(film['genre'], end=', ')
        else:
            print("and " + film['genre'], end=' movies.\n\n')

    return

def print_toppings(topping_info):

    print("My favourite pizza toppings are:")

    toppings = [t for t in topping_info['pizza_toppings']]

    for t in toppings:
        print(f'-{t}')

    print()
    
    return

def add_topping(s_info, new_topping):

    s_info['pizza_toppings'].extend(new_topping)

    for i, pt in enumerate(s_info['pizza_toppings']):
        s_info['pizza_toppings'][i] = pt.lower()

    s_info['pizza_toppings'].sort()

def print_student_info(info):

    full_name = info['full_name'].title()
    first_name = info['full_name'].split()
    student_id = info['student_id']
    print(f'\nMy name is {full_name}, but you can call me Mr. {first_name[0]}.')
    print(f'My student ID is {student_id}.\n')

    return

if __name__ == '__main__':
    main()
