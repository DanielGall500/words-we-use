import pandas as pd
import spacy
import sys

if __name__ == "__main__":

	#Argument 1: Our path to the word-frequency input data
	in_path = sys.argv[1]

	#Argument 2: Our path for where we should store our output POS Tagging
	out_path = sys.argv[2]

	data = pd.read_csv(in_path)
	nlp = spacy.load('en_core_web_sm')

	complete_data = []

	for index, row in data.iterrows():
		word = str(row['word'])
		freq = row['freq']
		is_simple = row['is_simple']
		pos = 'None'

		for token in nlp(word):
			#Get Part-Of-Speech Tag
			pos = token.pos_

		complete_data.append([word, pos, freq, is_simple])

	df = pd.DataFrame(complete_data, columns=['word', 'type', 'freq', 'is_simple'])
	df.to_csv(out_path)

