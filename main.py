import os
from spider import WWDCSpider
from graph_generator import GraphGenerator

def main():
    print("Starting WWDC Spider...")
    spider = WWDCSpider()
    generator = GraphGenerator()

    output_file = "wwdc_graph.md"
    existing_graph = None

    # Read existing graph if it exists
    if os.path.exists(output_file):
        with open(output_file, "r") as f:
            existing_graph_content = f.read()
        existing_graph = generator.parse_mermaid_markdown(existing_graph_content)

    # Read initial links from file
    initial_links_file = "initial_links.md"
    if not os.path.exists(initial_links_file):
        print(f"Error: {initial_links_file} not found. Please create it with a list of URLs.")
        return

    with open(initial_links_file, "r") as f:
        initial_urls = [url.strip() for url in f.readlines() if url.strip()]

    if not initial_urls:
        print(f"No URLs found in {initial_links_file}. Exiting.")
        return

    for start_url in initial_urls:
        print(f"Crawling from initial link: {start_url}")
        spider.crawl(start_url)

    print("\n--- Crawling Complete ---")
    print(f"Total visited URLs: {len(spider.visited_urls)}")

    print("Generating Mermaid graph...")
    mermaid_markdown = generator.generate_mermaid_markdown(spider.video_graph, existing_graph)

    with open(output_file, "w") as f:
        f.write(mermaid_markdown)
    print(f"Mermaid graph successfully generated and saved to {output_file}")

if __name__ == "__main__":
    main()
