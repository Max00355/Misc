import re
import urllib
import os

class YoutubeDownloader:
    def __init__(self):
        self.youtubeSearchUrl = "https://www.youtube.com/results?search_query="
        self.youtubeDownloader = "http://en.savefrom.net/1-how-to-download-youtube-video/"

    def main(self):
        name = raw_input("Name of Song: ")
        self.downloadVideo(self.searchVideo(name))

    def downloadByName(self, name):
        self.downloadVideo(self.searchVideo(name))
        print "{} has been downloaded".format(name)

    def searchVideo(self, name):
        html = urllib.urlopen(self.youtubeSearchUrl + name.replace(" ", '+')).read()
        links = re.findall("href=\"\/watch\?v\=[a-zA-Z0-9]*\"", html)
        toDownload = links[0].split('"')[1]
        return "https://youtube.com/"+toDownload

    def downloadVideo(self, url):
        os.system("youtube-dl --extract-audio --audio-format mp3 \"{}\"".format(url))

if __name__ == "__main__":
    YoutubeDownloader().main()
