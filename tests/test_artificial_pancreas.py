import pytest
from  main.artificial_pancreas import  ArtificialPancreasSystem


@pytest.fixture
def instance():
    return ArtificialPancreasSystem(glucose_level=100, target_glucose=10, tolerance=0.1, insulin_sensitivity=10)



def test_meal(instance):
    start = instance.glucose_level
    pan = instance.meal(carbs=60)
   # assert instance.glucose_level > start
    assert pan > start, f"Expects pan to be greater than start"
    
def test_exercise(instance):
    exp = instance.glucose_level
    dur = instance.exercise(duration=int(40))
    assert exp > dur                        # You can't compare an int and None

#def test_predict_action(var):
 #   aps = ArtificialPancreasSystem(insulin_sensitivity = 0.1, target_glucose =120, tolerance = 10, glucose_level = 5.0)
  #  action, level = var.pretict_action
# Read more on type hints in pyton