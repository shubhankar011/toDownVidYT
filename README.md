<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>toDownVidYT - Project Overview</title>
  <style>
    body {
      font-family: "Poppins", sans-serif;
      background: linear-gradient(135deg, #3a3a58, #5f5fbf);
      color: #fff;
      margin: 0;
      padding: 20px;
      line-height: 1.6;
    }

    h1, h2, h3 {
      color: #ffcc70;
      margin-bottom: 10px;
    }

    h1 {
      text-align: center;
      margin-top: 10px;
      text-shadow: 0 0 8px rgba(255, 204, 112, 0.8);
    }

    p, li, td {
      color: #f0f0f0;
    }

    code {
      background: rgba(255, 255, 255, 0.1);
      padding: 3px 6px;
      border-radius: 5px;
      color: #ffae70;
    }

    pre {
      background: rgba(0, 0, 0, 0.3);
      padding: 12px;
      border-radius: 10px;
      overflow-x: auto;
      color: #e6e6e6;
    }

    table {
      border-collapse: collapse;
      width: 100%;
      margin-top: 10px;
      margin-bottom: 10px;
    }

    table, th, td {
      border: 1px solid rgba(255,255,255,0.2);
      padding: 10px;
    }

    th {
      background-color: rgba(255,255,255,0.15);
    }

    .section {
      margin-bottom: 40px;
    }

    footer {
      text-align: center;
      color: rgba(255,255,255,0.7);
      margin-top: 40px;
      font-size: 14px;
    }

    .highlight {
      color: #ffae70;
      font-weight: bold;
    }

    ul {
      list-style: square;
      margin-left: 20px;
    }
  </style>
</head>
<body>

  <h1>🎥 toDownVidYT</h1>
  <p style="text-align:center;"><b>Creator & Author — Shubhankar Kumar</b></p>
  <p style="text-align:center;"><i>“A project I began at the start of 2025 to explore YouTube video processing, backend scripting, and web-based automation using Python.”</i></p>

  <div class="section">
    <h2>🧩 Overview</h2>
    <p><b>toDownVidYT</b> is a two-part Python project designed to download YouTube videos or audio with full control over format, naming, and storage — first as a <b>CLI tool</b>, later expanded into a <b>web-based Flask interface</b>.</p>
  </div>

  <div class="section">
    <h2>🗂️ Project Structure</h2>
    <pre>
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
└── README.html / README.md      # Project documentation
    </pre>
  </div>

  <div class="section">
    <h2>⚙️ Features</h2>
    <ul>
      <li>🎬 Download YouTube videos and audio in multiple formats</li>
      <li>⚙️ Automatic folder creation and FFmpeg conversion</li>
      <li>🌐 Flask web interface with responsive UI</li>
      <li>🧩 CLI version with console-based progress output</li>
      <li>📦 Modular structure separating logic and interface</li>
    </ul>
  </div>

  <div class="section">
    <h2>🚀 Quick Start Guide</h2>

    <h3>1️⃣ Install Dependencies</h3>
    <pre><code>pip install -r requirements.txt</code></pre>

    <h3>2️⃣ Install FFmpeg</h3>
    <p>Download <b>FFmpeg 7.1 or newer</b> and add it to your system PATH.</p>
    <pre><code>ffmpeg -version</code></pre>

    <h3>▶️ Run CLI Version</h3>
    <pre><code>cd CLI
python main_02.py</code></pre>
    <ul>
      <li>Enter YouTube video URL</li>
      <li>Select format and download directory</li>
      <li>Enter optional filename</li>
    </ul>

    <h3>🌐 Run Web Version</h3>
    <pre><code>cd WEB-based
python app.py</code></pre>
    <p>Then open your browser at:</p>
    <pre><code>http://127.0.0.1:5000</code></pre>
    <p>Paste a link, select a format, and click <b>Download</b>. Files appear in the <code>/downloads</code> folder.</p>
  </div>

  <div class="section">
    <h2>🎬 Playback Options</h2>
    <ul>
      <li>To open automatically in VLC:
        <pre><code>pip install python-vlc</code></pre>
      </li>
      <li>To open in Windows Media Player — simply run from any interpreter.</li>
    </ul>
  </div>

  <div class="section">
    <h2>🧠 Technical Notes</h2>
    <ul>
      <li>Uses <b>yt-dlp</b> for extraction, handling DASH streams, and FFmpeg merging</li>
      <li>FFmpeg performs <code>.webm → .mp4</code> conversion (takes ~1–2 minutes for HD)</li>
      <li>Subtitles can be embedded if available (<code>writesubtitles=True</code>)</li>
    </ul>
  </div>

  <div class="section">
    <h2>🧩 Update Log</h2>
    <table>
      <tr><th>Date</th><th>Update</th><th>Description</th></tr>
      <tr><td>05 Jan 2025</td><td>Update 1</td><td>Added more configurations to yt-dlp options dictionary</td></tr>
      <tr><td>07 Jan 2025</td><td>Update 2</td><td>Fixed bug causing files not to open automatically</td></tr>
      <tr><td>08 Jan 2025</td><td>Update 3</td><td>Error handling, folder auto-creation, audio-only & HD/SD mode</td></tr>
      <tr><td>10 Jan 2025</td><td>Update 4</td><td>Fixed file-opening issue</td></tr>
      <tr><td>11 Jan 2025</td><td>Issue</td><td>FFmpeg conversion delay (~2 min)</td></tr>
      <tr><td>04 Feb 2025</td><td>Update 5</td><td>Removed auto file-opening</td></tr>
      <tr><td>11 Mar 2025</td><td>Update 6</td><td>Rewrote code to comply with YouTube policy changes</td></tr>
      <tr><td>20 Jun 2025</td><td>Update 7</td><td>Added cookie file handling support</td></tr>
      <tr><td>26 Sep 2025</td><td>Update 8</td><td>Started GUI (Beta branch)</td></tr>
      <tr><td>27 Sep 2025</td><td>Update 9</td><td>GUI Beta improvements</td></tr>
      <tr><td>29 Oct 2025</td><td>Update 10</td><td>Minor fixes and CSS improvements</td></tr>
      <tr><td>30 Oct 2025</td><td>Update 11</td><td>Released stable web-based version (merged into main)</td></tr>
    </table>
  </div>

  <div class="section">
    <h2>🧭 Roadmap</h2>
    <ul>
      <li>[ ] Add real-time progress percentage in web version</li>
      <li>[ ] Implement multi-threaded FFmpeg merging</li>
      <li>[ ] Add video thumbnail preview before download</li>
      <li>[ ] User-uploadable cookies for private videos</li>
      <li>[ ] Implement download queue & history management</li>
    </ul>
  </div>

  <footer>
    <p>© 2025 <b>Shubhankar Kumar</b> — All rights reserved.</p>
    <p><i>“Built with Flask, yt-dlp, and passion for coding.”</i></p>
  </footer>

</body>
</html>
