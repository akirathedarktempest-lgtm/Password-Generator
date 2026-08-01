import random

text="abcdefghijklmnopqrstuvwxyz"
captial_text="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="0123456789"
special_symbols="@#$&%"

def generate():
    token=""
    for _ in range(3):
        for __ in range(12):
            token+=random.choice([random.choice(text),random.choice(captial_text),random.choice(numbers),random.choice(special_symbols)])
        token+="."
    return token

print(generate())
#so...i am working on an application, and that application needs api, and api needs security, and for that, i am making this token generator
