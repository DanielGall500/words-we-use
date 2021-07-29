import os
import sys

"""
Process
1. Condense Set Of Transcriptions
2. Word-Frequency Pairs
3. Part-Of-Speech Tagging
4. Remove Plurals
5. Order Data By Frequency
6. Extract Computer Science Terms

Analysis
1. Perform POS Analysis On Final Data
2. Perform POS Analysis On CS Terms
3. Store Final Results
"""

if __name__ == "__main__":

	#The folder containing all relevant transcriptions
	#For example, it may contain ten transcription files from a lecture series.
	in_folder_path = sys.argv[1]

	##Text Condenser: Merges Text Files Into One
	condense_in = in_folder_path
	condense_out = "out/condensed.txt"
	c1 = "python process/condense/txtcondenser.py {} {}".format(condense_in, condense_out)

	#Store The Frequency Of Each Word
	wordfreq_out = "out/wordfreq.csv"
	c2 = "python process/wordfreqpairs/wordfreqpairs.py {} {}".format(condense_out, wordfreq_out)

	#Part-Of-Speech Tagging: Store the type of word. Ex: Noun, Verb, Adverb, etc.
	pos_out = "out/pos.csv"
	c3 = "python process/pos/pos.py {} {}".format(wordfreq_out, pos_out)

	#Combine any noun plurals with their singular
	plurals_out = "out/plurals.csv"
	c4 = "python process/plurals/combine_plurals.py {} {}".format(pos_out, plurals_out)

	#Sort the data by word frequency
	order_out = "out/complete/complete_data.csv"
	c5 = "python process/order/order_data.py {} {}".format(plurals_out, order_out)

	#Extract any CS-related terms. Can be based on FOLDOC or CS1. 
	cs_terms_out = "out/csterms_out.csv"
	c6 = "python process/csterms/csterms.py {} {}".format(order_out, csterms_out)

	#Execute the commands
	commands = [c1, c2, c3, c4, c5, c6]
	for c in commands:
		print("Executing Command: {}".format(c))
		os.system(c)
		print("Execution Complete")
