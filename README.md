<br />
<p align="center">

  <h3 align="center">Words We Use</h3>

  <p align="center">
    Transcription Processing Tools for "Simple English" Analysis
  </p>
</p>

<!-- ABOUT THE PROJECT -->
## About The Project
Analysing how native English speakers communicate tricky concepts to non-native speakers is an important part of understanding how we can improve education in any area. This project provides a set of tools which process and analyse a series of lectures, tutorials, or any other educational content. This is with the intention of understanding how we can potentially improve our teaching practices in an environment where not everyone is a native speaker of a language.

There are two stages to the analysis of a set of transcripts. Firstly, the processing stage will take the raw transcript data and generate a CSV file containing the used words, their number of occurrences, their part-of-speech (POS) and whether they are "simple". This data will be cleaned and will remove punctuation and numbers.

Then comes the analysis stage. Here we produce information about the proportion of simple English to all words, given a set of filters. These filters can be based on POS, for instance only taking into account nouns, or based on whether we want to take into account only unique occurrences of words or not.

### Processing Pipeline
1. Condense Set Of Transcriptions → Merges text files / folder of transcriptions into one.
2. Word-Frequency Pairs → Store the frequency of each word.
3. Part-Of-Speech Tagging → Store the type of word. Ex: noun, verb, adverb, etc.
4. Combine Singular & Plurals → Combine any noun plurals with their singular.
5. Order Data By Frequency → Sort the data by word frequency.
6. Extract Computer Science Terms → Extract any CS-related terms. Can be based on FOLDOC or CS1.

### Built With
* [Pandas](https://pandas.pydata.org/)
* [SpaCy](https://spacy.io/)

<!-- GETTING STARTED -->
## Getting Started
In order to run these tools on a set of transcriptions, run the following commands from the command line.

    python process_suite.py [FOLDER_WITH_TRANSCRIPTIONS]
    python analysis_suite.py

## Example Analysis Output
<pre>

Analysis: Complete
--Naive-- (All)
Type:  None
Simple:  155
All:  571
0.271

--Non-Naive-- (Only Unique)
Type:  None
Simple:  2562
All:  4979
0.515

-----------------

--Naive-- (All)
Type:  NOUN
Simple:  31
All:  106
0.292

--Non-Naive-- (Only Unique)
Type:  NOUN
Simple:  211
All:  575
0.367

-----------------

--Naive-- (All)
Type:  VERB
Simple:  36
All:  211
0.171

--Non-Naive-- (Only Unique)
Type:  VERB
Simple:  356
All:  994
0.358

-----------------

--Naive-- (All)
Type:  ADJ
Simple:  21
All:  52
0.404

--Non-Naive-- (Only Unique)
Type:  ADJ
Simple:  66
All:  146
0.452

...

-----------------

Analysis: Computer Science Terms
...

Data Analysis Complete!</pre>
