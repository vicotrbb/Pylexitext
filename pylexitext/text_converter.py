from __future__ import unicode_literals
import youtube_dl as yt
import speech_recognition as sr
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence
import shutil

from . import text


def convert_sound_to_text(sound_file) -> text.Text:
    """
        Converts an audio to text
    """

    r = sr.Recognizer()
    folder_name = "audio-chunks"
    sound = AudioSegment.from_mp3(sound_file)

    chunks = split_on_silence(
        sound,
        min_silence_len=500,
        silence_thresh=sound.dBFS-14,
        keep_silence=500,
    )

    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    converted_text = ""

    for i, audio_chunk in enumerate(chunks, start=1):
        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")
        with sr.AudioFile(chunk_filename) as source:
            audio_listened = r.record(source)
            try:
                text_chunks = r.recognize_google(audio_listened)
            except sr.UnknownValueError as e:
                print("Error:", str(e))
            else:
                text_chunks = f"{text_chunks.capitalize()}. "
                print(chunk_filename, ":", text_chunks)
                converted_text += text_chunks

    shutil.rmtree(folder_name, ignore_errors=True)
    os.remove(sound_file)
    return text.Text(converted_text)


def from_video_to_text(video_path, source='youtube') -> text.Text:
    """
    Converts the audio of a video to text
    """

    try:
        if source == 'youtube':
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }]
            }

            output_file_name = None
            with yt.YoutubeDL(ydl_opts) as ydl:
                extracted_info = ydl.extract_info(url=video_path, download=False)
                output_file_name = ydl.prepare_filename(extracted_info)
                ydl.download([video_path])

            output_file_name = output_file_name.split('.', 1)[0] + ".mp3"

            return convert_sound_to_text(output_file_name)

        elif source == 'file':
            return
    except:
        print('This functionality needs a ffmpeg decoder, please install it.')
        print('Ubuntu/debian -> sudo apt-get install ffmpeg')
        print('MacOS -> brew install ffmpeg')
        print('Windows using chocolatey -> choco install ffmpeg')


def from_podcast_to_text(url, source='spotify') -> text.Text:
    pass


def text_to_sound(text):
    pass


def sound_to_text(text):
    pass
