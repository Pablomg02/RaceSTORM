

class Car():
    def __init__(self, tire):
        """
        Define the car object. It is the object used to model the car in the simulation.

        Parameters
        ----------
        tire : Tire
            The tire object that the car is using.
        """
        self.tire = tire
        self.stint_lap = 1



    def laptime(self, addlap : bool = True) -> float:
        """
        Calculate the laptime of the car at a given lap

        Parameters
        ----------
        addlap : bool
            Whether to add a lap to the stint lap counter or not

        Returns
        -------
        time : float
            The time it takes to complete the lap
        """

        time, is_done = self.tire.laptime(self.stint_lap)


        if addlap:
            self.stint_lap += 1

        return time
    


    def pitstop(self, tire):
        """
        Change the tire of the car. This method can be called by the simulator to change the tire of the car. 
        """
        self.tire = tire
        self.stint_lap = 1