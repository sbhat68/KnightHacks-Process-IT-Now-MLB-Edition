from flask import Flask, render_template, request
import data

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("main_page.html")

@app.route('/process', methods=['POST'])
def process():
    # Retrieve the HTTP POST request parameter value from 'request.form' dictionary
    _question = request.form.get('question')  # get(attr) returns None if attr is not present


    # Validate and send response
    if _question:
        return render_template('main_page_response.html', question=data.parse(_question))
    else:
        return render_template('main_page_null.html')

if __name__ == '__main__':
    app.run(debug=True)
