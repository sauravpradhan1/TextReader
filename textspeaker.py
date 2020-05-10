from google_speech import Speech

# say "Hello World"
text = input("Please enter your text")
lang = "en"
speech = Speech(text, lang)

# you can also apply audio effects while playing (using SoX)
# see http://sox.sourceforge.net/sox.html#EFFECTS for full effect documentation
sox_effects = ("tempo", "1.5")
speech.play(sox_effects)
