class Tire():
    def __init__(self, time0 : float, degradation : float, max_laps : float, name : str = ""):

        """
        Define the tire object with the following attributes:
        time0 : float
            The time it takes to complete a lap on the first lap
        degradation : float
            The degradation of the tire per lap
        max_laps : float
            The maximum number of laps the tire can be used for
        """
        self.name = name
        self.time0 = time0
        self.max_laps = max_laps
        self.degradation = degradation
        

    def __str__(self):
        if self.name == "":
            return "Unnamed Tire"
        else:
            return self.name
        
    def __repr__(self):
        return self.__str__()
        


    def laptime(self, lap_stint : int, print_time : bool = False) -> float:
        """
        Calculate the laptime of the tire at a given lap
        """

        if lap_stint > self.max_laps:
            is_done = True
            time = self.time0 + ((self.max_laps)*self.degradation)*2

        else:
            is_done = False
            time = self.time0 + (lap_stint)*self.degradation

        if print_time:
            print(f"Stint lap {lap_stint}: {time}")
        return time, is_done