import requests
from bs4 import BeautifulSoup
from collections import deque
from urllib.parse import urljoin

class WWDCSpider:
    def __init__(self):
        self.urls_to_visit = deque()
        self.visited_urls = set()
        self.video_graph = {} # {video_url: [related_video_urls]}

    def fetch_page(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None

    def parse_video_page(self, html_content, base_url):
        if not html_content:
            return []
        soup = BeautifulSoup(html_content, 'lxml')
        related_videos = []

        # Find the 'Related Videos' section
        related_videos_section = soup.find('h2', string='Related Videos')
        if related_videos_section:
            # Find the immediate sibling ul with class 'links small'
            related_ul = related_videos_section.find_next_sibling('ul', class_='links small')
            if related_ul:
                for link in related_ul.find_all('a', href=True):
                    href = link['href']
                    full_url = urljoin(base_url, href)
                    # Filter for WWDC video URLs and avoid duplicates
                    if "developer.apple.com/videos/play/wwdc" in full_url and full_url not in self.visited_urls:
                        related_videos.append(full_url)
        return related_videos

    def crawl(self, start_url):
        self.urls_to_visit.append(start_url)

        while self.urls_to_visit:
            current_url = self.urls_to_visit.popleft()
            if current_url in self.visited_urls:
                continue

            print(f"Crawling: {current_url}")
            html = self.fetch_page(current_url)
            self.visited_urls.add(current_url)

            if html:
                related_videos = self.parse_video_page(html, current_url)
                self.video_graph[current_url] = related_videos
                for video_url in related_videos:
                    if video_url not in self.visited_urls and video_url not in self.urls_to_visit:
                        self.urls_to_visit.append(video_url)

if __name__ == "__main__":
    # This is a placeholder URL. Replace with an actual WWDC 2025 video URL for testing.
    # You'll need to inspect a WWDC video page to find the correct selectors for related videos.
    start_url = "https://developer.apple.com/videos/play/wwdc2025/301/" # Example WWDC 2025 URL
    spider = WWDCSpider()
    spider.crawl(start_url)
    print("\n--- Crawling Complete ---")
    print("Video Graph:")
    for video, related in spider.video_graph.items():
        print(f"{video} -> {related}")
    print(f"Total visited URLs: {len(spider.visited_urls)}")