from pytube import YouTube
url = input("Enter URL: ");
yt = YouTube(url);
print ("You want to Download: \n", yt.filename);
video = yt.get("mp4", "720p");
print ("File Downloaded in Desktop!!");
video.download("C:\\Users\\msp\\Desktop");
