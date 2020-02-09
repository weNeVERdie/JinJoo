from moviepy.editor import VideoFileClip, concatenate
import os

def assemble_cuts(inputfile, cuts, outputfile):
    """ Concatenate cuts and generate a video file. """
    '''
    input :::
    inputfile (str) : 작업할 비디오 파일 dir.
    cuts (list) : 클립할 영상의 시작점과 끝점을 넣는다. [[시작점1, 끝점1],[시작점2,끝점2],...]
    outputfile (str) : 저장할 파일명
    
    return ::: 편집된 영상파일이 저장된다.
    (None) 
    '''
    video = VideoFileClip(inputfile)
    final = concatenate([video.subclip(start, end)
                         for (start,end) in cuts])
    # 파일 저장 경로를 설정하고 싶으면 사용한다.
    # os.chdir('/home/pirl/PycharmProjects/NAVER_hack/save_video')
    final.to_videofile(outputfile)

###USAGE
# # 작업할 비디오 파일을 넣어준다.
# inputfile = "/home/pirl/PycharmProjects/NAVER_hack/Dog4727.mp4"
#
#
# # 시작점과 끝 점을 pair로 리스트 형식으로 넣어준다.
# # which can be expressed in seconds (15.35), in (min, sec), in (hour, min, sec), or as a string: '01:03:05.35'.
# cuts = [[1,3],[6,11]]
#
# assemble_cuts(inputfile, cuts, "dog_1.mp4")

