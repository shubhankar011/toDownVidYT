from flask import Flask, render_template, request
import os
from main_02 import yt_iops

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def YTD():
    message = None
    if request.method == 'POST':
        url = request.form.get('url')
        choice_index = int(request.form.get('format', 0))

        if not url:
            message = "Please enter a valid URL."
        else:
            try:
                output = ["bestaudio+bestvideo", "bestaudio", "bestvideo", "best"]
                path = os.path.join(os.getcwd(), 'downloads')
                if not os.path.exists(path):
                    os.makedirs(path)

                yt_iops(url, output, path, name=None, choice_index=choice_index)
                message = "Download completed successfully! File saved in 'downloads/'"
            except Exception as e:
                message = f"Error: {e}"

    return render_template('index.html', message=message)


if __name__ == "__main__":
    app.run(debug=True)
