import random

tarotCards = ["The Fool (0)", "The Magician (1)",  "The High Priestess (2)", "The Empress (3)", " The Emperor (4)",
              "The Hierophant (5)", "The Lovers (6)", "The Chariot (7)", "Strength (8)", "The Hermit (9)",
              "Wheel of Fortune (10)", "Justice (11)", "The Hanged Man (12)", "Death (13)", "Temperance (14)",
              "The Devil (15)", "The Tower (16)", "The Star (17)", "The Moon (18)", "The Sun (19)", "Judgment (20)",
              "The World (21)"]

past = random.randint(0, 1)
if past == 0:
    print()
    print("Past: " + random.choice(tarotCards) + " reversed.")
else:
    print()
    print("Past: " + random.choice(tarotCards))

present = random.randint(0, 1)
if present == 0:
    print("Present: " + random.choice(tarotCards) + " reversed.")
else:
    print("Present: " + random.choice(tarotCards))

future = random.randint(0, 1)
if future == 0:
    print("Future: " + random.choice(tarotCards) + " reversed.")
else:
    print("Future: " + random.choice(tarotCards))

