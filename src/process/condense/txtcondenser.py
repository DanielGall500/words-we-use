from os import listdir
from os.path import isfile, join
from spacy.lang.en import English
import sys

class TextFileCondenser:
	def __init__(self, save_path):
		self.save_path = save_path
		self.lang_parser = English()
	
	def condense(self, folder):
		files = [file for file in listdir(folder) \
		if isfile(join(folder,file))]

		file_texts = []

		for file in files:
			text = self.text_from_file(file, folder)
			file_texts.append(text)

		all_words = []
		for text in file_texts:
			for line in text:
				#Skip empty lines
				if line == '\n':
					continue

				tokens = self.lang_parser(line)
				tokens = [str(t) for t in tokens if str(t) != '\n']
				all_words.extend(tokens)

		with open(self.save_path, 'w+') as f:
			for word in all_words:
				f.write(word + " ")


	def text_from_file(self, file, folder=None):
		path = join(folder,file) if folder else file

		with open(path, 'r') as f:
			lines = f.readlines()
		return lines

	def _remove_newlines(text):
		return re.sub(r"\n", '', text)

if __name__ == "__main__":
	in_folder = sys.argv[1]
	out_path = sys.argv[2]

	file_condenser = TextFileCondenser(out_path)
	file_condenser.condense(in_folder)


