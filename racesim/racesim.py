from tire import Tire
import itertools
from matplotlib import pyplot as plt

class RaceSim:
    def __init__(self, laps : int):
        self.laps = laps

    def simulate(self, tire0 : Tire,  lap_pit : list[int], tire_pit : list[Tire], print_laps : bool = False) -> float:

        lap = 1
        lap_stint = 0
        time = 0
        tire = tire0
        if print_laps:
            x = []
            y = []

        while lap <= self.laps:

            if lap in lap_pit:
                index = lap_pit.index(lap)
                tire = tire_pit[index]
                lap_stint = 0
                time += 20
                if print_laps:
                    print(f"Pit at lap {lap} for {tire}")

            lap_time = tire.laptime(lap_stint,)[0]
            time += lap_time

            if print_laps:
                print(f"Lap {lap}: {lap_time}")
                x.append(lap)
                y.append(lap_time)

            lap += 1
            lap_stint += 1

        if print_laps:
            plt.plot(x,y)
            plt.show()

        return time
    
    def optimize(self, tire0 : Tire, tires_available : list, pit_stops : int = 1) -> tuple[int, float, Tire]:
        optimal_pit = 0
        optimal_time = float("inf")



        """
        Para evitar esta repeticion, lo que puedo hacer es crear una funcion que me devuelva todas las combinaciones posibles de pit stops
        y lo mismo para neumaticos, y luego iterar sobre esas combinaciones.
        """

        pit_lap_options = list(itertools.combinations(range(1, self.laps+1), pit_stops))
        tire_pit_options = list(itertools.product(tires_available, repeat=pit_stops,))

        for pit_lap in pit_lap_options:
            for tire_pit in tire_pit_options:
                sim = self.simulate(tire0, pit_lap, tire_pit)
                if sim < optimal_time:
                    optimal_pit = pit_lap
                    optimal_time = sim
                    optimal_tire_pit = tire_pit

        return optimal_pit, optimal_time, optimal_tire_pit
"""
        if pit_stops == 1:
            for tire_pit in tires_available:
                for i in range(1, self.laps+1):
                    sim = self.simulate(tire0, [i], [tire_pit])
                    if sim < optimal_time:
                        optimal_pit = [i]
                        optimal_time = sim
                        optimal_tire_pit = [tire_pit]

        elif pit_stops == 2:
            for tire_pit1 in tires_available:
                for tire_pit2 in tires_available:
                    for i in range(1, self.laps+1):
                        for j in range(i+1, self.laps+1):
                            sim = self.simulate(tire0, [i, j], [tire_pit1, tire_pit2])
                            if sim < optimal_time:
                                optimal_pit = [i, j]
                                optimal_time = sim
                                optimal_tire_pit = [tire_pit1, tire_pit2]

        
        elif pit_stops == 3:
            for tire_pit1 in tires_available:
                for tire_pit2 in tires_available:
                    for tire_pit3 in tires_available:
                        for i in range(1, self.laps+1):
                            for j in range(i+1, self.laps+1):
                                for k in range(j+1, self.laps+1):
                                    sim = self.simulate(tire0, [i, j, k], [tire_pit1, tire_pit2, tire_pit3])
                                    if sim < optimal_time:
                                        optimal_pit = [i, j, k]
                                        optimal_time = sim
                                        optimal_tire_pit = [tire_pit1, tire_pit2, tire_pit3]
        
        return optimal_pit, optimal_time, optimal_tire_pit
"""