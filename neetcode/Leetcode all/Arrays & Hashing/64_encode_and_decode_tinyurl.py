class Codec:
    def __init__(self):
        self.url_map = {}
        self.id = 0

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.url_map[self.id] = longUrl
        shorturl = f"http:tinyurl.com/{self.id}"
        self.id += 1
        return shorturl

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        url = int(shortUrl.split('/')[-1])
        return self.url_map[url]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))