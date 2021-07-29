import pandas as pd
import os
import sys

if __name__ == "__main__":
	in_path = sys.argv[1]
	out_path = sys.argv[2]

	data = pd.read_csv(in_path)
	data = data.sort_values('freq', ascending=False)

	data.to_csv(out_path)