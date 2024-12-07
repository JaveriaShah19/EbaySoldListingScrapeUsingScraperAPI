**Project Description:** 

**Ebay Sold Listings Scraper with Flask, ScraperAPI, and Clay Integration**

This project involves building a web application using Flask, BeautifulSoup, ScraperAPI, and Clay to scrape and retrieve the total number of sold listings for a specific brand on eBay. The application exposes an API endpoint that allows users to request the number of sold listings for any brand available on eBay. The project integrates Clay for seamless automation and data flow, sending brand data from Clay, fetching the number of sold listings from eBay, and delivering the results back to Clay for further processing or reporting.

**Key Features:**
Scraping eBay Listings: The project scrapes the eBay search results page to extract the total number of sold listings for a given brand. This is done by parsing the page content using BeautifulSoup and locating the correct HTML element that contains the sold listings count.

**Clay Integration:** The system is designed to work with Clay, where data (such as brand names) is sent to the API, and the corresponding sold listings data is returned to Clay. This allows for seamless integration within Clay’s workflow and easy automation for tasks such as sending the scraped data to other systems or analyzing it.

**Retry Mechanism:** To handle transient errors or network failures, the scraper includes a retry mechanism. If an error occurs (such as a failed request), the system automatically retries the request up to 3 times, with a delay between each attempt.

**API Endpoint for Brand Query:** A RESTful API is created using Flask that accepts a POST request with the brand name and returns the number of sold listings for that brand from eBay. If the information is not available, it returns "N/A", ensuring smooth API usage without crashes.

**Integration with ScraperAPI:** The scraper uses ScraperAPI to bypass restrictions that eBay may place on bots. ScraperAPI handles the proxy rotation automatically, allowing for faster and more reliable scraping.

**Customizable Brand Search:** The application is designed to accept dynamic brand names and returns the total sold listings for any brand available on eBay. It also includes functionality for handling spaces in brand names and converting them into URL-friendly formats.

**Error Handling:** Comprehensive error handling ensures that the system gracefully handles issues such as network failures, incorrect HTML structure, or missing elements, providing meaningful error messages in case of failures.


**Technologies Used:**

Flask: For building the web API.

BeautifulSoup: For parsing and extracting HTML data from eBay.

Requests: For making HTTP requests to ScraperAPI and eBay.

ScraperAPI: For bypassing eBay’s restrictions and scraping data reliably using rotating proxies.

Clay: For automating data handling and ensuring seamless input/output integration.
