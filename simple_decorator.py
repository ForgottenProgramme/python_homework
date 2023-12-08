def polite(rejection):
    def wrapper():
        return "You're a wonderful person but " + rejection() + " I wish you all the best!"
    
    return wrapper

@polite
def rejection(name= "John"):
    return f"I cannot be with you, {name}."

print(rejection())

