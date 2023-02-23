import unittest
from main import getScoreUtilisateur

#Numéro identifiant du client dont on teste le score
NUM_ID = 100002

class TestScore(unittest.TestCase):

    #Fonction qui teste si le score renvoyé est bien entre 0 et 1
    def test_is_score_between_0_and_1(self):  
        score=getScoreUtilisateur(NUM_ID)
        self.assertGreaterEqual(score, 0)
        self.assertLessEqual(score, 1)
        print("Le score est bien entre 0 et 1")
        
if __name__ == '__main__':
    unittest.main()