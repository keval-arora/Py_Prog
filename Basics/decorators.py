def to_speak(func):

    def yell():
        return func().upper()
    def wisper():
        return func().lower()
    
    if n == 1:
        return yell
    else:
        return wisper