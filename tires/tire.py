class Tire():
    def __init__(self, time0 : float, degradation : float, max_laps : float, name : str):

        """
        Define the tire object with the following attributes:
        time0 : float
            The time it takes to complete a lap on the first lap
        degradation : float
            The degradation of the tire per lap
        max_laps : float
            The maximum number of laps the tire can be used for
        """
        self.time0 = time0
        self.max_laps = max_laps
        self.degradation = degradation
        self.name = name

    def __str__(self):
        return self.name
        


    def laptime(self, lap_stint : int) -> float:
        """
        Calculate the laptime of the tire at a given lap
        """
        is_done = False

        if lap_stint > self.max_laps:
            is_done = True

        return self.time0 + (lap_stint)*self.degradation, is_done