import os
import glob
import multiprocessing
import subprocess

def convert_flac_to_wav(flac_file, output_dir):
    wav_file = os.path.join(output_dir, os.path.splitext(os.path.basename(flac_file))[0] + '.wav')
    subprocess.run(['ffmpeg', '-i', flac_file, wav_file], capture_output=True)


def convert_all_flac_to_wav(input_dir, output_dir):
    flac_files = glob.glob(os.path.join(input_dir, '*.flac'))
    pool = multiprocessing.Pool()
    pool.starmap(convert_flac_to_wav, [(flac_file, output_dir) for flac_file in flac_files])
    pool.close()
    pool.join()

if __name__ == '__main__':
    
    input_dir = './dataset/test/test'
    output_dir = './dataset/test/wav_test'
    os.makedirs(output_dir, exist_ok=True)
    convert_all_flac_to_wav(input_dir, output_dir)