# WWDC Video Graph Spider

This Python application spiders WWDC video pages to discover related videos and generates a Mermaid markdown file representing the video dependency graph. This helps visualize the connections between different WWDC sessions.

## Features

-   **Web Scraping:** Crawls WWDC video pages to extract links to related videos.
-   **Graph Generation:** Creates a Mermaid-compatible markdown file (`wwdc_graph.md`) visualizing the relationships between videos.
-   **Incremental Updates:** Appends new video relationships to an existing graph, avoiding duplicates.
-   **Configurable Starting Points:** Reads initial video URLs from a file (`initial_links.md`) for flexible crawling.

## Installation

To set up the project, follow these steps:

1.  **Clone the repository:**

    ```bash
    git clone <your-repository-url>
    cd dubdubspider
    ```

2.  **Create a Python Virtual Environment:**

    ```bash
    python3 -m venv venv
    ```

3.  **Activate the Virtual Environment:**

    -   **macOS/Linux:**

        ```bash
        source venv/bin/activate
        ```

    -   **Windows:**

        ```bash
        .\venv\Scripts\activate
        ```

4.  **Install Dependencies:**

    ```bash
    pip install requests beautifulsoup4 lxml
    ```

## Usage

1.  **Prepare `initial_links.md`:**

    Create a file named `initial_links.md` in the root directory of the project. List the starting WWDC video URLs, one URL per line. For example:

    ```
    https://developer.apple.com/videos/play/wwdc2025/301/
    https://developer.apple.com/videos/play/wwdc2024/1000/
    https://developer.apple.com/videos/play/wwdc2023/10105/
    ```

2.  **Run the Application:**

    Make sure your virtual environment is activated (as shown in the Installation section), then run:

    ```bash
    python3 main.py
    ```

    The application will start crawling from the URLs specified in `initial_links.md`. Progress will be printed to the console.

3.  **View the Graph:**

    After the crawling is complete, a file named `wwdc_graph.md` will be generated or updated in the project root. This file contains the Mermaid markdown syntax for the video dependency graph.

    You can view this graph using any Markdown viewer that supports Mermaid, such as:
    -   GitHub (it renders Mermaid diagrams directly in markdown files).
    -   VS Code with a Mermaid extension.
    -   Online Mermaid live editors.

## Example Mermaid Output

```mermaid
graph TD
    "https://developer.apple.com/videos/play/wwdc2025/286/" --> "https://developer.apple.com/videos/play/wwdc2025/259"
    "https://developer.apple.com/videos/play/wwdc2025/286/" --> "https://developer.apple.com/videos/play/wwdc2025/301"
    "https://developer.apple.com/videos/play/wwdc2025/301" --> "https://developer.apple.com/videos/play/wwdc2025/360"
```

## Contributing

Contributions are welcome! If you find a bug or have an idea for an enhancement, please open an issue or submit a pull request.
