class ArtificialPancreasSystem:
    """A simplified model for data-driven glucose regulation."""
        
    GLUCOSE_PER_CARB = 0.5      # fixed increase per carb unit
    GLUCOSE_BURN_PER_MIN = 0.3  # fixed decrease per minute of exercise


    def __init__(self, glucose_level, insulin_sensitivity=1.0, target_glucose=100, tolerance=10):
        self.glucoselevel = glucose_level
        self.insulin_sensitivity = insulin_sensitivity
        self.target_glucose = target_glucose
        self.tolerance = tolerance
        


    def __repr__(self):
        return f"ArtificialPancreasSystem(Glucose Level: {self.glucoselevel}, Insulin Sensitivity: {self.insulin_sensitivity}, Target Glucose: {self.target_glucose}, Tolerance: {self.tolerance})" # This is the representational state of the class i would like to see when i print the class object
        # TODO: initialize class attributes here = DONE
        #pass

    def meal(self, carbs: float):
        """Simulate a meal event (input feature: carbs)."""

        if carbs > 0:
            self.glucoselevel += carbs * self.GLUCOSE_PER_CARB

        if carbs < 0:
            raise ValueError("You haven't eaten, Carbohyrate level cannot be non-negative")
        



        # TODO: increase glucose based on carbs eaten
        pass

    def exercise(self, duration: float):
        """Simulate physical activity (input feature: duration)."""

        if duration > 0:
            self.glucoselevel -= duration * self.GLUCOSE_BURN_PER_MIN
        
        if self.glucoselevel < 50:
            self.glucoselevel = 50 # Prevent glucose from dropping below a safe level

        if duration < 0:
            raise ValueError("You havent done any exercise, duration cannot be negative")
        # TODO: decrease glucose based on duration of exercise
        pass




    def predict_action(self, target_glucose: float, tolerance: float):
        """
        Predict and apply an appropriate system action.
        Acts like a decision function in a model.
        """
        self.target_glucose = target_glucose
        self.tolerance = tolerance
        self.deliver_insulin()

    def deliver_insulin(self):
        
        excallation = self.target_glucose + self.tolerance
        insulin = self.insulin_sensitivity * (self.glucoselevel - self.target_glucose)

        if self.glucoselevel > excallation:
            print(f"You need to take {insulin} amount of insulin")
        elif self.glucoselevel < (self.target_glucose - self.tolerance):
            print("You need to eat something, your glucose level is too low")
        else:
            print("Your glucose level is stable, no action needed")
        
        # TODO: decide what to do if glucose is too high, too low, or stable
        #pass