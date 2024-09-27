# YouTube Comments Analyzer

## Overview

This project is a **YouTube Comments Analyzer** web app built using **Flask**, **Natural Language Processing (NLP)**, and **Machine Learning**. The app is designed to automatically classify YouTube comments as either spam or legitimate, as well as perform sentiment analysis to determine if the comment expresses positive, negative, or neutral sentiment. This tool can be used to improve content moderation and provide insights into user engagement.

## Features

- **Spam Detection**: Uses machine learning algorithms to identify and filter out spam comments.
- **Sentiment Analysis**: Determines whether a comment is positive, negative, or neutral based on the language used.
- **Web Interface**: Interactive web app built with Flask for easy input and real-time analysis of YouTube comments.
- **Scalable**: The app is designed to handle large datasets of comments for comprehensive analysis.

## Installation

To run the app locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/KrishBhimani/YouTube-Comments-Analyzer.git
    cd YouTube-Comments-Analyzer
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv env
    env\Scripts\activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Download the Pre-trained Models**:
    - Download the pre-trained machine learning models (pickle files) from the link below and save them in the `models/` folder:
      - [Download Pickle Files]([your-download-link-here](https://drive.google.com/drive/folders/1Q4jxmyvuJ4bUNJbbK3j3MNX0V2eLQDGx?usp=sharing))

5. **Run the Flask app**:
    ```bash
    flask run --reload
    ```

6. **Access the web app**: Open your browser and navigate to `http://127.0.0.1:5000/` to use the web app.

## Usage

1. **Input YouTube Comments**: The web app allows you to paste or upload a dataset of YouTube comments.
2. **Spam Detection**: The app will automatically classify comments as spam or legitimate using a pre-trained machine learning model.
3. **Sentiment Analysis**: For each comment, the app provides a sentiment score, classifying the comment as positive, negative, or neutral.
4. **Results**: The processed comments will be displayed on the web app with labels for spam detection and sentiment.

## Models and Algorithms

- **Spam Detection**: Uses a machine learning classifier trained on labeled data to differentiate between spam and legitimate comments.
- **Sentiment Analysis**: Utilizes NLP techniques and sentiment scoring algorithms to determine the sentiment of each comment.
- **Flask Web Framework**: Enables the deployment of the web app for real-time analysis.

## Data

This project uses a dataset of YouTube comments containing features such as:
- Comment Text
- Likes/Reactions (Optional)
- Spam Label (for training the spam detection model)

## Future Improvements

- **Model Optimization**: Improve accuracy through hyperparameter tuning and training on larger datasets.
- **Comment Insights**: Provide additional insights such as comment engagement metrics or reply analysis.
- **Deployment**: Deploy the app to a cloud platform like AWS or Heroku for broader accessibility.

## Contributing

If you'd like to contribute to this project, follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any questions or suggestions, feel free to open an issue or reach out to me at [your.email@example.com](mailto:erkrishbhimani@gmail.com).

