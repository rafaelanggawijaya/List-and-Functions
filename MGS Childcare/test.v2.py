def list_cleaner(unclean):
    return [[word.strip('\' ,') for word in sublist] for sublist in unclean]

listing = [["carl", 10], ["Matt", 0]]
list_cleaner(listing)
print(listing)
