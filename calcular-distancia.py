import math

def calcular_distancia(lat1, lon1, lat2, lon2): 
    radio_tierra = 6371.0
    
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    
    a = math.sin(dlat / 2)** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    distancia = radio_tierra * c
    return distancia

locales_prueba = [
   {"nombre": "Local A", "latitud": 40.712776, "longitud": -74.005974},
   {"nombre": "Local B", "latitud": 34.052235, "longitud": -118.243683},
   {"nombre": "Local C", "latitud": None, "longitud": None},
   {"nombre": "Local D", "latitud": 41.878113, "longitud": -87.629799},
   {"nombre": "Local E", "latitud": None, "longitud": None},
]

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

latitud_usuario = -32.59580331074668
longitud_usuario = -62.82951255514566

locales_ordenados = ordenar_locales(latitud_usuario, longitud_usuario)

for local in locales_ordenados:
    print(f"Nombre: {local['nombre']}, Distancia: {local['distancia']}")