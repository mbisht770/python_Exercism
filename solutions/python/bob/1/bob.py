def response(phrase):
    phrase = phrase.strip()

    if phrase == "":
        return "Fine. Be that way!"
    if phrase.isupper():
        if phrase.endswith("?"):
            return "Calm down, I know what I'm doing!"
        return "Whoa, chill out!"
    if phrase.endswith("?"):
        return "Sure."
    return "Whatever."
