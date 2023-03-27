from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, Email, Length
from flask_ckeditor import CKEditorField


# #WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


class RegisterForm(FlaskForm):
    email = StringField(label="E-mail", validators=[DataRequired(), Email("This field requires a valid email address.")])
    password = PasswordField(label="Password", validators=[DataRequired()])
    name = StringField(label="Name", validators=[DataRequired(), Length(max=1000)])
    submit = SubmitField(label='Sign Me Up!')


class LoginForm(FlaskForm):
    email = StringField(label="E-mail", validators=[DataRequired(), Email("This field requires a valid email address.")])
    password = PasswordField(label="Password", validators=[DataRequired()])
    submit = SubmitField(label='Let Me In!')


class CommentForm(FlaskForm):
    comment_txt = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField(label='SUBMIT COMMENT')

