import requests
from bs4 import BeautifulSoup

# Get the URL of the YouTube video.
video_url = "https://www.youtube.com/watch?v=ZKNQ6gsW45M"

# Make a request to the YouTube video page.
response = requests.get(video_url)

# Parse the HTML of the video page using Beautiful Soup.
soup = BeautifulSoup(response.content, "html.parser")

# Find the element that contains the subtitles.
subtitles = soup.find("div", class_="ytd-video-transcript")

# Extract the subtitles from the element.
subtitles_text = subtitles.text

# Save the subtitles to a file.
with open("subtitles.txt", "w") as f:
    f.write(subtitles_text)
