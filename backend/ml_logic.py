import random
import secrets
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer


class Mediator:
    def __init__(self, words):
        self.target_word = ""
        self.words = words
        self.human_won = False
        self.machine_won = False
    def emit(self,words):
      self.target_word = secrets.choice(words)
      return self.target_word

    def get_feedback(self, guess):
        feedback = []
        for g, t in zip(guess, self.target_word):
            if g == t:
                feedback.append("green")
            elif g in self.target_word:
                feedback.append("yellow")
            else:
                feedback.append("gray")
        return feedback

    def validate_guess(self, guess):
        if guess in self.words:
            return True
        return False




class HumanPlayer:
    def make_guess(self):
        return 1


class MachinePlayer:
    def __init__(self, words):
        self.words = words
        self.X, self.vectorizer = self.preprocess(words)
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.model.fit(self.X, np.arange(len(words)))
        self.candidates = words[:]

    def preprocess(self, words):
        vectorizer = CountVectorizer(analyzer="char", ngram_range=(1, 1))
        X = vectorizer.fit_transform(words).toarray()
        return X, vectorizer

    def make_guess(self, feedback=None, previous_guess=None):
        if feedback and previous_guess:
            self.candidates = self.filter_candidates(self.candidates, previous_guess, feedback)
        candidate_indices = [self.words.index(word) for word in self.candidates]
        return self.words[np.random.choice(candidate_indices)]

    def filter_candidates(self, candidates, guess, feedback):
        new_candidates = []
        for word in candidates:
            match = True
            for i, (g, f) in enumerate(zip(guess, feedback)):
                if f == "green" and word[i] != g:
                    match = False
                    break
                elif f == "yellow" and (g not in word or word[i] == g):
                    match = False
                    break
                elif f == "gray" and g in word:
                    match = False
                    break
            if match:
                new_candidates.append(word)
        return new_candidates



if __name__ == "__main__":
    pass
