Web Scraper Project
A Python-based web scraping tool to extract product data (title and price) from e-commerce sites.
This project uses requests and BeautifulSoup libraries to scrape data and exports it into a CSV file.

Features
Scrapes product titles and prices from a specified URL

Supports scraping from different URLs by passing the URL as an argument

Saves the scraped data into a CSV file (output.csv)

Easy to modify for other websites with similar HTML structure

Requirements
Python 3.x

requests

beautifulsoup4

Install dependencies with:

bash
Copy
Edit
pip install -r requirements.txt
Usage
Clone or download the repository.

Open scraper.py and modify the URL in the main function or pass the URL dynamically.

Run the scraper:

bash
Copy
Edit
python scraper.py
The scraped data will be saved to output.csv.

How It Works
Sends an HTTP GET request to the given URL with appropriate headers.

Parses the HTML content with BeautifulSoup.

Finds product containers using CSS selectors.

Extracts product title and price.

Writes data to CSV.

Sample Output
bash
Copy
Edit
Title,Price
Laptop 1,$999
Laptop 2,$799
...
Contributing
Feel free to fork and modify the scraper to suit your needs! Open an issue or pull request for improvements.

License
This project is open source and available under the MIT License.
