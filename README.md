# House-Price-Prediction

Predict house prices in Bangalore based on various features such as location, size, and number of bathrooms. This is a supervised machine learning regression task. This project leverages real estate data to provide accurate price predictions for potential buyers and sellers.


## Files

- `app.py`: The main Flask application file that serves the web interface for predicting house prices.
- `Cleaned_House_Data.csv`: The cleaned dataset used for training the model.
- `House Data.csv`: The raw dataset containing house prices and features.
- `house_price_prediction_model.pkl`: The trained machine learning model serialized using pickle.
- `House_price_regression.ipynb`: Jupyter notebook containing the data analysis, preprocessing, and model training steps.
- `README.md`: This file.
- `static/style.css`: CSS file for styling the web interface.
- `templates/index.html`: HTML template for the web interface.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Sakib0/House-Price-Prediction.git
    cd House-Price-Prediction
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Run the Flask application:
    ```sh
    python app.py
    ```

4. Open your web browser and go to `http://127.0.0.1:5000` to access the application.

## Usage

1. Open the web application.
2. Enter the required features such as location, size, and number of bathrooms.
3. Click on the "Predict" button to get the estimated house price.

## Model Training

To train the model, follow the steps in the `House_price_regression.ipynb` notebook. This includes data cleaning, feature engineering, model training, and evaluation.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
