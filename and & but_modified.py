import glob
import nltk
from nltk.tokenize import word_tokenize
from collections import Counter
import os

nltk.download('punkt')

def is_case_marker(word):

    case_markers = ['के', 'का', 'को', 'से', 'में', 'ने', 'लिए', 'पर', 'हें', 'अरे', 'की']
    return word in case_markers

def is_and_clause(word):
    and_clause = ['और', 'या', 'लेकिन', 'परन्तु', 'क्यूंकि']
    return word in and_clause
def is_but_clause(word):
    but_clause = ['लेकिन','परन्तु','क्यूंकि']
    return word in but_clause


def calculate_token_type_ratio(tokens):
    token_counts = Counter(tokens)
    token_type_ratio = len(token_counts) / len(tokens)
    return token_type_ratio

def calculate_token_type_ratio_with_case_markers(tokens):
    case_markers = []
    for token in tokens:
        if is_case_marker(token):
            case_markers.append(token)
    case_marker_percentage = (len(case_markers) / len(tokens)) * 100
    token_type_ratio = calculate_token_type_ratio(tokens)
    return case_markers, case_marker_percentage, token_type_ratio

def calculate_token_type_ratio_with_and_clause(tokens):
    and_clause = []
    for token in tokens:
        if is_and_clause(token):
            and_clause.append(token)
    and_clause_percentage = (len(and_clause) / len(tokens)) * 100
    token_type_ratio = calculate_token_type_ratio(tokens)
    return and_clause, and_clause_percentage, token_type_ratio





def calculate_token_type_ratio_with_but_clause(tokens):
    but_clause = []
    for token in tokens:
        if is_but_clause(token):
            but_clause.append(token)
    but_clause_percentage = (len(but_clause) / len(tokens)) * 100
    token_type_ratio = calculate_token_type_ratio(tokens)
    return but_clause, but_clause_percentage, token_type_ratio







def calculate_token_type_ratio_multiple_files(directory_path):
    token_type_ratios = []
    case_markers_list = []
    case_marker_percentages = []
    and_clause_list = []
    and_clause_percentages = []
    but_clause_list = []
    but_clause_percentages = []
    for file_name in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file_name)
        _files = [file_path]
        token_type_ratios_folder = []
        sentence_length_folder = []
        avg_sentences_folder = []
        for _file_path in _files:
            if os.path.isfile(_file_path):
                with open(_file_path, 'r', encoding='utf-8') as file:
                    text = file.read()
                    sentence_length_folder.append(len(text.split()) / len(text.split('\n')))
                    avg_sentences_folder.append(len(text.split('\n')))
                    tokens = word_tokenize(text)


                    case_markers, case_marker_percentage, token_type_ratio = calculate_token_type_ratio_with_case_markers(tokens)
                    case_markers_list.extend(case_markers)
                    case_marker_percentages.append(case_marker_percentage)



                    and_clause ,and_clause_percentage ,token_type_ratio = calculate_token_type_ratio_with_and_clause(tokens)
                    and_clause_list.extend(and_clause)
                    and_clause_percentages.append(and_clause_percentage)

                    but_clause, but_clause_percentage, token_type_ratio = calculate_token_type_ratio_with_but_clause(tokens)
                    but_clause_list.extend(but_clause)
                    but_clause_percentages.append(but_clause_percentage)

                    token_type_ratios.append(token_type_ratio)
                    token_type_ratios_folder.append(token_type_ratio)

                    #print(f"{_file_path}: Token Type Ratio = {token_type_ratio:.4f}")
        #print(f"{file_name}: Token Type Ratio = {sum(token_type_ratios_folder)/len(token_type_ratios_folder):.4f}")
    print(f"{directory_path}: Token Type Ratio = {sum(token_type_ratios) / len(token_type_ratios):.4f}")
    print(f"{directory_path}: Avg Sentences per file = {sum(avg_sentences_folder) / len(avg_sentences_folder):.4f}")
    print(f"{directory_path}: Avg Sentence Length = {sum(sentence_length_folder) / len(sentence_length_folder):.4f}")
    print(f"{directory_path}: Case Marker Percentage = {sum(case_marker_percentages) / len(case_marker_percentages):.2f}%")
    print(f"{directory_path}: and_clause Percentage = {sum(and_clause_percentages)/len(and_clause_percentages):.2f}%")
    print(f"{directory_path}: but_clause Percentage = {sum(but_clause_percentages)/len(but_clause_percentages):.2f}%")
    return case_markers_list, case_marker_percentages , and_clause_list , and_clause_percentages , but_clause_list, but_clause_percentages





directory_path = r"C:\Users\Tanvi Kandalla\Desktop\Spoken Hindi Project\HUTB\Comparison"
case_markers, case_marker_percentages, and_clause, and_clause_percentages, but_clause, but_clause_percentages = calculate_token_type_ratio_multiple_files(directory_path)





#print(f"List of case markers: {case_markers}")
#print(f"Average Case Marker Percentage: {sum(case_marker_percentages) / len(case_marker_percentages):.2f}%")
#print("Average Conjunction Percentage : {sum(conjunction_percentages) / len(conjunction_percentages): .2f}%")







