MENU_PROMPT = 'Enter "c" To Create Blog, "l" To List Blogs, "r" To Read One, "p" To Create Post, "q" To Quit: '

blogs = dict()

def menu():
    print_blogs()

    selection = input(MENU_PROMPT)

    while selection != 'q':
        if selection == 'c':
            ask_create_blog()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            ask_read_blog()
        elif selection == 'p':
            ask_create_post()
        selection = input(MENU_PROMPT)

def print_blogs():
    for key, blog in blogs.items():
        print('- {}'.format(blog))

def ask_create_blog():
    pass

def ask_read_blog():
    pass

def ask_create_post():
    pass