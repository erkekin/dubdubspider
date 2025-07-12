import argparse
from spider import WWDCSpider
from graph_generator import GraphGenerator

def main():
    parser = argparse.ArgumentParser(description="Spider WWDC video pages and generate a Mermaid graph.")
    parser.add_argument("start_url", help="The initial WWDC video URL to start crawling from.")
    args = parser.parse_args()

    print(f"Starting WWDC Spider from: {args.start_url}")
    spider = WWDCSpider()
    spider.crawl(args.start_url)

    print("\n--- Crawling Complete ---")
    print(f"Total visited URLs: {len(spider.visited_urls)}")

    print("Generating Mermaid graph...")
    generator = GraphGenerator()
    mermaid_markdown = generator.generate_mermaid_markdown(spider.video_graph)

    output_file = "wwdc_graph.md"
    with open(output_file, "w") as f:
        f.write(mermaid_markdown)
    print(f"Mermaid graph successfully generated and saved to {output_file}")

if __name__ == "__main__":
    main()
