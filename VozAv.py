import speech_recognition as sr
import pyttsx3  #importa Fala
from gtts import gTTS       #Importar Sintetizador de Voz da Google
from datetime import datetime   # importa sistema de data
from playsound import playsound
## Corrigir Acentos
from unicodedata import normalize



def remover_acentos(txt):
    return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')

def ListenWorkd():
    Falou = OuvirFala()  # Ouve a Fala
    #print(Falou)
    #print('Type Falou: ', type(Falou))
    TRFalou = remover_acentos(Falou)  # Corrige acentos para os comandos
    #print('Acento: ', TRFalou)
    return str(TRFalou)



def Falarhora():
    agora = datetime.now()  #data e horario atual
    #nome = "Ricardo"
    hora = agora.hour
    minuto = agora.minute
    texto = "Agora são " + str(hora) + " horas e " + str(minuto) + " minutos"
    #-sintetização da hora  /    Usar Formula Básica
    en = pyttsx3.init()
    en.setProperty('rate', 115)
    en.setProperty('volume', 1)
    en.setProperty('voice', b'brazil')
    en.say(texto)
    en.runAndWait()




#Capturar Fala
def OuvirFala():

    r = sr.Recognizer()
    with sr.Microphone() as s:
        r.adjust_for_ambient_noise(s)
        playsound('todo.mp3')
        #print('Diga Algo ...')
        audio = r.listen(s)
        Falou = r.recognize_google(audio, language='pt')
        #print('Você disse: ', Falou)
        Falou2 = remover_acentos(Falou)
        Falou3 = Falou2.lower()
        del(Falou)
        del(Falou2)
        return Falou3



def falag(falaragora):
    str(falaragora)
    voz = gTTS(falaragora, lang='pt')
    voz.save('voz.mp3')
    playsound("voz.mp3")



