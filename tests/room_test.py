import json
import unittest
import sys
import os
from app import app
from bulbs.bulbs_fill import RoomFill

app.testing = True


class TestApi(unittest.TestCase):
    """
    Test cases
    """

    def test_success(self):
        with app.test_client() as client:
            result = client.get('/bulbs_status/?filename=test1.txt')
            self.assertEqual(result.status_code, 200)

    def test_fail(self):
        with app.test_client() as client:            
            result = client.get('/bulbs_status/?filename=test.txt')
            self.assertEqual(result.status_code, 404)

    def test_context(self):
        sys.path.append(os.getcwd())
        with open("tests/data/result.txt", "r") as f:
            l = [line.split() for line in f]
            lines = [list( map(int,i) ) for i in l]        
        room = RoomFill('test1.txt')
        data = room.bulbs()         
        self.assertEqual(data.tolist(), lines)
        


if __name__ == "__main__":
    unittest.main()
