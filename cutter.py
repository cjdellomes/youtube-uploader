import os
import subprocess
import glob

VIDEO_FOLDER = os.path.join(os.path.dirname(__file__), '/videos')
INPUT_FILE = 'test-original.mp4'

def cut(input_file_path, output_file_path, start_time, end_time):
    subprocess.call(['ffmpeg', '-i', input_file_path, '-ss', start_time, '-to',
        end_time, '-c', 'copy', output_file_path])
    return output_file_path

def segment(file_path, segment_time_seconds):
    dir_name = os.path.dirname(file_path)
    file_name_no_ext = os.path.splitext(file_path)[0]
    segment_path = os.path.join(dir_name, file_name_no_ext)

    subprocess.call(['ffmpeg', '-i', file_path, '-map', '0', '-c', 'copy', '-f',
        'segment', '-segment_time', str(segment_time_seconds),
        '-reset_timestamps', '1', segment_path+'_%03d.mp4'])
    return get_segment_output_files(segment_path)

def get_segment_output_files(segment_path):
    return glob.glob(segment_path + '_*')

def main():
    input_file_path = os.path.join(VIDEO_FOLDER, INPUT_FILE)
    output_file_path = os.path.join(VIDEO_FOLDER, 'output.mp4')
    #cut(input_file_path, output_file_path, '00:00:00', '00:03:00')
    segments = segment(input_file_path, 300)
    print(segments)

if __name__ == "__main__":
    main()