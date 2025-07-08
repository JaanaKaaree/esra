from flask import Flask, render_template
from flask_frozen import Freezer

app = Flask(__name__)
app.config['FREEZER_DESTINATION'] = 'output'
app.config['FREEZER_RELATIVE_URLS'] = True
freezer = Freezer(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/business-services.html')
def business_services():
    return render_template('business-services.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/getting-started.html')
def getting_started():
    return render_template('getting-started.html')

@app.route('/training-services.html')
def training_services():
    return render_template('training-services.html')

@app.route('/ideas-to-stories.html')
def ideas_to_stories():
    return render_template('ideas-to-stories.html')

@app.route('/bot-builder.html')
def bot_builder():
    return render_template('bot-builder.html')

@app.route('/smart-business.html')
def smart_business():
    return render_template('smart-business.html')

@app.route('/ai-business-playbook.html')
def ai_business_playbook():
    return render_template('ai-business-playbook.html')

@app.route('/ai-for-podcast.html')
def ai_for_podcast():
    return render_template('ai-for-podcast.html')

@app.route('/ai-for-video.html')
def ai_for_video():
    return render_template('ai-for-video.html')

if __name__ == '__main__':
    # Freeze the site
    freezer.freeze()
