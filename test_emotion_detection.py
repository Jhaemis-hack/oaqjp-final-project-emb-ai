from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
        self.assertEqual(emotion_detector("I love working with python").get("label"), "SENT_POSITIVE"),
        self.assertEqual(emotion_detector("I hate working with python").get("label"), "SENT_NEGATIVE"),
        self.assertEqual(emotion_detector("I am neutral on python").get("label"),"SENT_NEUTRAL")


unittest.main()
