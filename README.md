# SpokenLanguageDetection
Deep Learning Project - Spoken Language Detection (English, French, and German)

Name - Bhaskar Sharma

The deep learning project will be able to identify languages (between English, German, and French) based on speech.

It may be extended later to include more languages.

Dataset used: https://www.kaggle.com/datasets/toponowicz/spoken-language-identification

How to run the code:-

To run the code, we need to install several Python libraries:

Pandas: For data manipulation and analysis.
NumPy: For numerical computing.
Matplotlib: For creating visualizations.
Scipy: we are using wavfile from scipy.io to read WAV files.
python_speech_features: For extracting features from speech signals.
Librosa: Another library for audio and music analysis.
Keras: For building and training neural networks. We are using Keras layers and models.
Scikit-learn: For machine learning tasks. We are using compute_class_weight from sklearn.utils.class_weight.
TQDM: For adding progress bars to loops.

We can install the libraries by running:
pip install pandas numpy matplotlib scipy python_speech_features librosa keras scikit-learn tqdm

As in the current condition, the small_dataset folder can be used to create a small dataset to train the model on.

The bigger dataset (complete dataset) can be in the following order:
(Optional) Reducing the size of the dataset by using the ReduceDataset script.
Executing FlacToWav script to convert the Flac files to wav files, so they are easier to process.
Then using the CreateCSV script to create the csv for the new wav folder.

The data.csv file corresponds to the small_dataset folder.
