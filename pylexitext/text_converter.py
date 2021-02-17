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
                text = r.recognize_google(audio_listened)
            except sr.UnknownValueError as e:
                print("Error:", str(e))
            else:
                text = f"{text.capitalize()}. "
                print(chunk_filename, ":", text)
                converted_text += text

    shutil.rmtree(folder_name, ignore_errors=True)
    return text.Text(converted_text)


def from_video_to_text(video_path, source='youtube') -> text.Text:
    """
    Converts the audio of a video to text
    """

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

        return convert_sound_to_text(output_file_name)

    elif source == 'file':
        return


def from_podcast_to_text(url, source='spotfy') -> text.Text:
    pass


def text_to_sound(text):
    pass
