import pytest
import pandas as pd
from bs4 import BeautifulSoup
import os

# The main function that processes the HTML files and creates the CSV
def process_files():
    d = {'title': [], 'price': [], 'link': []}

    for file in os.listdir("data"):
        try:
            with open(f"data/{file}") as f:
                html_doc = f.read()
            soup = BeautifulSoup(html_doc, 'html.parser')
            t = soup.find("h2")
            title = t.get_text()
            p = soup.find("span", attrs={"class": 'a-price-whole'})
            price = p.get_text()
            l = soup.find("a")
            link = "https://amazon.in/" + l['href']
            d['title'].append(title)
            d['price'].append(price)
            d['link'].append(link)
        except Exception as e:
            print(e)

    df = pd.DataFrame(data=d)
    df.to_csv("data.csv", index=False)
    return df

# Test case 1: Check if the 'data' directory exists
def test_data_directory_exists():
    assert os.path.exists("data"), "The 'data' directory does not exist."

# Test case 2: Check if there are files in the 'data' directory
def test_files_in_data_directory():
    files = os.listdir("data")
    assert len(files) > 0, "No files found in the 'data' directory."

# Test case 3: Verify that the HTML files can be parsed without errors
def test_html_parsing():
    for file in os.listdir("data"):
        try:
            with open(f"data/{file}") as f:
                html_doc = f.read()
            soup = BeautifulSoup(html_doc, 'html.parser')
            assert soup is not None, f"Failed to parse HTML in file: {file}"
        except Exception as e:
            pytest.fail(f"Exception occurred while parsing HTML: {e}")

# Test case 4: Ensure that the CSV file is created after processing
def test_csv_file_creation():
    df = process_files()
    assert os.path.exists("data.csv"), "Data CSV file was not created."
    assert not df.empty, "Data CSV file is empty."

# Test case 5: Verify the content of the CSV file
def test_csv_content():
    df = pd.read_csv("data.csv")
    assert not df.empty, "Data CSV file is empty."
    assert "title" in df.columns, "'title' column is missing in the CSV file."
    assert "price" in df.columns, "'price' column is missing in the CSV file."
    assert "link" in df.columns, "'link' column is missing in the CSV file."
