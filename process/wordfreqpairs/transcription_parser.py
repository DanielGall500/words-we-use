from spacy.lang.en import English
import pandas as pd
import os

class SimpleEnglishParser:
	def __init__(self, basic_words_path):
		self.lang_tokeniser = English()

		#Retrieve our basic words from the file
		with open(basic_words_path, 'r') as bw_file:
			words = bw_file.readlines()[0]

		self.basic_english = self._preprocess(words)

	def parse_text(self, text):
		tokens = self._preprocess(text)
		vocab = self._get_vocab(tokens)
		freq = self._get_frequencies(vocab, tokens)
		is_simple = self._get_is_simple(vocab)

		return pd.DataFrame({"word" : vocab, \
							 "freq": freq, \
							 "is_simple": is_simple})

	def _get_vocab(self, tokens):
		return list(set(tokens))

	def _get_frequencies(self, vocab, full_text):
		freq = []
		for word in vocab:
			count = full_text.count(word)
			freq.append(count)
		return freq

	def _get_is_simple(self, vocab):
		is_simple = []
		for word in vocab:
			is_in_basic_english = (word in self.basic_english)
			is_simple.append(is_in_basic_english)
		return is_simple

	def _preprocess(self, text):
		parse_by_lang = self.lang_tokeniser(text)
		return (parse_by_lang.text.lower()).split()