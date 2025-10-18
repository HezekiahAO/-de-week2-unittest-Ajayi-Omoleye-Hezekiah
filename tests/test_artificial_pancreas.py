import unittest 
import main.artificial_pancreas as artificial_pancreas

class TestArtificialPancreas(unittest.TestCase):
    def test_calculate_insulin_dosage(self):
        aps = artificial_pancreas.ArtificialPancreasSystem(glucose_level=180, insulin_sensitivity=0.1, target_glucose=120, tolerance=10)
        insulin_dosage = aps.insulin_sensitivity * (aps.glucoselevel - aps.target_glucose)
        self.assertEqual(insulin_dosage, 6.0)  # 0.1 * (180 - 120) = 6.0

unittest.main()