

from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get')
def get_bot_response():
    user_input = request.args.get('msg')
    bot_response = generate_bot_response(user_input)
    return str(bot_response)
# ###
# def generate_bot_response(user_input):
#     # Here, you would write the code to generate a response from your chatbot based on the user's input.
#     # For this example, we'll just return a random response from a list of options.
#     a=user_input
#     responses = ['I am doing well!', 'Thank you for asking.', 'Sorry, I did not understand your question.']
#     return random.choice(responses)+" "+a
# ####

def generate_bot_response(user_message):
    # List of responses for different user messages
    greeting_responses = ['Hi there!', 'Hello!', 'Greetings!', 'Howdy!']
    name_responses = ['GVM BSc IT', 'Gyanodaya BSc IT']
    location_responses = ['Our school is located in the heart of the city.', 'Our school is situated in a quiet suburb.', 'Our school is in a beautiful rural setting.']
    program_responses = ['We offer a wide variety of programs including STEM, arts, and sports.', 'Our programs include robotics, coding, painting, and music.']
    admission_responses = ['Our admissions process starts in January.', 'To apply, please visit our website and fill out the online application form.']
    farewell_responses = ['Goodbye!', 'Take care!', 'See you later!', 'Bye!']
    principal_responses=['Prof Meena Patil',]

    # Process the user message and return a response
    if user_message.lower() in ['hi', 'hello', 'hey']:
        return random.choice(greeting_responses)
    if user_message.lower() in ['what is your name of college?', 'Name of School']:
        return random.choice(name_responses)
    elif user_message.lower() in ['where is the school located?', 'what is the address of the school?']:
        return random.choice(location_responses)
    elif user_message.lower() in ['what programs does the school offer?', 'what courses are available?', 'what are the extracurricular activities?']:
        return random.choice(program_responses)
    elif user_message.lower() in ['how do I apply for admission?', 'when does the admission process start?', 'what is the admission process?']:
        return random.choice(admission_responses)
    elif user_message.lower() in ['bye', 'goodbye']:
        return random.choice(principal_responses)
    elif user_message.lower() in ['What is you principal name?','Your principal Name']:
        
        return random.choice(farewell_responses)
    else:
        return "I'm sorry, I don't understand. Can you please try again?"



if __name__ == '__main__':
    app.run(debug=False)
