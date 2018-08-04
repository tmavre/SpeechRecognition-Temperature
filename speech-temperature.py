import sys
import speech_recognition as sr
from weather import Weather, Unit


def start_speech_listener():
    while True:
        # initialize recognizer.
        r = sr.Recognizer()
        # mention source it will be either Microphone or audio files.
        with sr.Microphone() as source:
            print("Speak Anything :")
            # listen to the source
            audio = r.listen(source)
            try:
                # use recognizer to convert our audio into text part.
                text = r.recognize_google(audio)
                print("You said : {}".format(text))

                if text == "temperature":
                    # Get weather forecasts for the upcoming days.
                    weather = Weather(unit=Unit.CELSIUS)
                    # put your location 
                    location = weather.lookup_by_location('brno')
                    forecasts = location.forecast
                    for forecast in forecasts:
                        print("===============")
                        print("Date: ", forecast.date)
                        print(forecast.text)
                        print("high : ", forecast.high)
                        print("low : ", forecast.low)
                        print("===============")
                if text == "exit":
                    sys.exit(0)
            except sr.RequestError:
                print(" API was unreachable or unresponsive")
                sys.exit(1)
            except sr.UnknownValueError:
                print("Unknown Value Error")


if __name__ == '__main__':
    start_speech_listener()
