# Systematic_Comparision_between_Spoken_and_Written_Hindi
This aims to bridge the gap between written and spoken language by systematically mapping the differences and variations that arise in different linguistic contexts.
README

Systematic Comparison between Spoken and Written Hindi
This code is designed to perform a systematic comparison between spoken and written Hindi. It calculates various linguistic attributes and provides insights into the distinctions between spoken and written data.

Prerequisites
Python 3.x
NLTK (Natural Language Toolkit) library
Setup and Usage
Install Python 3.x on your system.
Install the NLTK library by running the following command:

pip install nltk
Download the necessary NLTK data by executing the following code:
python

import nltk
nltk.download('punkt')
Copy and paste the provided code into a Python file (e.g., comparison.py).
Adjust the directory_path variable to specify the directory containing the Hindi text files for comparison. Ensure that the directory path uses the correct file path syntax for your operating system.
Run the Python script.
Functionality
The code provides the following functionality:

Calculation of token type ratio: This ratio measures the diversity of unique tokens in a given text.
Analysis of case markers: Identification of case markers and calculation of their percentage within the tokens.
Analysis of conjunctions: Identification of conjunctions and calculation of their percentage within the tokens.
Calculation of average sentence length and average number of sentences per file.
Output
Upon running the code, the following information will be displayed:

Token Type Ratio: The average token type ratio for all files in the specified directory.
Average Sentences per File: The average number of sentences per file in the specified directory.
Average Sentence Length: The average length of sentences in terms of token count.
Case Marker Percentage: The average percentage of case markers within the tokens.
Conjunction Percentage: The average percentage of conjunctions within the tokens.
Note
Please ensure that the directory specified in the directory_path variable contains the appropriate Hindi text files for comparison.

For any questions or assistance, please contact Aadya Ranjan at aadyaranjan83@gmail.com.
