import requests
import datetime

# URL de la API

print("____________________________________________")
print("____Consultar buses proximos a paradero_____")
print("____________________________________________")
paradero_i = input("ingrese paradero a consultar: ")
print("____________________________________________")
print("____________________________________________")

url = "https://api.xor.cl/red/bus-stop"
new_url ="{}/{}".format(url, paradero_i)

response = requests.get(new_url)

try:  
    # Verificar si la respuesta es exitosa
    response.raise_for_status()

    # Procesar los datos de la respuesta
    data = response.json()

    #Hora de consulta
    fecha_actual = datetime.datetime.now().date()
    hora_actual = datetime.datetime.now().time()
    hora_formateada = hora_actual.strftime('%H:%M %p')

    print("___________Proximidad buses_________________")

    print("____________________________________________")

    print('Fecha de consulta',fecha_actual,' ',hora_formateada)

    #print(data)
    print("____________________________________________")

    paradero = data['id']
    print('Paradero: ', paradero)

    print("____________________________________________")

    direccion = data['name']
    print('Dirección: ',direccion)
    
    results = data['services']
    print("____________________________________________")
    print("__________informacion del paradero__________")
    print("____________________________________________")
    for bus in results:
        id = bus['id']
        status = bus['status_description']
        print('|',id,'|',status)
        print("____________________________________________")

      
except requests.exceptions.RequestException as error:
    # Manejar el error de red
    print(f"Error de red: {error}")
except ValueError as error:
    # Manejar el error de procesamiento de la respuesta
    print(f"Error de respuesta: {error}")