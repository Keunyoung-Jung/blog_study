from flask import Flask, Blueprint, request, render_template,make_response\
    ,jsonify,redirect,url_for,session
from flask_login import login_user,current_user,logout_user
from blog_control.user_mgmt import User
import datetime
from blog_control.session_mgmt import BlogSession

blog_abtest = Blueprint('blog', __name__,template_folder='templates')
print(blog_abtest.__dict__)


@blog_abtest.route('/set_email',methods=['GET','POST'])
def set_email():
    if request.method == 'GET' :
        print('set email',request.args.get('user_email'))
        return redirect(url_for('blog.test_blog'))
    else :
        # print('set_email', request.headers)
        print('set_email',request.form['user_email'],request.form['blog_id'])
        user = User.create(request.form['user_email'],request.form['blog_id'])
        login_user(user,remember=True, duration=datetime.timedelta(days=30))
        return redirect(url_for('blog.test_blog'))
    # return make_response(jsonify(success=True),200)
    
@blog_abtest.route('/logout')
def logout():
    User.delete(current_user.id)
    logout_user()
    return redirect(url_for('blog.test_blog'))
    
@blog_abtest.route('/test_blog')
def test_blog():
    # BlogSession.get_blog_page()
    if current_user.is_authenticated :
        web_page_name = BlogSession.get_blog_page(current_user.blog_id)
        BlogSession.save_session_info(session['client_id'],current_user.user_email,web_page_name)
        return render_template(
            web_page_name,
            user_email=current_user.user_email)
    else:
        web_page_name = BlogSession.get_blog_page()
        BlogSession.save_session_info(session['client_id'],'anonymous',web_page_name)
        return render_template(web_page_name)
