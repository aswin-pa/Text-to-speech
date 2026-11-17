import wave
import tempfile
from piper import PiperVoice

MODEL_PATH = "voices/en_US-lessac-medium.onnx"

# Load the model once at startup, not on every request
voice = PiperVoice.load(MODEL_PATH)

def text_to_wav(text: str) -> str:
    """Synthesize text and return the path to a temporary WAV file."""
    tmp = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
    tmp.close()
    with wave.open(tmp.name, "wb") as wav_file:
        if hasattr(voice, "synthesize_wav"):
            voice.synthesize_wav(text, wav_file)   # Piper 1.3+
        else:
            voice.synthesize(text, wav_file)       # older Piper
    return tmp.name