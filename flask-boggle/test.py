from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

def setup(self):

    app.config['TESTING'] = True
    self.client = app.test_client()
def test_for_valid_word(self):
"""Testing for an entry on the board that contains a valid word"""
    with self.client as client:
        with client.session_transaction as session:
            session['board'] = [["F", "I", "L", "E", "S"], 
                                ["F", "I", "L", "E", "S"], 
                                ["F", "I", "L", "E", "S"], 
                                ["F", "I", "L", "E", "S"], 
                                ["F", "I", "L", "E", "S"]]
    resp = self.client.get('/check-word?word=files')
    self.assertEqual(resp.json['result'], 'ok')

def test_for_invalid_word(self):
"""checking for invalid word that """
    self.client.get('/')
    resp = self.client.get('/check-word?word=rectangle')
    self.assertEqual(resp.json['result'], 'no-on-board')

def test_not_in_dict(self):
    """check if word entered is not in the Boggle Dictionary"""

    self.client.get('/')
    resp = self.client.get('/check-word?word=recatngel')
    self.assertEqual(response.json['result'], 'not-word')


def test_page(self):
    """Testing the web page by checking proper session and html is shown"""

    with self.client:
        resp = self.client.get('/')
        self.assertIn('board', session)
        self.assertIsNone(session.get('highscore'))
        self.assertIn(b'<p>High Score:', resp.data)
        self.assertIsNone(session.get('plays'))
        self.assertIn(b'Count Down:', resp.data)
        self.assertIn(b'Score:', resp.data)
    # TODO -- write tests for every view function / feature!

