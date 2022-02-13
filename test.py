import unittest
import most_active_cookie

class Test(unittest.TestCase):
    def test(self):
        f = 'cookie_log.csv'
        self.assertEqual(most_active_cookie(), ['AtY0laUfhglK3lC7'])
        self.assertEqual(most_active_cookie(), ['SAZuXPGUrfbcn5UA', '5UAVanZf6UtGyKVS', 'AtY0laUfhglK3lC7'])
        self.assertEqual(most_active_cookie(), ['4sMM2LxV07bPJzwf'])
        self.assertEqual(most_active_cookie(), ['SAZuXPGUrfbcn5UA'])
        self.assertEqual(most_active_cookie(), ['fbcn5UAVanZf6UtG'])
        self.assertEqual(most_active_cookie(), [])
            
if __name__ == '__main__':
    unittest.main()
