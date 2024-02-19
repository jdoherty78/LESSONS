import speech_recognition as sr
from speech_txt import SpeakText
from speech_calc_total import SpeechCalcTotal
from speech_calc_file import SpeechCalcFile

def SpeakLoop():
    x = True
    r = sr.Recognizer()
    
    while x:
        try:
            # time.sleep(1)
            with sr.Microphone() as source:
                print("START SPEAKING")
                r.adjust_for_ambient_noise(source, duration=0.5)
                # Listens to user's input voice
                audio = r.listen(source)
                MyText = r.recognize_google(audio)
                MyText = MyText.lower()
                SpeakText(MyText)
        
                split = MyText.split(" ")


                if "calculate" in split:

                    calc = SpeechCalcTotal(split)
                    total = sum(calc)
                    print("Total: {}".format(total))

                    SpeechCalcFile(total, calc)
                
                if "quit" in split or "stop" in split or "end" in split:
                    x = False
    
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        except sr.UnknownValueError as e:
            print("Unknown error occurred")
        
if __name__ == '__main__':
    SpeakLoop()
