from pytube import YouTube
url="https://youtu.be/RMXR3snavxc"
video=YouTube("https://youtu.be/RMXR3snavxc")
st=video.streams.get_highest_resolution()
st.download()