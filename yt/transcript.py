


from youtube_transcript_api import YouTubeTranscriptApi
import requests
from bs4 import BeautifulSoup
import re




def get_id(url):

    regex_id = r"^.*((youtu.be\/)|(v\/)|(\/u\/\w\/)|(embed\/)|(watch\?))\??v?=?([^#&?]*).*"
    try:
        if matches := re.match(regex_id, url):
            id = matches.group(7)
            
            if len(id) == 11:
                return id
            else:
                print("ID is incorrect")
        else: 
            print("You provided a wrong url")

    except Exception as e:
        print(e)



def main():
    
    video_url = "https://www.youtube.com/watch?v=QHXET1G9Y5U&t=1s"
    video_id = get_id(video_url)
    print(video_id)
    
    video_data = {
        "title": "",
        "author": "",
        "date": "",
        "views": "",
        "text": ""
    }
    
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    for line in transcript:
        video_data["text"] = line['text']
    
    return video_data
    
if __name__ == "__main__":
    main()



# find all videos connected to person

# loop over the video

    # scrape each one and save in cleaner format into db
    
    
# fetch data from db

# fine tune model with data