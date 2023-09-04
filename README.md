# Breast Cancer Predictor

Welcome to the Breast Cancer Predictor, a powerful tool designed to help diagnose breast cancer based on measurements from your cytology lab. 

This machine learning app is here to assist in distinguishing between benign and malignant breast masses, offering invaluable support to healthcare professionals and researchers.

## Installation

1. Clone this repository to your local machine:

```bash
git clone https://github.com/kedinaimoke/BreastCancerPredictor.git

cd BreastCancerPredictor
```
2. Install the required Python packages:

```python
pip install -r requirements.txt
```

## Usage

1. Launch the application:

```python
streamlit run st_cancerpred.py
```

2. Use the sliders in the leftbar to adjust the measurements according to your tissue sample's characteristics.

## Understanding The Output

The application provides you with insights into the diagnosis process:

Column 1: You'll find a radar chart visually representing your input data and comparing it with the characteristics of benign (Product A) and malignant (Product B) masses.

Column 2: This section is available for additional information or user interactions.

## Contributing

Pull requests are welcome. If you're considering significant changes, feel free to begin a discussion by opening an issue first.

When contributing, please ensure that you update any relevant tests as needed. Your efforts are greatly appreciated!
