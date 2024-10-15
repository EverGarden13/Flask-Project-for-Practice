import unittest
from emotion_app import emotion_predictor

class TestEmotionPredictor(unittest.TestCase):

    def test_emotion_prediction(self):
        text = "I feel sad and angry."
        result, status_code = emotion_predictor(text)
        self.assertEqual(status_code, 200)
        self.assertIn('anger', result)
        self.assertIn('joy', result)

    def test_empty_input(self):
        text = ""
        result, status_code = emotion_predictor(text)
        self.assertEqual(status_code, 400)
        self.assertIn('error', result)

if __name__ == '__main__':
    unittest.main()
