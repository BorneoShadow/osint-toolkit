# OSINT Investigation Toolkit

This toolkit allows cybersecurity enthusiasts and professionals to gather and analyze public data for investigations. The scripts use APIs and web scraping techniques to retrieve data from various sources, including Twitter, LinkedIn, and domain registries.

## Features:
- Retrieve basic information from social media profiles (Twitter, LinkedIn)
- Perform DNS lookups for domains
- Extract metadata from files (images, PDFs)
- Search for exposed email addresses and data breaches
- Geolocation based on IP addresses

## Usage:
1. Clone the repository:
git clone https://github.com/lucasbujang/osint-toolkit.git cd osint-toolkit

2. Install the required dependencies:
pip install -r requirements.txt


3. Run the scripts:
- **Twitter Scraper**: Retrieves user information and recent tweets from a public Twitter account.
  ```
  python twitter_scraper.py --username target_username
  ```

- **Domain Lookup**: Provides basic DNS information for a given domain.
  ```
  python domain_lookup.py --domain example.com
  ```

- **Metadata Extractor**: Extracts metadata from image files (e.g., geolocation, camera model).
  ```
  python metadata_extractor.py --file target_image.jpg
  ```
<details>
  <summary  align="center">
    <samp align="center">
      &#9776; Click Here to View More
    </samp></summary> 
  
## Community
Join the [The Intelligence Den](https://discord.gg/dYqyYMmeXa) and learn! It's an excellent space for learning about OSINT, sharing insights, and collaborating with like-minded individuals. Mai berandau enggau kami!

## License:
MIT License
