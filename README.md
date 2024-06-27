# LC---distancia_locales

Tomando en consideración mi ignorancia acerca de la comunicación dentro de la app, extraje la lógica a un ambiente local para que opere con datos de prueba y luego pueda ser reflejada en entorno de desarrollo. 

La primera función es tomada de GPT, basada en una fórmula llamada Formula de Harversine.

Opera con mayor precision al tomar el radio de la tierra y realizar operaciones trigonométricas. 

```
def calcular_distancia(lat1, lon1, lat2, lon2): 
    radio_tierra = 6371.0
    
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    
    a = math.sin(dlat / 2)** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    distancia = radio_tierra * c
    return distancia
```

Una vez obtenido ese valor de distancia, se puede proceder con un método de ordenamiento que tomará en cuenta el resultado entre ese calculo y la ubicación del usuario 

```
def ordenar_locales(latitud_usuario, longitud_usuario): 
        locales = locales_prueba
        if not locales:
            return []
        
        for local in locales: 
            if "latitud" in local and "longitud" in local and local["latitud"] is not None and local["longitud"] is not None: 
                local["distancia"] = local["distancia"] = calcular_distancia(latitud_usuario, longitud_usuario, local["latitud"], local["longitud"])
                print(local["distancia"])
            else:
                local["distancia"] = 0
                
        locales_con_distancia = [local for local in locales if local["distancia"] != 0]
        locales_sin_distancia = [local for local in locales if local["distancia"] == 0]
        
        locales_con_distancia.sort(key=lambda x: (x["distancia"], x["nombre"]))
        locales_sin_distancia.sort(key=lambda x: (x["nombre"]))
        
        return locales_con_distancia + locales_sin_distancia
```

Cuando exista posibilidadd de generar distancia debido a que la latitud y longitud no son None (esto deberá ser revisado para adaptar a las condiciones necesarias), se podrá generar el campo de distancia dentro del json o lista que se provee.
En caso de que no, ese campo obtendrá el valor de 0

Los datos de prueba para locales fueron los siguientes:

```
locales_prueba = [
   {"nombre": "Local A", "latitud": x1, "longitud": y1},
   {"nombre": "Local B", "latitud": x2, "longitud": y2},
   {"nombre": "Local C", "latitud": None, "longitud": None},
   {"nombre": "Local D", "latitud": x3, "longitud": y3},
   {"nombre": "Local E", "latitud": None, "longitud": None},
]
```

y se añadieron mis coordenadas para generar las pruebas, a través de las variables latitud_usuario y longitud_usuario.

Una vez ejecutado, se obtuvieron los siguientes resultados por ordenamiento:

Nombre: Local A, Distancia: z1
Nombre: Local D, Distancia: z2
Nombre: Local B, Distancia: z3
Nombre: Local C, Distancia: inf
Nombre: Local E, Distancia: inf


Se observa que aquellos con inf han sido ordenados alfabeticamente. 




