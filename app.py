from flask import Flask, render_template, url_for, request, redirect, session

app = Flask(__name__)
app.secret_key = 'pineapples'

@app.route('/')
