import requests


"""

    Get Questions from https://opentdb.com/api_config.php
    Remove the upper dictionary and leave the rest as it is

"""


class Data:
    def __init__(self):
        self.question_data = []
        self.parameters = {
            "amount": 10,
            "difficulty": "easy",
            "type": "boolean"
        }

    def load_questions_from_api(self):
        response = requests.get("https://opentdb.com/api.php", params=self.parameters)
        response.raise_for_status()
        self.question_data = response.json()["results"]
        return self.question_data
        #print(self.question_data)


question_data = [
    {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
     "question": "The Great Wall of China is visible from the moon.", "correct_answer": "False",
     "incorrect_answers": ["True"]},
    {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "easy",
     "question": "The Indie Game Development Studio Cing, developers of Hotel Dusk and Last Window, went bankrupt on March 1st, 2010.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "medium",
     "question": "DragonForce&#039;s &#039;Through the Fire and Flames&#039; is widely considered to be the hardest song in the Guitar Hero series.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Entertainment: Board Games", "type": "boolean", "difficulty": "medium",
     "question": "In the game &quot;Racko&quot; you may pick up ANY card from the discard pile.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Science & Nature", "type": "boolean", "difficulty": "medium",
     "question": "Like with the Neanderthals, Homo sapiens sapiens also interbred with the Denisovans.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Science: Mathematics", "type": "boolean", "difficulty": "medium",
     "question": "The proof for the Chinese Remainder Theorem used in Number Theory was NOT developed by its first publisher, Sun Tzu.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Science: Mathematics", "type": "boolean", "difficulty": "medium",
     "question": "111,111,111 x 111,111,111 = 12,345,678,987,654,321", "correct_answer": "True",
     "incorrect_answers": ["False"]}, {"category": "Science: Mathematics", "type": "boolean", "difficulty": "hard",
                                       "question": "If you could fold a piece of paper in half 50 times, its&#039; thickness will be 3\/4th the distance from the Earth to the Sun.",
                                       "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "easy",
     "question": "The PlayStation was originally a joint project between Sega and Sony that was a Sega Genesis with a disc drive.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Vehicles", "type": "boolean", "difficulty": "easy",
     "question": "The full English name of the car manufacturer BMW is Bavarian Motor Works", "correct_answer": "True",
     "incorrect_answers": ["False"]}, {"category": "Vehicles", "type": "boolean", "difficulty": "medium",
                                       "question": "When BMW was established in 1916, it was producing automobiles.",
                                       "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "easy",
     "question": "In Terraria, you can craft the Cell Phone pre-hardmode.", "correct_answer": "True",
     "incorrect_answers": ["False"]}, {"category": "Entertainment: Music", "type": "boolean", "difficulty": "medium",
                                       "question": "For his performance at ComplexCon 2016 in Long Beach, California, Skrillex revived his &quot;Mothership&quot; set piece for one night only.",
                                       "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "General Knowledge", "type": "boolean", "difficulty": "medium",
     "question": "&quot;Buffalo buffalo Buffalo buffalo buffalo buffalo Buffalo buffalo.&quot; is a grammatically correct sentence.",
     "correct_answer": "True", "incorrect_answers": ["False"]}]
