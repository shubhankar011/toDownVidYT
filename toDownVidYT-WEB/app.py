from flask import Flask, render_template, request, send_from_directory
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

                if os.path.exists('/tmp'):
                    for file in os.listdir('/tmp'):
                        if file.startswith('downloaded_video'):
                            try:
                                os.remove(os.path.join('/tmp', file))
                            except:
                                pass

                yt_iops(url, output, '/tmp', name='downloaded_video', choice_index=choice_index)
                for file in os.listdir('/tmp'):
                    if file.startswith('downloaded_video'):
                        message = "File Downloaded!"
                        return send_from_directory('/tmp', file, as_attachment=True)
                message = "Error: File was downloaded but could not be located."
            except Exception as e:
                message = f"Error: {e}"

    return render_template('index.html', message=message)


if __name__ == "__main__":
    app.run(debug=True)
