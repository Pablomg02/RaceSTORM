"""
NOTE: The Tire class will not maintain state information (e.g., wear, temperature) directly. 
This data will be managed within the Car object. The rationale is that tires are frequently replaced during a race, 
and associating state directly with tire instances could lead to inconsistency or errors when handling 
multiple cars or replacing tires dynamically.
"""


class DeterministicTire():
    def __init__(self, time0 : float, degradation : float, max_laps : float, name : str = ""):

        """
        Define the tire object with the following attributes:
        time0 : float
            The time it takes to complete a lap on the first lap
        degradation : float
            The degradation of the tire per lap
        max_laps : float
            The maximum number of laps the tire can be used for. After this number of laps, the tire is considered destroyed
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
        Calculate the laptime of the tire at a given lap. The tire is the object that govern the laptime of the car in the simulation, and the
        other car parameters, such as the fuel load, are treated as time multipliers for now.

        Parameters
        ----------
        lap_stint : int
            The lap number of the stint the tire is in (starting from 1)
        print_time : bool
            Whether to print the time of the lap

        Returns
        -------
        time : float
            The time it takes to complete the lap 
        is_done : bool
            Whether the tire is destroyed or not. It is modeled as if the tire has a puncture after the max_laps
        """

        if lap_stint > self.max_laps:
            is_done = True
            time = self.time0 + ((self.max_laps)*self.degradation)*3

        else:
            is_done = False
            time = self.time0 + (lap_stint)*self.degradation

        if print_time:
            print(f"Stint lap {lap_stint}: {time}")
        return time, is_done