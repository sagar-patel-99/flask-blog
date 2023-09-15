 from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

# Replace the SQLite database with a Python list to store posts
posts = []

def get_post(post_id):
    for post in posts:
        if post['id'] == post_id:
            return post
    abort(404)

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            post_id = len(posts) + 1
            new_post = {'id': post_id, 'title': title, 'content': content}
            posts.append(new_post)
            flash('Post created successfully!')
            return redirect(url_for('index'))

    return render_template('create.html')

@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            post['title'] = title
            post['content'] = content
            flash('Post updated successfully!')
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)

@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    post = get_post(id)
    posts.remove(post)
    flash('Post "{}" was successfully deleted!'.format(post['title']))
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000) 
