 # import the library
import speech_recognition as sr 
import datetime
from weather import Weather, Unit

while True:
    # initialize recognizer
    r = sr.Recognizer()  
    # mention source it will be either Microphone or audio files.
    with sr.Microphone() as source:  
        print ("Speak Anything :")
        # listen to the source
        audio = r.listen(source)  
        try:
            # use recognizer to convert our audio into text part.
            text = r.recognize_google(audio)  
            print("You said : {}".format(text))

            if text == "temperature":
                #Get weather forecasts for the upcoming days.
                weather = Weather (unit=Unit.CELSIUS)
                #put your location here
                location = weather.lookup_by_location ('brno')
                forecasts = location.forecast
                for forecast in forecasts:
                    print ("===============")
                    print ("Date: ", forecast.date)
                    print (forecast.text)
                    print ("high : ", forecast.high)
                    print ("low : ", forecast.low)
                    print ("===============")

            if text == "exit":
                break

        except:
            # In case of voice not recognized  clearly
            print("Sorry could not recognize your voice")  
