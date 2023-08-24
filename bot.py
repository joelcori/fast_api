import re
import random


def get_rpta(entrada):
    # Establecer un patrón de expresión regular
    msj_dividido = re.split(r"\s|[,:;.?!-_]\s*", entrada.lower())

    # Revisar todas las respuestas posibles
    rpta = check_todo_msj(msj_dividido)

    return rpta


#                              palabras reconocidas - Sencillas            Requeridas
def msj_prob(msj_user, palabras_reconocidas, rpta_unica=False, palabras_req=[]):
    certeza_msj = 0
    hay_palabras_req = True

    # Iteración de mensaje (por cada palabra) - Validación
    for palabra in msj_user:
        if palabra in palabras_reconocidas:
            certeza_msj += 1

    pctj = float(certeza_msj) / float(len(palabras_reconocidas))

    # Validación
    for palabra in palabras_req:
        if palabra not in msj_user:
            hay_palabras_req = False
            break

    if hay_palabras_req or rpta_unica:
        return int(pctj * 100)
    else:
        return 0


# Función que revisa todas las posibles respuestas
def check_todo_msj(msj):
    mayor_prob = {}  # Probabilidad mayor

    def rpta(rpta_bot, list_palabras, rpta_unica=False, palabras_req=[]):
        nonlocal mayor_prob
        mayor_prob[rpta_bot] = msj_prob(msj, list_palabras, rpta_unica, palabras_req)
    
    rpta("Por favor, escriba su nombre y apellido", ["si"], rpta_unica=True)

    rpta("¡Hola " + "Joel" + "! Gracias por contactarnos, ¿cómo podemos ayudarte? \n" +
              "     1. Buscar prendas \n" +
              "     2. Nuestras sedes \n" +
              "     3. Promociones y descuentos \n" +
              "     4. Consultar en WhatsApp \n" +
              "     Por favor, elija una opción (1-4)", ["joel"], rpta_unica=True)
    
    rpta("Bien, ¿para quién es la prenda? \nhombre \nmujer", ["uno"], rpta_unica=True)
    rpta(
        "¿Qué prendas desea? \nPantalones \nCamisas \nPolos \nCasacas \nRopa Interior",
        ["hombre", "mujer"],
        rpta_unica=True,
    )
    rpta(
        "¿Qué talla desea? \nXS \nS \nM \nL \nXL \nXXL",
        ["pantalones", "camisas", "polos", "casacas", "ropa", "interior"],
        rpta_unica=True,
    )
    rpta(
        "Bien, ¿qué color desea? \nRojo \nAzul \nVerde \nAzul Noche",
        ["xs", "s", "m", "l", "xl", "xxl"],
        rpta_unica=True,
    )
    rpta(
        "Bien, enseguida pasamos al proceso de compra",
        ["rojo", "azul", "verde", "azul noche"],
        rpta_unica=True,
    )

    rpta("¿En qué distrito vive?", ["dos"], rpta_unica=True)
    rpta(
        "La dirección de la sede que hay en su distrito es Av. Alfredo Mendiola 3870",
        ["independencia"],
        rpta_unica=True,
    )
    rpta(
        "La dirección de la sede que hay en su distrito es Av. Alfredo Benavides 870",
        ["surco"],
        rpta_unica=True,
    )
    rpta(
        "La dirección de la sede que hay en su distrito es Av. Nicolás Ayllón 4582",
        ["ate"],
        rpta_unica=True,
    )
    rpta(
        "La dirección de la sede que hay en su distrito es Av. Circunvalación 370",
        ["sjl"],
        rpta_unica=True,
    )

    rpta(
        "Este 19 y 20 de septiembre te traemos descuentos y promociones en vestidos y blusas para dama por la primavera. Puedes obtener hasta un 40%. ¡No te lo pierdas! \n-> Blusas \n-> Vestidos \nEscribe la opción que deseas y te mostraremos sus promociones",
        ["tres"],
        rpta_unica=True,
    )
    rpta(
        "Excelente. Aquí te mostramos los vestidos para dama que tenemos disponibles en la promoción. Escriba el número de opción del vestido que prefiera \na) VESTIDO LARGO CAMI TATIENNE S/ 61.99 -40% \nb) VESTIDO ESPRIT S/ 79.99 -34% \nc) VESTIDO LARGO BARBADOS S/ 67.99 -29%",
        ["vestidos"],
        rpta_unica=True,
    )
    rpta(
        "Excelente. Aquí te mostramos las blusas para dama que tenemos disponibles en la promoción. Escriba el número de opción del vestido que prefiera \na) BLUSA MANGA LARGA VUELOS MARQUIS S/ 70.99 -25% \nb) BLUSA CUELLO AZIZ S/ 89.99 -32% \nc) BLUSA INDEX LONG SLEEVE S/ 58.99 -17%",
        ["blusas"],
        rpta_unica=True,
    )
    rpta(
        "Bien, ahora le haremos una guía para el proceso de compra...",
        ["a", "b", "c"],
        rpta_unica=True,
    )

    rpta(
        "Excelente, para contactarte en WhatsApp por favor ingrese su consulta:",
        ["cuatro"],
        rpta_unica=True,
    )
    rpta(
        "Bien, por favor ingrese a este link: \nhttps://api.whatsapp.com/send/?phone=%2B51926916453&text=Hola%2C+tengo+una+consulta%2C+vengo+del+ChatBot.&type=phone_number&app_absent=0",
        ["devolución", "reclamo"],
        rpta_unica=True,
    )

    # Buscar respuesta más probable
    mejor_match = max(mayor_prob, key=mayor_prob.get)

    return unknown() if mayor_prob[mejor_match] < 1 else mejor_match


def unknown():
    rpta = [
        "¿Puedes decirlo de nuevo?",
        "No estoy seguro de lo que quieres",
        "Búscalo en Google a ver qué tal",
    ][random.randrange(3)]
    return rpta


def msj_bienvenida():
    # opcion_inicio = input("Bot: Bienvenido, ¿tienes alguna pregunta o necesitas ayuda? \nCliente: ")
    # return opcion_inicio
    opcion_inicio = "Bienvenido, ¿tienes alguna pregunta o necesitas ayuda?"

    return opcion_inicio


def msj_nombre_opciones(entrada):
    if entrada == "si":
        opcion_nombre = "Por favor, escriba su nombre y apellido"
        return opcion_nombre
        # print("Bot: ¡Hola " + opcion_nombre + "! Gracias por contactarnos, ¿cómo podemos ayudarte? \n" +
        #       "     1. Buscar prendas \n" +
        #       "     2. Nuestras sedes \n" +
        #       "     3. Promociones y descuentos \n" +
        #       "     4. Consultar en WhatsApp \n" +
        #       "     Por favor, elija una opción (1-4)")
    else:
        # print("Bot: Fue un gusto conversar contigo.")
        return "Fue un gusto conversar contigo."


# msj_nombre_opciones()

# while True:
#     print("Bot: " + get_rpta(input('Cliente: ')))
