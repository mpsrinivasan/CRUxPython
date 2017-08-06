from pytube import YouTube;
import Tkinter;

def YTD():
    url = theEntry1.get();
    yt = YouTube(url);
    destn = theEntry2.get();
    video = yt.get("mp4", "720p");
    print destn;
    video.download(destn);
    print ("done.");

#YTD();
root = Tkinter.Tk();
theLabel1 = Tkinter.Label(root, text = "Enter URL: ");
theEntry1 = Tkinter.Entry(root, width = "100");
theLabel2 = Tkinter.Label(root, text = "Enter Destination: ");
theEntry2 = Tkinter.Entry(root, width = "100");

theButton = Tkinter.Button(root, text = "Submit", command = YTD);
theLabel1.pack();
theEntry1.pack();
theLabel2.pack();
theEntry2.pack();
theButton.pack();
root.mainloop();
