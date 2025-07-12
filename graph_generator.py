import re

class GraphGenerator:
    def __init__(self):
        pass

    def parse_mermaid_markdown(self, markdown_content):
        existing_graph = {}
        # Regex to find lines like "video_url --> related_video_url"
        # It captures the source and target URLs
        pattern = re.compile(r'"(https://developer.apple.com/videos/play/wwdc[0-9]{4}/[0-9]+/?)" --> "(https://developer.apple.com/videos/play/wwdc[0-9]{4}/[0-9]+/?)"')
        
        for line in markdown_content.splitlines():
            match = pattern.search(line)
            if match:
                source_url = match.group(1)
                target_url = match.group(2)
                if source_url not in existing_graph:
                    existing_graph[source_url] = []
                if target_url not in existing_graph[source_url]:
                    existing_graph[source_url].append(target_url)
        return existing_graph

    def generate_mermaid_markdown(self, new_video_graph, existing_graph=None):
        combined_graph = {} if existing_graph is None else existing_graph.copy()

        for video_url, related_videos in new_video_graph.items():
            if video_url not in combined_graph:
                combined_graph[video_url] = []
            for related_video_url in related_videos:
                if related_video_url not in combined_graph[video_url]:
                    combined_graph[video_url].append(related_video_url)

        mermaid_output = "graph TD\n"
        for video_url, related_videos in combined_graph.items():
            for related_video_url in related_videos:
                mermaid_output += f"    \"{video_url}\" --> \"{related_video_url}\"\n"
        return mermaid_output

if __name__ == "__main__":
    # Example usage:
    example_graph = {
        "https://developer.apple.com/videos/play/wwdc2025/286/": [
            "https://developer.apple.com/videos/play/wwdc2025/259/",
            "https://developer.apple.com/videos/play/wwdc2025/301/"
        ],
        "https://developer.apple.com/videos/play/wwdc2025/301/": [
            "https://developer.apple.com/videos/play/wwdc2025/360/"
        ]
    }
    generator = GraphGenerator()
    markdown = generator.generate_mermaid_markdown(example_graph)
    print(markdown)

    with open("wwdc_graph.md", "w") as f:
        f.write(markdown)
    print("Mermaid markdown written to wwdc_graph.md")

    # Test parsing existing markdown
    existing_markdown = """
graph TD
    "https://developer.apple.com/videos/play/wwdc2025/100/" --> "https://developer.apple.com/videos/play/wwdc2025/101/"
    "https://developer.apple.com/videos/play/wwdc2025/100/" --> "https://developer.apple.com/videos/play/wwdc2025/102/"
    "https://developer.apple.com/videos/play/wwdc2025/101/" --> "https://developer.apple.com/videos/play/wwdc2025/103/"
    """
    parsed_graph = generator.parse_mermaid_markdown(existing_markdown)
    print("\nParsed Existing Graph:", parsed_graph)

    # Test merging
    new_data = {
        "https://developer.apple.com/videos/play/wwdc2025/100/": [
            "https://developer.apple.com/videos/play/wwdc2025/104/"
        ],
        "https://developer.apple.com/videos/play/wwdc2025/105/": [
            "https://developer.apple.com/videos/play/wwdc2025/100/"
        ]
    }
    merged_markdown = generator.generate_mermaid_markdown(new_data, parsed_graph)
    print("\nMerged Markdown:", merged_markdown)
