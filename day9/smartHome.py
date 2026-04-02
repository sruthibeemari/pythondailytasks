class WifiDevice:
    def wifi(self):
        print("Wifi Connected")
class VoiceAssistant:
    def Voice(self):
        print("Voice assistant Activated")
class SmartSpeaker(WifiDevice,VoiceAssistant):
    def Speaker(self):
        print("Smart Speaker playing music")


s1=SmartSpeaker()
s1.wifi()
s1.Voice()
s1.Speaker()
