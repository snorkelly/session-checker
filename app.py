from flask import Flask, request, render_template

app = Flask(__name__)

# Route for the home page
@app.route('/', methods=['GET', 'POST'])
def home():
    results = None

    if request.method == 'POST':
        # Get the input text from the form
        input_text = request.form['input_text']

        # Perform word search and get results
        results = perform_word_search(input_text)

    return render_template('index.html', results=results)

def perform_word_search(input_text):
    # Replace this with your code for finding the word 'TRAININGS' in input_text
    # You can use the provided code or implement your own logic here
    # Return the count of occurrences of the word 'TRAININGS'

    # Example code for finding the count of 'TRAININGS' using string method
    count = input_text.upper().count('TRAININGS')

    return count

if __name__ == '__main__':
    app.run(debug=True)
