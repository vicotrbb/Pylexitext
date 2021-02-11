from __future__ import unicode_literals
import youtube_dl as yt


def from_video_to_text(video_url, source='youtube'):
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
        extracted_info = None
        with yt.YoutubeDL(ydl_opts) as ydl:
            extracted_info = ydl.extract_info(url=video_url, download=False)
            output_file_name = ydl.prepare_filename(extracted_info)
            ydl.download([video_url])

        return output_file_name, extracted_info

    else:
        return


def from_audio_to_text(audio, source='path'):
    pass


def from_podcast_to_text(url, source='spotfy'):
    pass
