print("🔮 Welcome to Srivardhan Maddi's Fortune Teller (21JE0517) 🔮")
mood = input("How are you feeling today? (happy/sad/neutral): ").lower()

if mood == "happy":
    print("✨ Your fortune: Joy radiates from within you, spreading light wherever you go. Bask in it, Vardhan, and keep shining bright! ✨")
elif mood == "sad":
    print("🌧️ Your fortune: Even the stormiest skies clear with time. Hold on tight, Vardhan-the rainbow is closer than you think. 🌈")
elif mood == "neutral":
    print("😐 Your fortune: Life flows steadily, Vardhan. Embrace the calm—it’s the perfect moment to plant seeds for future triumphs. 🌿")
else:
    print("🤔 Sorry, I don't have a fortune for that mood.")