import pandas as pd
import pickle
import sys

#Form plural of a given noun singular
def get_plural(singular):
		return singular + 's'

if __name__ == "__main__":
	#Argument 1: Our input data from which we would like to
	#combine any plurals
	in_path = sys.argv[1]

	#Argument 2: Our output path to store the data 
	#with all plurals combined
	out_path = sys.argv[2]

	#Where to store a record of all removed plurals
	removed_elements = "out/plural_groups.csv"

	data = pd.read_csv(in_path)

	plural_groups = []

	for s_index, row in data.iterrows():
		singular = row['word']
		ling_type = row['type']
		s_freq = row['freq']

		if ling_type == 'NOUN':
			for p_index, potential_plural in data.iterrows():
				plural = potential_plural['word']
				p_freq = potential_plural['freq']

				if plural == get_plural(singular):
					plural_groups.append([singular, plural])
					data.drop(p_index, inplace=True)
					s_freq += p_freq
					data.at[s_index, 'freq'] = s_freq

	#Save data but with no plurals
	data.to_csv(out_path)

	#Save the plurals that were removed to a file
	with open(removed_elements, 'w+') as f:
		f.write(str(plural_groups))