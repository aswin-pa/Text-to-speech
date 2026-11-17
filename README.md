# Text to Speech Project

## 1. Install dependencies

Open a terminal in the `backend` folder:

    cd backend
    python -m venv venv
    venv\Scripts\Activate.ps1          (Windows PowerShell)
    source venv/bin/activate           (Linux/macOS)
    pip install -r requirements.txt

System dependency (not a pip package): FFmpeg

    winget install Gyan.FFmpeg         (Windows, then reopen terminal)
    sudo apt install ffmpeg            (Ubuntu/Debian)
    brew install ffmpeg                (macOS)

## 2. Download the voice model (once)

Still in `backend` with the venv active:

    python -m piper.download_voices en_US-lessac-medium --download-dir voices

## 3. Run

    uvicorn main:app --reload

Open http://127.0.0.1:8000/docs to test the API, then open `frontend/index.html` in your browser.
