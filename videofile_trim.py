from moviepy.editor import VideoFileClip, concatenate


def assemble_cuts(cuts, outputfile):
    """ Concatenate cuts and generate a video file. """
    final = concatenate([video.subclip(start, end)
                         for (start,end) in cuts])
    final.to_videofile(outputfile)


#작업할 비디오 파일을 넣어준다.
# video = VideoFileClip("dogo.mp4")

# 시작점과 끝 점을 pair로 리스트 형식으로 넣어준다.
#which can be expressed in seconds (15.35), in (min, sec), in (hour, min, sec), or as a string: '01:03:05.35'.
# cuts = [[5,10.5],[20,25],[30,35]]

# assemble_cuts(cuts, "doggy.mp4")
