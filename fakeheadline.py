import random

# subjects
subjects = [ 
    "Aamir", "Barack", "Batman", "Bill", "Captain", "Elon", "Indian", "Iron",
    "Jack", "James", "KL", "MS", "Mission", "Money", "Narendra", "Salman",
    "Shahrukh", "Squid", "Tom", "Virat"
]

actions = [
    "announced", "arrived", "challenged", "launched", "played", "replaced",
    "transformed", "won"
]

things = [
    "Mumbai", "most centuries", "the Black Pearl", "Season 4", "the Indian RBI Bank",
    "this Sunday", "Indian cinema", "England in Manchester", "a secret bunker",
    "a submarine", "a time machine", "a spaceship", "an invisible car", "the White House",
    "the Great Wall of China", "the Oscars stage", "the moon base", "Wakanda"
]

# Headlines loop
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    thing = random.choice(things)

    headline = f"Breaking News by MS: {subject} {action} {thing}"
    print(f"\n{headline}")

    # Ask if user wants to save
    save_input = input("Do you want to save this headline to a file? (yes/no): ").strip().lower()
    if save_input == "yes":
        with open("fake_news_log.txt", "a") as file:
            file.write(headline + "\n")
        print("✅ Headline saved to 'fake_news_log.txt'.")

    # Ask if user wants another headline
    user_input = input("Do you want to see another headline? (yes/no): ").strip().lower()
    if user_input == "no":
        break

# Exit message
print("\nThank you for using the Fake News Headline Generator. Have a fun day! — by Manish")
