from tire import Tire

class RaceSim:
    def __init__(self, laps : int):
        self.laps = laps

    def simulate(self, tire0 : Tire,  lap_pit : int, tire_pit : Tire):

        lap = 1
        lap_stint = 0
        time = 0
        tire = tire0

        while lap <= self.laps:
            if lap == lap_pit:
                tire = tire_pit
                lap_stint = 0
            time += tire.laptime(lap_stint)[0]
            lap += 1
            lap_stint += 1

        return time
    
    def optimize(self, tire0 : Tire, tires_available : list):
        optimal_pit = 0
        optimal_time = float("inf")

        for tire_pit in tires_available:
            for i in range(1, self.laps+1):
                sim = self.simulate(tire0, i, tire_pit)
                if sim < optimal_time:
                    optimal_pit = i
                    optimal_time = sim
                    optimal_tire_pit = tire_pit
        
        return optimal_pit, optimal_time, optimal_tire_pit