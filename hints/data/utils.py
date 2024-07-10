
# Utility functions that don't relate to any global vars, for data.

# This might become a minor class function.
def remove_braces(text: str) -> str:
    '''Remove the {} from a string.'''
    return text.replace('{', '').replace('}', '')
