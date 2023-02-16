import unittest
import requests

#Numéro identifiant du client dont on teste le score
NUM_ID = 100002

class TestScore(unittest.TestCase):
    #URL de l'API
    URL = "https://stark-lake-17991.herokuapp.com/predict?numeroClient=" + str(NUM_ID)

    #Fonction qui teste si le score renvoyé est bien entre 0 et 1
    def test_is_score_between_0_and_1(self):  
        response=requests.get(self.URL).json()
        score=response[0]
        self.assertGreaterEqual(score, 0)
        self.assertLessEqual(score, 1)
        print("Le score est bien entre 0 et 1")
        
if __name__ == '__main__':
    unittest.main()