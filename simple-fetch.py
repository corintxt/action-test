import io
import os
import requests
import pandas as pd

def fetch_test(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.text
    return data

def read_csv(datastring):
    csv = io.StringIO(datastring)
    df = pd.read_csv(csv)
    return df

if __name__ == "__main__":
    test_url = 'https://raw.githubusercontent.com/corintxt/papiris/main/testout.csv'

    data = fetch_test(test_url)
    df = read_csv(data)

    print(len(df))

    # save the data in the data directory
    directory = os.path.join(os.getcwd(), "data")
    if not os.path.exists(directory):
        os.makedirs(directory)

    data_file = os.path.join(directory, "test_data.csv")

    df.to_csv(data_file)