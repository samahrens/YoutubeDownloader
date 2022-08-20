from pytube import YouTube

link = input("Please enter the link of the video: ")
yT = YouTube(link)

print("Title of video: ", yT.title)
print("Total views: ", yT.views)

path = input("Please enter the absolute file path to download this video: ")

print("Downloading...")

yD = yT.streams.get_highest_resolution()
yD.download(path)

print("Video successfully downloaded!")
