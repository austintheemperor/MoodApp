"""ask user for name
ask how are you feeling
respond to feeling"""

bad_day_words = [
    "bad",
    "terrible",
    "awful",
    "horrible",
    "miserable",
    "dreadful",
    "lousy",
    "crappy",
    "rotten",
    "pathetic",
    "frustrating",
    "stressful",
    "chaotic",
    "disastrous",
    "grim",
    "bleak",
    "draining",
    "exhausting",
    "annoying",
    "irritating",
    "depressing",
    "overwhelming",
    "rough",
    "tough",
    "unbearable",
    "shitty",
    "tragic",
    "unlucky",
    "cursed",
    "messy",
    "hectic"
]

good_day_words = [
    "good",
    "great",
    "awesome",
    "fantastic",
    "amazing",
    "wonderful",
    "excellent",
    "perfect",
    "pleasant",
    "enjoyable",
    "nice",
    "lovely",
    "beautiful",
    "productive",
    "successful",
    "smooth",
    "easy",
    "relaxing",
    "peaceful",
    "fun",
    "exciting",
    "rewarding",
    "satisfying",
    "bright",
    "cheerful",
    "uplifting",
    "refreshing",
    "energizing",
    "lucky",
    "blessed",
    "memorable"
]

def findWord(hayStack, needle):
    return (' ' + needle + ' ') in (' ' + hayStack + ' ')

name = input("What is your name? ")
print(f"Hello {name}, how are you feeling today?")
userInput = input().lower()
day = ""

# Check for bad words
for word in bad_day_words:
    if findWord(userInput, word):
        print("Sorry, that's not a good day.")
        day = "bad"
        break

# check for good words
if day != "bad":
    for word in good_day_words:
        if findWord(userInput, word):
            print("Great, that's a good day.")
            day = "good"
            break

# if I could not find any specific words
if day != "good" and day != "bad":
    print("I could not determine how you are feeling.")
