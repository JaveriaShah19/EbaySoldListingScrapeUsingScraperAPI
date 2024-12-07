from flask import Flask, jsonify, request
import requests
from bs4 import BeautifulSoup  # We'll use BeautifulSoup for parsing HTML
import re  # Importing the re module
import time

app = Flask(__name__)

# ScraperAPI key
SCRAPER_API_KEY = '4868cf221503d67d470e5c948546725e'

def extract_brand_from_website(website):
    from urllib.parse import urlparse
    domain = urlparse(website).netloc
    brand_name = re.sub(r'^(www\d?\.)|(\.com|\.net|\.org)$', '', domain)
    return brand_name.capitalize()

def scrape_ebay_sold_listings(brand_name):
    
    max_retries = 3  # Number of retries
    retry_delay = 10  # Delay in seconds between retries

    for attempt in range(max_retries):
        try:
            # Delay before the first request and subsequent retries
            if attempt > 0:
                print(f"Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)

            # Construct the search URL
            search_url = f"https://www.ebay.com/sch/i.html?_from=R40&_nkw={brand_name.replace(' ', '+')}&LH_Sold=1&rt=nc"

            # Request through ScraperAPI
            response = requests.get(f"http://api.scraperapi.com/?api_key={SCRAPER_API_KEY}&url={search_url}")
            
            # Check for successful response
            if response.status_code != 200:
                raise Exception(f"Failed to fetch data: HTTP {response.status_code}")

            # Parse the page content
            soup = BeautifulSoup(response.text, 'html.parser')

            sold_listings_heading = soup.find('h1', class_='srp-controls__count-heading')

            # Validate that the heading contains sold listings (not the brand name)
            if sold_listings_heading:
                # Extract the first span which contains the number of sold listings
                sold_listings_span = sold_listings_heading.find('span', class_='BOLD')
                if sold_listings_span:
                    total_sold_value = sold_listings_span.get_text().replace(",", "")
                    return total_sold_value

            # Return "N/A" if the required elements are not found
            return "N/A"

        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")

            # If the maximum attempts are reached, log and return an error
            if attempt == max_retries - 1:
                return "Error: Unable to fetch data after multiple retries"

@app.route('/get-sold-listings', methods=['POST'])
def get_sold_listings():
    data = request.json
    brand_name = data.get('brand_name')

    if not brand_name:
        return jsonify({"error": "Brand name is required"}), 400

    listings_count = scrape_ebay_sold_listings(brand_name)
    return jsonify({"brand_name": brand_name, "sold_listings": listings_count})

if __name__ == '__main__':
    app.run(debug=True)
