import random
import matplotlib.pyplot as plt


def laptime(lap, laptime0_average, laptime_stddev):
    """
    Devuelve el tiempo de una vuelta, sabiendo la vuelta del stint, siguiendo una distribucion normal
    """
    return random.normalvariate(laptime0_average + 0.1*lap, laptime_stddev+0.003*lap)

def safety_car(prob):
    """
    Devuelve True si hay safety car, False si no lo hay
    """
    return random.random() < prob


def race_sim(laptime, laps, laptime_args = []):
    """
    Dada una funcion que devuelve el tiempo de una vuelta, simula una carrera de n vueltas.
    
    laptime_args es una lista con los argumentos que necesita la funcion laptime, ademas del 
    primer argumento que es el numero de vuelta.
    """
    final_time = 0
    for i in range(laps):
        final_time += laptime(i, *laptime_args)

    return final_time



# vamos a suponer que el tiempo por vuelta es de 60 segundos de media
laptime0_average = 60
# y que la desviación estándar es de 5 segundos
laptime_stddev = 0.3


vueltas = 60

result = race_sim(laptime, # Funcion que calcula el tiempo de una vuelta
                  vueltas, # Numero de vueltas
                  laptime_args=[laptime0_average, laptime_stddev] # Otros argumentos de la funcion
                  )
print(f"Ejemplo de una carrera: {result}")


# Vamos a hacer una simulacion de 1000 carreras
results = []

for _ in range(1000):
    race = race_sim(laptime, vueltas, laptime_args=[laptime0_average, laptime_stddev])
    if safety_car(0.03):
        race += 20
    results.append(race)

plt.figure()
plt.hist(results, bins=100)
plt.show()
    



