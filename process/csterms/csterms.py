import pandas as pd
import sys

CS_ONE = 'process/csterms/data/CS1_words.csv'
FOLDOC = 'data/compwords.csv'

if __name__ == "__main__":
	#Argument 1: The data to extract CS terms from
	in_path = sys.argv[1]

	#Argument 2: Where to store our final output CSV file
	out_path = sys.argv[2] 

	#Insert here the specific CS-term dictionary path
	compwords = pd.read_csv(FOLDOC)['0'].tolist()

	data = pd.read_csv(in_path)

	found_comp_words = []

	for index, row in data.iterrows():
		
		#Separate and store each feature
		word = row['word']
		ling_type = row['type']
		freq = row['freq']
		is_simple = row['is_simple']

		if word in compwords:
			cs_term_row = [word, ling_type, freq, is_simple]
			found_comp_words.append(cs_term_row)

	found_cs_df = pd.DataFrame(found_comp_words, columns=['word','type','freq','is_simple'])
	found_cs_df.to_csv(out_path)
