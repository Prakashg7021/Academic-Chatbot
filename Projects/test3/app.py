import pandas as pd
from flask import Flask, render_template, request, redirect, session, url_for
import random
app = Flask(__name__)
app.secret_key = 'your_secret_key_here' # Set a secret key for session management

# A dictionary of users with their username and password
users = {'prakash': 'password123','john': 'password123', 'jane': 'password456', 'jack': 'password789'}

@app.route('/')
def home():
    if 'username' in session:
        return render_template('index.html')
    else:
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error='Invalid username or password')
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

@app.route('/get')
def get_bot_response():
    if 'username' in session:
        user_input = request.args.get('msg')
        bot_response = generate_bot_response(user_input)
        return str(bot_response)
    else:
        return redirect(url_for('login'))

# Chatbot response generation function
# def generate_bot_response(user_message):
#     # List of responses for different user messages
#     greeting_responses = ['Hi there!', 'Hello!', 'Greetings!', 'Howdy!']
#     name_responses = ['GVM BSc IT', 'Gyanodaya BSc IT']
#     location_responses = ['Our school is located in the heart of the city.', 'Our school is situated in a quiet suburb.', 'Our school is in a beautiful rural setting.']
#     program_responses = ['We offer a wide variety of programs including STEM, arts, and sports.', 'Our programs include robotics, coding, painting, and music.']
#     admission_responses = ['Our admissions process starts in January.', 'To apply, please visit our website and fill out the online application form.']
#     farewell_responses = ['Goodbye!', 'Take care!', 'See you later!', 'Bye!']
#     principal_responses=['Prof Meena Patil',]

#     # Process the user message and return a response
#     if user_message.lower() in ['hi', 'hello', 'hey']:
#         return random.choice(greeting_responses)
#     if user_message.lower() in ['what is your name of college?', 'Name of School','name']:
#         return random.choice(name_responses)
#     elif user_message.lower() in ['where is the school located?', 'what is the address of the school?','located', 'location']:
#         return random.choice(location_responses)
#     elif user_message.lower() in ['what programs does the school offer?', 'what courses are available?', 'what are the extracurricular activities?','extracurricular','activity','activities']:
#         return random.choice(program_responses)
#     elif user_message.lower() in ['how do I apply for admission?', 'when does the admission process start?', 'what is the admission process?','process','admission']:
#         return random.choice(admission_responses)
#     elif user_message.lower() in ['bye', 'goodbye']:
#         return random.choice(farewell_responses)
#     elif user_message.lower() in ['What is you principal name?','Your principal Name','principal']:
#         return random.choice(principal_responses)
#     else:
#         return "I'm sorry, I don't understand. Can you please try again?"



