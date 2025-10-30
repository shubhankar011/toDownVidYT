# 🎥 toDownVidYT
### Creator & Author — **Shubhankar Kumar**

> *“A project I began at the start of 2025 to explore YouTube video processing, backend scripting, and web-based automation using Python. Over time, it evolved from a CLI downloader into a full Flask web application with modular design and UI.”*

## 🧩 Overview
**toDownVidYT** is a two-part Python project designed to download YouTube videos or audio with full control over format, naming, and storage — first as a **command-line tool**, later expanded into a **web-based Flask interface**.

It uses **yt-dlp** as the core downloading engine and **FFmpeg** for postprocessing and format conversion.

---

## 🗂️ Project Structure
toDownVidYT/
│
├── CLI/                         # Console-based version
│   └── main.py                  # Original yt-dlp script with user input and console logging
│
├── WEB-based/                   # Flask web application
│   ├── app.py                   # Flask routes and integration
│   ├── main_02.py               # Backend logic for yt-dlp
│   ├── templates/
│   │   └── index.html           # Web UI (form input + dynamic messages)
│   ├── static/
│   │   └── css/
│   │       └── style-02.css     # Responsive CSS design
│   └── downloads/               # Output folder for downloaded media
│
├── requirements.txt             # Dependencies (Flask, yt-dlp, etc.)
└── README.md                    # Project documentation

---

## ⚙️ Core Features
### 🧮 CLI Version
- Full terminal-based interaction  
- Dynamic format selection (`bestaudio`, `bestvideo`, `bestaudio+bestvideo`, `best`)  
- Auto-creates download folders if missing  
- Handles FFmpeg conversion automatically  
- Console logs all operations for debugging and clarity  

### Web-Based Version
- Flask-powered web interface  
- Responsive HTML + CSS front-end  
- Real-time progress animation  
- Format dropdown selection  
- Downloads stored in `/downloads`  
- Optional cookies.txt integration (for private videos)  
- Backend error handling and FFmpeg merging  

---

## Quick Start Guide

### Install dependencies
```bash
pip install -r requirements.txt```
2️⃣ Install FFmpeg
Download FFmpeg 7.1 or newer and add it to your system PATH.
You can verify it by running:

bash
Copy code
ffmpeg -version
▶️ Run CLI Version
bash
Copy code
cd CLI
python main_02.py
You’ll be asked to:

Enter a YouTube video URL

Select a format and download directory

Enter an optional filename

The CLI version also prints available formats and shows real-time progress directly in the terminal.

🌐 Run Web Version
bash
Copy code
cd WEB-based
python app.py
Then open your browser and go to:

cpp
Copy code
http://127.0.0.1:5000
Paste a YouTube link, choose your format, and click Download.
Files will appear inside the /downloads folder.

🎬 Playback Options
▶️ To open automatically in VLC
bash
Copy code
pip install python-vlc
Then run the CLI version using IDLE Python.

💿 To open with Windows Media Player
Simply run the script from any Python interpreter — it works automatically.

🧠 Technical Notes
Uses yt-dlp for extraction, handling DASH streams, and FFmpeg merging.

FFmpeg performs .webm → .mp4 conversion (takes ~1–2 minutes for HD).

Subtitles can be embedded if available (writesubtitles=True).

Cookie support (optional): add a cookies.txt next to main_02.py.
| Date            | Update                          | Description                                                                 |
| --------------- | ------------------------------- | --------------------------------------------------------------------------- |
| **05 Jan 2025** | Update 1                        | Added more configurations to yt-dlp options dictionary                      |
| **07 Jan 2025** | Update 2                        | Fixed bug causing downloaded files to not open automatically                |
| **08 Jan 2025** | Update 3 *(v01.8.3a)*           | Major update: error handling, folder auto-creation, audio-only & HD/SD mode |
| **10 Jan 2025** | Update 4                        | Fixed file-opening issue                                                    |
| **11 Jan 2025** | Issue                           | FFmpeg conversion delay (~2 min) on `.webm → .mp4`                          |
| **04 Feb 2025** | Update 5                        | Removed auto file-opening for stability                                     |
| **11 Mar 2025** | Update 6                        | Rewrote code to comply with updated YouTube policy changes                  |
| **20 Jun 2025** | Update 7                        | Added cookie file handling support                                          |
| **26 Sep 2025** | Update 8                        | Began work on GUI (Beta branch)                                             |
| **27 Sep 2025** | Update 9                        | GUI Beta improvements and performance tweaks                                |
| **29 Oct 2025** | Update 10                       | Minor fixes and CSS improvements in Beta                                    |
| **30 Oct 2025** | Update 11 *(Final Beta → Main)* | Released stable web-based version, merged into main branch                  |
Roadmap (Upcoming)

<li> Add real-time progress percentage in web version

 <li>Implement multi-threaded FFmpeg merging for faster processing

<li> Add video thumbnail preview before download

 <li>User-uploadable cookies (private video support)

 <li>Implement download queue & history management

## Author

###Shubhankar Kumar

<code>“Every version of this project taught me something new — from console handling to web routing, from debugging yt-dlp internals to designing responsive UIs.
This project isn’t just a downloader; it’s my 2025 journey of becoming a better developer.”
License</code>

Open for educational and personal use.
Attribution is appreciated if modified or redistributed.
