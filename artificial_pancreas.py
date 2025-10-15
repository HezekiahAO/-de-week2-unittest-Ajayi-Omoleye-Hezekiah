class ArtificialPancreasSystem:
    "A simplified model for data-driven glucose regulation."
        
    GLUCOSE_PER_CARB = 0.5      # fixed increase per carb unit
    GLUCOSE_BURN_PER_MIN = 0.3  # fixed decrease per minute of exercise


    def __init__(self, glucose_level, insulin_sensitivity: float, target_glucose: float, tolerance: float):
        self.glucoselevel = glucose_level
        self.insulin_sensitivity = insulin_sensitivity
        self.target_glucose = target_glucose
        self.tolerance = tolerance
        


    def __repr__(self):
        return f"ArtificialPancreasSystem(Glucose Level: {self.glucoselevel}, Insulin Sensitivity: {self.insulin_sensitivity}, Target Glucose: {self.target_glucose}, Tolerance: {self.tolerance})" # This is the representational state of the class i would like to see when i print the class object.

    def meal(self, carbs: float):
        """Simulate a meal event (input feature: carbs)."""

        if carbs > 0:
            self.glucoselevel += carbs * self.GLUCOSE_PER_CARB

        else:
            print("You haven't eaten, Carbohyrate level cannot be non-negative")
        


    def exercise(self, duration: float):
        """Simulate physical activity (input feature: duration)."""

        if duration > 0:
            self.glucoselevel -= duration * self.GLUCOSE_BURN_PER_MIN
        
        if self.glucoselevel < 50:
           self.glucoselevel = 50 # Prevent glucose from dropping below a safe level
           print("Duration of exercise is dangerously high, you need to stop the excersies!")

        if duration <= 0:
            print("You havent done any exercise today, get to work!")


    def predict_action(self, glucose_level, target_glucose: float, tolerance: float):
        """
        Predict and apply an appropriate system action.
        Acts like a decision function in a model.
        """
        self.target_glucose = target_glucose
        self.glucose_level = glucose_level
        self.tolerance = tolerance
        
        escallation = self.target_glucose + self.tolerance
        descallation = self.target_glucose - self.tolerance
        insulin = self.insulin_sensitivity * (self.glucoselevel - self.target_glucose)

        if self.glucoselevel >= escallation:
            print(f"You need to take {insulin} amount of insulin")
        elif self.glucoselevel <= descallation:
            print("You need to eat some CARB, your glucose level is too low")
        else:
            print("Your glucose level is stable, no action needed")
        


pan = ArtificialPancreasSystem(glucose_level=100, insulin_sensitivity = 1, target_glucose=100, tolerance=10)   # create an instance of the ArtificialPancreasSystem class
pan.exercise(duration=50)  # Simulate 30 minutes of exercise
pan.meal(carbs=60)        # Simulate a meal with 60 grams of carbohydrates
pan.predict_action(target_glucose = 50, tolerance = 6, glucose_level=5) # Predict action based on current glucose level, target glucose, and tolerance