def generate_bot_response(user_message):
    # List of responses for different user messages
    greeting_responses = ['Hi there!', 'Hello!', 'Greetings!', 'Howdy!']
    name_responses = ['GVM BSc IT', 'Gyanodaya BSc IT']
    location_responses = ['Our school is located in the heart of the city.', 'Our school is situated in a quiet suburb.', 'Our school is in a beautiful rural setting.']
    program_responses = ['We offer a wide variety of programs including STEM, arts, and sports.', 'Our programs include robotics, coding, painting, and music.']
    admission_responses = ['Our admissions process starts in January.', 'To apply, please visit our website and fill out the online application form.']
    farewell_responses = ['Goodbye!', 'Take care!', 'See you later!', 'Bye!']
    principal_responses=['Prof Meena Patil']
    eligibility_responses=['The eligibility criteria for Bsc IT admission in GVM Bsc IT may vary depending on the program and course. Generally, you will need to have passed 10+2 (or equivalent) with Mathematics as a subject, and also meet the minimum marks requirement set by the institute.']
    dresscode_responses=['The dress code for students at GVM Bsc IT is regular. Students are required to wear formal attire such as shirts, trousers, and shoes to maintain a professional environment on campus.']
    fees_responses=['The fee structure for Bsc IT at GVM Bsc IT may vary depending on the program and course. You can visit the official website or contact the admission department for more details on the fee structure.']
    facility_responses=['GVM Bsc IT offers a variety of facilities to its students, including a library, computer lab, sports facilities, and a cafeteria.']
    durationprogram_responses=[' The Bsc IT program at GVM is a three-year full-time course.']
    hostel_responses=['Yes, GVM Bsc IT has a hostel facility for both male and female students. The hostel is equipped with all necessary amenities and is located within the campus.']
    campus_responses=['Our campus is located in a beautiful and vibrant community with state-of-the-art facilities and resources for students. You can find more information about our campus on our website or schedule a campus tour to see it for yourself.']
    classsize_resp=['The average class size varies depending on the program and level of study. Generally, our classes are small and intimate, with an emphasis on personalized attention and mentorship from faculty members']
    graduation_rate_resp=['The average graduation rate at GVM varies depending on the program and level of study. You can find more information about graduation rates on our website or contact our institutional research office for more information.']
    placement_resp=['GVM has a career center that provides a wide range of services and resources to help students with career planning, job search, and professional development. You can find more information about our career center on our website or contact our career services office for more information.']
    event_resp=['The student life at GVM is vibrant and diverse, with a variety of clubs, organizations, and events that cater to students interests and passions. You can find more information about student life on our website or contact our student affairs office for more information.']
    
    
    if ('school' in user_message and 'name' in user_message) or ('college' in user_message and 'name' in user_message):
        a = 'school name'
    elif 'located' in user_message or 'location' in user_message:
        a = 'located'
    elif any(s in user_message for s in ['admission', 'process']):
        a = 'admissionprocess'
    elif 'program' in user_message:
        a = 'program'
    elif 'eligibility' in user_message or 'criteria' in user_message:
        a = 'eligibility'
    elif 'dress' in user_message or 'dresscode' in user_message:
        a = 'dresscode'
    elif 'fees' in user_message or 'fee' in user_message:
        a = 'fees'
    elif any(s in user_message for s in ['placement', 'opportunities']):
        a = 'placement'
    elif 'facility' in user_message or 'facilities' in user_message:
        a = 'facility'
    elif 'duration' in user_message or 'duration of program' in user_message:
        a = 'durationprogram'
    elif 'hostel' in user_message or 'stayplace' in user_message:
        a = 'hostel'
    elif 'principal' in user_message:
        a = 'principal'
    elif 'campus' in user_message:
        a = 'campus'
    elif 'classsize' in user_message:
        a = 'classsize'
    elif 'graduation_rate' in user_message or 'graduation rate' in user_message or 'grad rate' in user_message:
        a = 'graduation_rate'
    elif 'placement' in user_message:
        a = 'placement'
    elif 'event' in user_message:
        a = 'event'

    
    
    # Process the user message and return a response
    if user_message.lower() in ['hi', 'hello', 'hey']:
        return random.choice(greeting_responses)
    elif a=='school name':
        return random.choice(name_responses)
    elif a=='located':
        return random.choice(location_responses)
    elif a=='program':
        return random.choice(program_responses)
    elif a=='admissionprocess':
        return random.choice(admission_responses)
    elif a=='eligibility':
        return random.choice(eligibility_responses)
    elif a=='dresscode':
        return random.choice(dresscode_responses)
    elif a=='fees':
        return random.choice(fees_responses)
    elif a=='facility':
        return random.choice(facility_responses)
    elif a=='durationprogram':
        return random.choice(durationprogram_responses)
    elif a=='hostel':
        return random.choice(hostel_responses)
    elif a=='principal':
        return random.choice(principal_responses)
    elif a=='campus':
        return random.choice(campus_responses)
    elif a=='classsize':
        return random.choice(classsize_resp)
    elif a=='graduation_rate':
        return random.choice(graduation_rate_resp)
    elif a=='placement':
        return random.choice(placement_resp)
    elif a=='event':
        return random.choice(event_resp)
    elif user_message.lower() in ['bye', 'goodbye']:
        return random.choice(farewell_responses)
    
    else:
        return "I'm sorry, I don't understand. Can you please try again?"


if __name__ == '__main__':
    app.run(debug=False)
