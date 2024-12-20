# Google Business Scraper

This tool allows you to scrape business-related data from Google Places using the Google Places API. It collects details such as business name, location, rating, contact information, and industry. The data is then cleaned and saved as a CSV file for further analysis.

## Requirements

Before running the scraper, ensure you have the following libraries installed:

- `requests`
- `pandas`

You can install them using `pip`:

```bash
pip install requests pandas
```

## How to Run and Test the Scraper

### Prerequisites

Before running the scraper, ensure you have the following:
1. **Python 3.x**: The scraper is written in Python, so make sure you have Python 3 installed on your system.
2. **Google Places API Key**: You'll need a Google Places API key to authenticate your requests. You can get it from the [Google Cloud Console](https://console.cloud.google.com/).

### Setup

1. **Clone the repository**: To get started, clone this repository to your local machine:

    ```bash
    git clone https://github.com/username/google-business-scraper.git
    ```

2. **Navigate to the project folder**:

    ```bash
    cd google-business-scraper
    ```

3. **API Key Configuration**:
    - Open the script `google_business_scraper.ipynb` (or `google_business_scraper.py` if running as a script).
    - Replace the `api_key` variable with your own API key.

### Running the Scraper

#### Option 1: Jupyter Notebook

1. Open the `google_business_scraper.ipynb` in your preferred Jupyter environment (e.g., Jupyter Notebook or JupyterLab).
2. Run all the cells to execute the code and start the scraping process.

#### Option 2: Python Script

1. Open a terminal in the project folder.
2. Run the script using Python:

    ```bash
    python google_business_scraper.py
    ```

### Testing the Scraper

1. **Test with different queries**: You can modify the query in the script to search for different types of businesses or locations. For example, change `"restaurants in Mumbai"` to `"hospitals in Delhi"` or `"coffee shops in New York"`.
   
2. **Rate Limiting**: The scraper includes a delay (`time.sleep(2)`) to ensure compliance with Google API's rate limits. If you need to scrape more data, consider implementing more sophisticated rate-limiting or pagination techniques.

### Data Output

- The scraper will generate a CSV file named `google_business_results.csv` containing the following fields:
    - **Name**: The name of the business.
    - **Address**: The business address.
    - **Rating**: The business's rating.
    - **Phone Number**: The business's contact number.
    - **Website**: The business's website URL.
    - **Industry**: The type or industry the business belongs to.

- The CSV file will be saved to your specified path (or the default location if not modified).

### Sample Dataset

The generated dataset will look like this (with anonymized or generic information):

```csv
Name,Address,Rating,Phone Number,Website,Industry
Restaurant A,"123 Street, Mumbai",4.5,"N/A","www.restaurantA.com","Food & Beverage"
Restaurant B,"456 Street, Mumbai",4.2,"N/A","www.restaurantB.com","Food & Beverage"
```

## Code Explanation

### 1. Import Libraries

The code begins by importing the necessary libraries:

- **`requests`**: To handle HTTP requests to Google API endpoints.
- **`pandas`**: For data manipulation, cleaning, and saving the scraped data into a CSV file.
- **`time`**: For adding a delay between API calls to avoid hitting Google Places API rate limits.

### 2. API Key Configuration

The `api_key` variable is where you need to insert your own Google API key, which is required for authentication to access the Google Places API. Ensure that you've enabled the "Places API" in your Google Cloud Console account.

### 3. Function: `get_places_data`

This function takes two parameters:
- `query`: A string representing the search query (e.g., "restaurants in Mumbai").
- `num_results`: The number of results you want to scrape (default is 40).

#### a. Sending Requests to the Google Places API

The function first constructs a request URL using the `base_url` and the query parameter. It sends a GET request to the Google Places API using the `requests.get()` method.

#### b. Processing the Results

The API response contains a list of results. For each result, the function extracts the following details:
- **Name**: The name of the business.
- **Address**: The business location address.
- **Rating**: The business's rating, if available.

#### c. Fetching Additional Details

For each business, the function sends another request to the Google Places Details API to fetch additional details, including:
- **Phone Number**: The contact number of the business.
- **Website**: The business's website URL.
- **Industry**: The type of business (e.g., restaurant, cafe, etc.), derived from the `types` field returned by the API.

#### d. Pagination Handling

The Google Places API provides a pagination mechanism, where the first set of results may not include all available businesses. If there are more pages of results, the `next_page_token` is used to send a subsequent request to fetch the next set of results. The function keeps fetching pages until the required number of results is obtained.

#### e. Data Aggregation and Return

All the fetched data is stored in a list of dictionaries, which is then converted into a Pandas DataFrame. The function returns this DataFrame.

### 4. Data Cleaning

Once the data is scraped, basic data cleaning steps are performed:
- **Removing Duplicates**: Duplicates are removed based on the business name and address to ensure unique entries.
- **Filling Missing Values**: Any missing values are filled with the string `"N/A"` to ensure consistency and avoid errors during data analysis.

### 5. Saving Data to CSV

Finally, the cleaned data is saved to a CSV file (e.g., `google_business_results.csv`) on your desktop (or a different location if the path is modified).

### Data Cleaning

The scraper includes basic data cleaning, which:
- **Removes duplicates**: Duplicates are removed based on the business name and address to ensure unique entries.
- **Fills missing values**: Any missing values are filled with `"N/A"` to ensure consistency and avoid errors during data analysis.

Feel free to modify the data processing steps based on your specific needs.

### Repository Files

- **Data Scraper.ipynb**: The Jupyter Notebook containing the scraping code.
- **Data_scraper.py**: A standalone Python script for running the scraper.
- **google_business_results.csv**: A sample dataset generated by the scraper.
- **README.md**: This file, providing documentation on how to run and test the scraper.
