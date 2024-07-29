
def return_title(seed_name: str = '') -> str:
    '''Returns the default name of the application, or,
    if one is provided, adds the seed name to the end.'''
    # The default title of the program
    title = 'TPR Hint Notebook'

    # If there was a seed name, append it
    if seed_name:
        title = f'{title} ({seed_name})'

    # Return the title with the seed name appended, if provided
    return title
