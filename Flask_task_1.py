from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Go to /getname?name=yourname"

@app.route('/getname')
def get_name():
    name = request.args.get('name')

    if name:
        return f"Hello {name.upper()} 👋"
    else:
        return "Please provide a name in URL"

if __name__ == '__main__':
    app.run(debug=True)