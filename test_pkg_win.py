# -*- coding: utf-8 -*-
"""
Test for the knowmine main module

"""

from knowmine import extract_relevant_sentences


main_terms = ['toxicity', 'acute', 'LC50', 'EC50']

relation_words = ["predict"]


def main():
    folder_path = "C:/Users/gulsha/Desktop/Toxicity 2018-2020/"
    extract_relevant_sentences(folder_path, main_terms,
                               relation_words, "db", 3)


if __name__ == '__main__':
    main()
