from flask import render_template,redirect,flash,url_for,request,abort
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager,login_user,logout_user,login_required,current_user
import os
from app import db,app

app.config['UPLOAD'] ="Post_anything/static/profile_pics"


login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)


from models import User,Post,Comment
from forms import CommentForm

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/",methods=["GET","POST"])
def signup():
    if request.method=="POST":
        username=request.form.get("username")
        email=request.form.get('email')
        pswd=request.form.get('password')
        cpswd=request.form.get('ConfirmPassword')
        bio=request.form.get('bio')
        file=request.files['filename']
        ext = os.path.splitext(file.filename)[1]
        allowed_extensions = ['.jpg', '.png', '.jpeg']
        if file and ext in allowed_extensions:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD'], filename))
        else:
            flash("Please Upload Only Image Files! ")
        if cpswd != pswd:
            flash("The Passwords do not Match","error")
        elif len(username)<=4:
            flash("Username should be above 4 characters","error")
        else:
            hashed = generate_password_hash(pswd)
            try:
                db.session.add(User(username=username,email=email,password=hashed,bio=bio,image_file=filename))
                db.session.commit()
                flash("Succes Account Created","success")
                return redirect(url_for("signin"))
            except:
                flash("Please try Again!","error")
                return redirect(url_for("signup"))
    return render_template('signup.html')

@app.route('/signin',methods=["GET","POST"])
def signin():
    if request.method=="POST":
        username=request.form.get('username')
        pswd=request.form.get('password')
        user=User.query.filter_by(username=username).first()
        if not user or not (check_password_hash(user.password,pswd)):
            flash("Invalid User Name or Password","error")
            return redirect(url_for('signin'))
        else:
            login_user(user)
            return redirect(url_for('home_page'))
    return render_template('signin.html')


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('signin'))

@app.route("/home",methods=["GET","POST"])
@login_required
def home_page():
            page = request.args.get('page', 1, type=int)
            posts=Post.query.paginate(page=page, per_page=5)
            posts_dict = {post.id: post for post in posts}
            return render_template('home.html',posts_dict=posts_dict,posts=posts)


@app.route("/create_a_post",methods=["GET","POST","PUT"])
def create_a_post():
    if request.method=="POST":
        title=request.form.get('title')
        desc=request.form.get('description')
        if len(title) == 0:
            flash("title Cannot be Empty","error")
        else:
            # try:
                poster=current_user.id
                db.session.add(Post(title=title, desc=desc,poster_id=poster))
                db.session.commit()
                flash("Post Added","success")
                return redirect(url_for("home_page"))
            # except:
            #        flash("Please try Again!")
            #        return redirect(url_for("create_a_post"))
    return render_template('create.html')

def comment_exists(comment,author):
        return Comment.query.filter_by(comment=comment,comment_author=author).first()

@app.route("/blog_post/<id>",methods=["GET","POST","PUT"])
def blog_post(id):
    form = CommentForm()
    if request.method=="POST":
        if form.validate_on_submit():
            comment = form.comment.data
            if comment_exists(comment,current_user.username):
                flash("You have already commented!","error")
            else:
                db.session.add(Comment(post_id=id,comment=comment,comment_author=current_user.username))
                db.session.commit()
    blog=Post.query.filter_by(id=id).first()

    comment=Comment.query.filter_by(post_id=id)
    return render_template('blog.html',blog=blog,comments=comment,form=form,user=current_user.username)


@app.route("/profile/<author>/")
def profile_page(author):
    user=User.query.filter_by(username=author).first()
    file_name="profile_pics/{}".format(user.image_file)
    return render_template("profile.html",author=author,bio=user.bio,posts=user.posts,image_file=url_for('static', filename=file_name))

@app.route("/post/id/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('home_page'))