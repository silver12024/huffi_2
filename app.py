from flask import Flask,render_template,request
app = Flask(__name__)

@app.route("/",method=['POST'])
def main():
    return render_template['index.html']
def process():
	_number=request.form['number']
	if_number:
		return bin(_number)
