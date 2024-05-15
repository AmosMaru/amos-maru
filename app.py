from flask import Flask, render_template

app = Flask(__name__, static_folder='static')


@app.route('/', methods=['GET'])
def render_index():
    return render_template('index.html')

# @app.route('/about.html', methods=['GET'])
# def render_about():
#     return render_template('about.html')

# @app.route('/blog.html', methods=['GET'])
# def render_blog():
#     return render_template('blog.html')

# @app.route('/contact.html', methods=['GET'])
# def render_contact():
#     return render_template('contact.html')

# @app.route('/single.html', methods=['GET'])
# def render_single():
#     return render_template('single.html')


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
