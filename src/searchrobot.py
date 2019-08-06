#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import wikipedia as wiki
from nltk import tokenize
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions

class SearchRobot():

    def __init__(self):
        self.keywords_list = []
        self.sentences_number = 7

        self.natural_language_understanding = NaturalLanguageUnderstandingV1(
                version = "2019-07-12",
                iam_apikey = "RMVmwXLQDwTE4qQ5oIN9_k0HLD8CwU8NK6NhYDaOZqU8",
                url = "https://gateway.watsonplatform.net/natural-language-understanding/api")

    def search(self, search_term):
        summary = wiki.summary(search_term, sentences = 7)
        summary = re.sub(r"\([^)]*\)", "", summary)

        return tokenize.sent_tokenize(summary)

    def get_keywords(self, sentences):
        for sentence in sentences:
            response = self.natural_language_understanding.analyze(text = sentence,
                    features = Features(
                        keywords = KeywordsOptions(emotion = True, sentiment = True,
                            limit = 2))).get_result()

            temp_list = []
            for keyword in response["keywords"]:
                temp_list.append(keyword["text"])

            self.keywords_list.append(temp_list)

        return self.keywords_list
