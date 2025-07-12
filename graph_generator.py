class GraphGenerator:
    def __init__(self):
        pass

    def generate_mermaid_markdown(self, video_graph):
        mermaid_output = "graph TD\n"
        for video_url, related_videos in video_graph.items():
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