# Arabic Text Analysis with TextBlob and TextBlob-AR

This repository demonstrates how to perform basic text analysis tasks—such as tokenization and sentiment analysis—on Arabic text using the `TextBlob` library and its Arabic extension, `textblob_ar`. The code is simple, modular, and beginner-friendly, making it a great starting point for working with Arabic NLP.

---

## **Features**
1. **Tokenization**:
   - Splits Arabic text into individual words (tokens).
2. **Sentiment Analysis**:
   - Analyzes the sentiment of Arabic text using the `textblob_ar` extension.
3. **Lightweight and Easy to Use**:
   - Requires minimal setup and leverages the familiar `TextBlob` API.

---

# NB: You can train your Neural Network or create your own extension the possibilities are open

Why Train Your Own Model?
While textblob_ar is a great starting point, training your own neural network or creating custom extensions allows you to:

Achieve higher accuracy for your specific domain or dataset.
Incorporate unique linguistic nuances of Arabic dialects or industry-specific terminology.
Scale your solution to handle complex tasks like multi-label classification or aspect-based sentiment analysis.

## **Dependencies**
To run this code, ensure you have the following Python libraries installed:

- `textblob`
- `textblob-extensions` (`textblob_ar`)

You can install the required libraries using `pip`:
```bash
pip install textblob textblob-extensions
```

---

## **Usage**

### **Step 1: Clone the Repository**
Clone this repository to your local machine:
```bash
git clone https://github.com/wzayed/arabic-text-analysis.git
cd arabic-text-analysis
```

### **Step 2: Run the Code**
The code performs two main tasks:
1. **Tokenization**: Splits Arabic text into words.
2. **Sentiment Analysis**: Predicts the sentiment polarity and subjectivity of the text.

#### Example Usage
```python
from textblob import TextBlob
from textblob_ar import TextBlobAR

# Sample Arabic text
arabic_text = "المطعم جيد"

# Create a TextBlobAR object
blob = TextBlobAR(arabic_text)

# Tokenization
tokens = blob.words
print("Tokens:", tokens)

# Sentiment Analysis
sentiment = blob.sentiment
print("Sentiment:", sentiment)
```

#### Expected Output
```
Tokens: ['المطعم', 'جيد']
Sentiment: Sentiment(polarity=0.5, subjectivity=0.6)
```

---

## **Code Explanation**

### **Tokenization**
The `blob.words` method splits the input Arabic text into individual words (tokens). This is useful for preprocessing tasks like stopword removal or frequency analysis.

Example:
```python
tokens = blob.words
print(tokens)  # Output: ['المطعم', 'جيد']
```

### **Sentiment Analysis**
The `blob.sentiment` method provides two metrics:
- **Polarity**: A float value between `-1.0` (negative) and `1.0` (positive), indicating the sentiment orientation.
- **Subjectivity**: A float value between `0.0` (objective) and `1.0` (subjective), indicating the degree of personal opinion or emotion in the text.

Example:
```python
sentiment = blob.sentiment
print(sentiment)  # Output: Sentiment(polarity=0.5, subjectivity=0.6)
```

---

## **Customization**

1. **Extend Functionality**:
   - Add more preprocessing steps (e.g., stemming, lemmatization) using external libraries like `camel-tools`.
   - Integrate additional NLP tasks like part-of-speech tagging or named entity recognition.

2. **Fine-Tune Sentiment Analysis**:
   - While `textblob_ar` provides a good baseline, you can fine-tune sentiment models on domain-specific datasets for improved accuracy.

3. **Support for Other Languages**:
   - `TextBlob` supports multiple languages. You can adapt this code for other languages by installing the appropriate extensions.

---

## **Model Details**
- **Underlying Model**: `textblob_ar` uses rule-based approaches and pre-trained models for Arabic text processing.
- **Sentiment Labels**:
  - Polarity ranges from `-1.0` (negative) to `1.0` (positive).
  - Subjectivity ranges from `0.0` (objective) to `1.0` (subjective).

---

## **Contributing**
Contributions are welcome! If you find any issues or have suggestions for improvement, feel free to open an issue or submit a pull request.

---

## **License**
This project is licensed under the MIT License. See the License file for details.

---

## **Contact**
For questions or collaboration opportunities, please reach out to me via:
- Email: wmzayed@gmail.com
- LinkedIn: (https://www.linkedin.com/in/Walid-Zayed)

---

Thank you for using this repository! I hope it helps you get started with Arabic text analysis. 😊  

--- 
