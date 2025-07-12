# WWDC Video Graph Spider Plan

This document outlines the plan for creating a Python application that spiders WWDC video pages, discovers related videos, and generates a Mermaid markdown file representing the video dependency graph.

## 1. Project Setup

- **Python Virtual Environment:** A virtual environment will be set up within the project directory to manage dependencies in isolation.
- **Install Dependencies:** The following Python libraries will be installed using `pip`:
    - `requests`: For making HTTP requests to fetch web page content.
    - `beautifulsoup4`: For parsing HTML and extracting information.
    - `lxml`: High-performance XML and HTML parser to be used with BeautifulSoup.

## 2. Web Spider Implementation (`spider.py`)

- **Core Logic:** A `spider.py` file will contain the main web scraping logic.
- **Starting Point:** The spider will begin with a single WWDC 2025 video URL.
- **URL Management:**
    - `urls_to_visit`: A queue or list to hold the URLs of video pages to be scraped.
    - `visited_urls`: A set to store the URLs of pages that have already been scraped to prevent redundant processing and infinite loops.
- **Scraping Process:** For each video URL, the spider will:
    1. Fetch the HTML content of the page using `requests`.
    2. Parse the HTML using `BeautifulSoup` to extract:
        - The URLs of all "related" or "recommended" videos on the page.
    3. **Data Storage:** The relationship between the current video and its related videos will be stored. A dictionary where keys are video urls and values are lists of related video urls is a good approach.
    4. **Queue Management:** New, unvisited related video URLs will be added to the `urls_to_visit` queue.
    5. visit all the queue and append to the markdown. Do not let duplicates.

## 3. Graph Generation (`graph_generator.py`)

- **Purpose:** A separate `graph_generator.py` script will be responsible for creating the Mermaid graph.
- **Input:** This script will take the data structure (the dictionary of video relationships) created by the spider as input.
- **Output:** It will generate a markdown file named `wwdc_graph.md`.
- **Mermaid Syntax:** The script will iterate through the video relationships and format them into Mermaid's flowchart syntax. For example:

  ```mermaid
  graph TD
      "https://developer.apple.com/videos/play/wwdc2025/286/" --> "https://developer.apple.com/videos/play/wwdc2025/259"
      "https://developer.apple.com/videos/play/wwdc2025/286/" --> "https://developer.apple.com/videos/play/wwdc2025/301"
      "https://developer.apple.com/videos/play/wwdc2025/301" --> "https://developer.apple.com/videos/play/wwdc2025/360"
      .
      .
      .
  ```

## 4. Main Application (`main.py`)

- **Orchestration:** A `main.py` script will serve as the entry point and coordinate the overall process.
- **Execution Flow:**
    1. It will accept the initial WWDC 2025 video URL as a command-line argument or from a configuration file.
    2. It will instantiate and run the spider to gather the video relationship data.
    3. It will then pass the collected data to the graph generator to produce the final `wwdc_graph.md` file.
    4. It will then jump to the first related video link and repeat the process. 
    5. A success message will be printed to the console upon completion.

This plan provides a structured approach to developing the WWDC video graph spider, separating concerns into distinct modules for clarity and maintainability.
