import csv
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def remove_half_empty_cols(data_file):
    """
    Reads data from a file, removes columns empty in more than half of the cells,
    and returns the filtered DataFrame.

    Args:
        data_file (str): The path to the data file (CSV, Excel, etc. supported by pandas).

    Returns:
        pandas.DataFrame: The DataFrame with columns empty in more than half
                           of the cells removed.
    """
    # Read data from the file using pandas.read_csv or other relevant function
    df = pd.read_csv(data_file)

    # Calculate the proportion of missing values in each column
    missing_prop = df.isnull().mean()

    # Remove columns with missing values exceeding half the DataFrame
    filtered_df = df.loc[:, missing_prop <= 0.5]
    filtered_df = filtered_df.dropna()
    return filtered_df


def update_calc_position(df):

    for race_id in df['race_id'].unique():
        winner_row = df[(df['race_id'] == race_id) & (df['calc_position'] == 1)]  # Find winner row

        if not winner_row.empty:
            winner_indices = winner_row.index
            df.loc[df['race_id'] == race_id, 'calc_position'] = 0  # Set all positions to 0
            df.loc[winner_indices, 'calc_position'] = 1  # Set winner position to 1


def model(df):
    X = df.drop(columns=['calc_position'])  # Features
    y = df['calc_position']  # Labels

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Instantiate the Logistic Regression model
    model = LogisticRegression()

    # Train the model on the training data
    model.fit(X_train, y_train)

    # Make predictions on the testing data
    y_pred = model.predict(X_test)

    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy:", accuracy)


filtered_df = remove_half_empty_cols('horseRacing.csv')
update_calc_position(filtered_df)
new_csv_file = 'updated_horse_racing.csv'
filtered_df = filtered_df.drop(columns=['price'])

model(filtered_df)
filtered_df.to_csv(new_csv_file, index=False)

