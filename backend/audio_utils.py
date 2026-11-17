from pydub import AudioSegment
import tempfile

# If FFmpeg is not on PATH on Windows, uncomment and set the path:
# AudioSegment.converter = r"C:\path\to\ffmpeg.exe"

def wav_to_mp3(wav_path: str) -> str:
    """Convert a WAV file to MP3 and return the MP3 path."""
    audio = AudioSegment.from_wav(wav_path)
    audio = audio.normalize()
    tmp = tempfile.NamedTemporaryFile(suffix=".mp3", delete=False)
    tmp.close()
    audio.export(tmp.name, format="mp3", bitrate="128k")
    return tmp.name
