# 🕸️ Web Scraper Project

A lightweight, Python-based web scraping tool that extracts product data (title and price) from e-commerce websites.  
It uses `requests` and `BeautifulSoup` to scrape data and exports the results to a CSV file.

---

## ✨ Features

- 🔗 Scrapes product titles and prices from any specified URL  
- 🌐 Accepts dynamic URLs via user input or code change  
- 📄 Saves scraped data into a structured CSV file (`output.csv`)  
- 🔧 Easy to adapt to other websites with a similar HTML layout  

---

## 📦 Requirements

- Python 3.x  
- requests
- beautifulsoup4

Install all dependencies by running:
  pip install -r requirements.txt


## 🚀 Usage
Clone or download this repository
Modify the URL directly in scraper.py or pass the URL dynamically
Run the scraper:
  python scraper.py
The scraped data will be saved in "output.csv" in the same folder


## ⚙️ How It Works
  Sends an HTTP GET request to the provided URL with appropriate headers
  Parses the HTML content using BeautifulSoup
  Identifies product containers using CSS selectors
  Extracts product titles and prices
  Writes the collected data into a CSV file


## 📊 Sample Output
  output.csv:
   Title,Price
   Laptop 1,$999
   Laptop 2,$799
   Laptop 3,$599

## 🤝 Contributing
Feel free to fork this repo, improve the scraper logic, and open a pull request.
Issues and suggestions are always welcome!

## 🪪 License
This project is licensed under the MIT License – feel free to use, modify, and distribute it.

✨ Author
Developed by Aditya Dwivedi
