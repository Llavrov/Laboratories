import ffmpeg


def video_to_giv():
    stream = ffmpeg.input('video.mp4')
    stream = ffmpeg.filter(stream, "file")
    stream = ffmpeg.output(stream, 'output.gif')
    ffmpeg.run(stream)


video_to_giv()

# def main():
#     video_to_giv()

# if __name__ == '__main__':
#     main()