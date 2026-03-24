# Spam Email/SMS Detector

##  Project Description
The Spam Email/SMS Detector is a machine learning-based project that classifies messages as spam or not spam (ham). With the increasing use of digital communication, unwanted and fraudulent messages have become very common. This project helps in automatically detecting such spam messages.
The system uses Natural Language Processing (NLP) techniques to analyze the text data. It converts the input message into numerical form using CountVectorizer and applies the Naive Bayes algorithm for classification.


## Objective
- To detect spam messages using machine learning  
- To apply NLP techniques for text classification  
- To build a simple and interactive prediction system  


##  Tools & Technologies Used
- Python  
- Pandas  
- Scikit-learn  
- NLTK  
- VS Code  

## Methodology
1. Load dataset (spam.csv)  
2. Data preprocessing (cleaning & formatting)  
3. Convert text into numerical data using CountVectorizer  
4. Split data into training and testing sets  
5. Train model using Naive Bayes algorithm  
6. Evaluate model accuracy  
7. Take user input and predict spam or not spam  


## Output
- The system takes a message as input  
- It predicts whether the message is:
  - Spam  
  - Not Spam (Ham)  


## How to Run the Project
1. Install required libraries:
  pip install pandas numpy scikit-learn nltk
2. Run the program:
   python main.py
3. Enter any message to check prediction
   
   Example:
   Enter a message: Win a free iPhone now!!!
   Prediction: spam

## Conclusion
This project demonstrates how machine learning and NLP can be used to detect spam messages effectively. It provides a simple and practical solution to filter unwanted messages.


