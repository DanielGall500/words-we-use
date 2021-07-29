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
	order_out = "out/complete/complete_data.csv"
	csterms_out = "out/complete/csterms_data.csv"

	# Analysis
	c1 = "python analyse/analysis.py {}".format(order_out)
	c2 = "python analyse/analysis.py {}".format(csterms_out)

	print("Analysing Data...")
	commands = [c1, c2]
	analysis_titles = ["Complete", "Computer Science Terms"]
	for i, c in enumerate(commands):
		print("\n\nAnalysis: {}".format(analysis_titles[i]))
		os.system(c)
	print("Data Analysis Complete!")