from google_speech import Speech

class TextReader:
    data = ""

    def __init__(self, data):
        self.data = data

    
    def speak(self):
        lang = "en"
        speech = Speech(self.data, lang)
        
        # you can also apply audio effects while playing (using SoX)
        # see http://sox.sourceforge.net/sox.html#EFFECTS for full effect documentation
        sox_effects = ("tempo", "1.5")
        return speech.play(sox_effects)



