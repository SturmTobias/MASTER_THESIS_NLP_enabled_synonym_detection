import nlpaug.augmenter.char as nac
import nlpaug.augmenter.word as naw
import nlpaug.augmenter.sentence as nas
import nlpaug.flow as nafc
from nlpaug.util import Action
import nltk
from nltk.corpus import wordnet
import nltk
import os
import csv
import pandas as pd
import numpy as np


# Defining source and output directions
source_file = 'labels_BPIC12.xlsx'
source_path = '/Users/tobisturm/Library/CloudStorage/OneDrive-UniversitätBayreuth/01 Masterarbeit/03 Data/01 Logs/01_event_labels/{}'.format(source_file)

output_file = 'labels_BPIC12_aug.csv'
output_path = '/Users/tobisturm/Library/CloudStorage/OneDrive-UniversitätBayreuth/01 Masterarbeit/03 Data/01 Logs/01_event_labels/augmented_logs/{}'.format(output_file)

# Reading excel file with activity labels
excel = pd.read_excel(source_path)
excel.head()

# Exporting activity labels from dataframe to a list
text = excel['Label'].tolist()

def input_labels(list_of_activity_labels):
    print('The following activity labels were imported:')
    for i in text:
        print(i)
    return

input_labels(text)

# First attempts showed that quality of augmentations are better, when input strings are of lower cases only
# Therefore converting all elements of input list into lower cases before inputting in augmenting engine

text_cap = []
for i in text:
    without = i.lstrip()
    capitalized = without.lower()
    text_cap.append(capitalized)

print(text_cap)

# Setting up the wordnet augmenting enginge and save it in var 'aug'
aug = naw.SynonymAug(aug_src='wordnet')

# Retrieving 10 synonymous activity labels per input activity label (n=10)
augmented_text = []
for i in text_cap:
    augmented_text.append(aug.augment(i, n=10))

# Flattening list of lists to get all unique activity labels as single elements
augmented_unique = []
for i in augmented_text:
    for j in i:
        augmented_unique.append(j)

print('The list augmented_unique contains {} items'.format(len(augmented_unique)))

# Zipping the list of all input labels (text_cap) with the list of augmentations (augmented_unique)
zipped = text_cap + augmented_unique
print(zipped)
print(len(zipped))

# Converting the zipped list into pandas dataframe and dropping out duplicates
# since the augmenting enginge generates the same synonyms sometimes
df = pd.DataFrame(augmented_unique, columns = ['augmented_labels'])
df_without_duplicates = df.drop_duplicates(subset=['augmented_labels'])
df_without_duplicates

# Saving dataframe without duplicates as .csv file
df_without_duplicates.to_csv(output_path, sep=';')