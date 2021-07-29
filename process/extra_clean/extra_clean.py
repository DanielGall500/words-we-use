import pandas as pd
import string
import sys

if __name__ == "__main__":

	#Example: 'csv/complete_no_plurals/pd_complete_no_plurals.csv'
	in_path = sys.argv[1]

	#Example: 'pd_complete_no_plurals_ordered.csv'
	out_path = sys.argv[2]

	df = pd.read_csv(in_path)

	#Filter out numbers & punctuation
	for index, row in df.iterrows():
		word = str(row['word'])
		is_punctuation = (word in string.punctuation)

		if word.isnumeric() or is_punctuation:
			df.drop(index, inplace=True)

	df.to_csv(out_path)



