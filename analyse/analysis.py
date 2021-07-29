import pandas as pd
import sys

#Naive Basic Overlap
basic_words_to_total = lambda list_basic_words, list_all_words : \
					round(list_basic_words / list_all_words,3)

def proportion_simple_naive(data, ling_type=None, as_length=True):
	filtered_rows = None
	all_rows = None

	if ling_type == None:
		filtered_rows = data[(data['is_simple'] == True)]
		all_rows = data
	else:
		filtered_rows = data[(data['type'] == ling_type) & (data['is_simple'] == True)]
		all_rows = data[data['type'] == ling_type]

	if as_length:
		return len(filtered_rows), len(all_rows)
	else:
		return filtered_rows, all_rows

def proportion_simple_nonnaive(data, ling_type=None):
	filtered_rows, all_rows = proportion_simple_naive(data, ling_type, as_length=False)

	occurrences_type_and_simple = filtered_rows['freq'].sum()
	occurrences_type_and_all = all_rows['freq'].sum()

	return occurrences_type_and_simple, occurrences_type_and_all

def results(data, ling_type=None):
	#Get Naive & Non-Naive Results
	A, B = proportion_simple_naive(complete_data, ling_type)
	C, D = proportion_simple_nonnaive(complete_data, ling_type)

	print("--Naive--")
	print("Type: ", ling_type)
	print("Simple: ", A)
	print("All: ", B)
	print(basic_words_to_total(A, B))

	print('\n--Non-Naive--')
	print("Type: ", ling_type)
	print("Simple: ", C)
	print("All: ", D)
	print(basic_words_to_total(C, D))
	print("\n-----------------\n")

if __name__ == "__main__":
	ling_types = ['NOUN', 'VERB', 'ADJ', 'PROPN', 'ADV']

	#Example: 'csv/cs_terms/cs50_foldoc_cs_terms.csv'
	in_path = sys.argv[1]

	complete_data = pd.read_csv(in_path)

	results(complete_data)

	for pos in ling_types:
		results(complete_data, pos)
