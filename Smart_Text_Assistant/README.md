# Smart Text Assistant (CLI-Based NLP Project)

## Objective

The objective of this project is to develop a CLI-based Smart Text Assistant that performs basic Natural Language Processing (NLP) tasks such as dictionary lookup, spelling correction, and next-word prediction. The system demonstrates how rule-based methods, statistical modeling, and frequency-based techniques can be combined to build an intelligent text assistant.

## Features

- Dictionary Lookup (Meaning + Synonyms)
- Spelling Correction with user confirmation
- Next Word Prediction based on input context
- Hybrid NLP approach:
  - Rule-based system
  - Trigram language model
  - Frequency-based fallback system

## Technologies Used

- Python 3.x
- NLTK (Natural Language Toolkit)
- wordfreq library
- textblob library
- Trigram (N-gram) Language Model
- Rule-based NLP logic

## Workflow

1. User enters a word or sentence via CLI
2. Input is tokenized and validated using NLTK
3. Based on input type:
   - Single word → Dictionary lookup + Spelling correction
   - Sentence → Next word prediction
4. Prediction pipeline:
   - Trigram model checks context
   - Rule-based system handles fixed patterns
   - wordfreq provides fallback suggestions
5. Final output is displayed to the user


## Sample Outputs

Input: sarry  
Did you mean 'sorry'? (y/n)

Input: happy  
Meaning: feeling or showing pleasure  
Synonyms: glad, joyful, pleased

Input: I am feeling  
Suggestions: happy, sad, tired, good

## Conclusion

This project demonstrates a hybrid NLP system combining rule-based logic, trigram modeling, and frequency-based word prediction. It provides a strong foundation for understanding core natural language processing techniques.

