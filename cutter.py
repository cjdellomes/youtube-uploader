import os
import subprocess

VIDEO_FOLDER = '/home/cjdellomes/youtube-uploader/videos'
INPUT_FILE = 'test-original.mp4'

def cut(input_file, output_file, start_time, end_time):
    subprocess.call(['ffmpeg', '-i', input_file, '-ss', start_time, '-to',
        end_time, '-c', 'copy', output_file])

def segment(file, segment_time_seconds):
    subprocess.call(['ffmpeg', '-i', file, '-map', '0', '-c', 'copy', '-f',
        'segment', '-segment_time', str(segment_time_seconds),
        '-reset_timestamps', '1', file+'_%03d.mp4'])

def main():
    input_file_path = os.path.join(VIDEO_FOLDER, INPUT_FILE)
    output_file_path = os.path.join(VIDEO_FOLDER, 'output.mp4')
    #cut(input_file_path, output_file_path, '00:00:00', '00:03:00')
    segment(input_file_path, 300)

if __name__ == "__main__":
    main()