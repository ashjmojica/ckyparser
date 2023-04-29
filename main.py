allowed_sentences = [
    "I want to travel",
    "I like Texas",
    "I want to swim",
    "Go to South Padre",
    "Get a hotel",
    "On the beach",
    "I want a view",
    "Love the sunrise",
    "A nice vacation",
    "Book a boat",
    "Need this trip",
    "Waves are high",
    "Prefer the boat",
    "I enjoy speed",
    "I love water",
]

def parse_sentence(sentence):
    if sentence in allowed_sentences:
        print("This sentence is allowed.")
    else:
        print("This sentence is not allowed.")

# Test the parser with an allowed and a not allowed sentence
parse_sentence("I want to travel")
parse_sentence("Random sentence")