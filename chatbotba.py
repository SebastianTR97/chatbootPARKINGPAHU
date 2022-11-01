from nltk.chat.util import Chat, reflections
import numpy as np
import random
import string # to process standard Python strings

mis_reflexions = {

}

pares = [

        [
        r"si, soy estudiante|hola, si|si|si soy|si soy estudiante|sip|sipi|yep|yeah",
        ["Perfecto, digite su numero de identificacion universitaria",]
    ],

 
        [
        r"No",
        ["Entiendo, en ese caso no puedo ayudarte. El servicio unicamente está disponible para estudiantes de la Intitución",] 
    ],
       
    [
        r"123",
        ["Hola sebastian Turizo, usted tiene ingreso para la moto con placa URW53F, por favor ingrese.",]
    ],

        [
        r"456",
        ["Hola Santiago Segura, usted tiene ingreso para la moto con placa GKM52M, por favor ingrese.",]
    ],

            [
        r"789",
        ["Hola Diego Cardona, usted NO tiene ingreso para el parqueadero",]
    ],

            [
        r"321|654|987|159|753|852|486|357",
        ["Disculpe, usted no se encuentra registrado en el sistema de la institución, porfavor intente nuevamente",]
    ],

     [
        r"perro|perra|pendejo|pendeja|idiota|sapo|sapa",
        ["Disculpe,no logré entender. ¿Podria intentar nuevamente?",]
    ],


    [
        r"disculpa (.*)",
        ["No pasa nada",]
    ],
    [
        r"hola|hey|buenas|oli|ola|hello",
        ["Hola, ¿podria digitar su numero de identificacion universitaria? ", "Que tal",]
    ],
    [
        r"que (.*) quieres ?",
        ["Nada gracias",]
        
    ],
    [
        r"(.*) creado ?",
        ["Fui creado hoy",]
    ],
    [
        r"finalizar",
        ["Chao","Fue bueno hablar contigo"]
],
    
]
def chatear():
    print("***************************************************************************************************************************************") 
    print("* Hola, soy el servicio de PARKINGPAHU, puedo ayudarle a dar ingreso al parqueadero de la universidad, siempre y cuando tengas acceso *") 
    print("* ¿Eres estudiante de la universidad actualmente?                                                                                     *") 
    print("***************************************************************************************************************************************") 
    chat = Chat(pares, mis_reflexions)
    chat.converse()
if __name__ == "__main__":
    chatear()

chatear()