from transcription_parser import SimpleEnglishParser
import sys
import os

if __name__ == "__main__":
	in_path = sys.argv[1]
	out_path = sys.argv[2]

	with open(in_path, 'r') as f:
		text = f.read()

	basic_words_path = 'res/basic_english.txt'
	parser = SimpleEnglishParser(basic_words_path)
	df = parser.parse_text(text)

	sorted_by_freq = df.sort_values(by=["freq"], ignore_index=True)
	sorted_by_freq.to_csv(out_path)

	

	



