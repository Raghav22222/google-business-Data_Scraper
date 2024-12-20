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
