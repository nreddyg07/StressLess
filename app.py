from flask import Flask, request, render_template

app = Flask(__name__)
questions = [
    "How often do you feel overwhelmed?",
    "Do you have trouble sleeping?",
    "Are you easily irritated or angered?",
    "Do you feel anxious frequently?",
    "How often do you feel fatigued?",
    "Do you have trouble concentrating?",
    "Have you experienced changes in appetite?",
    "Do you avoid social activities?",
    "Do you experience physical symptoms like headaches or muscle tension?",
    "Do you find it hard to relax?"
]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        stress_level = 0
        for i, question in enumerate(questions):
            answer = request.form.get(f'question{i}')
            if answer == 'Very often':
                stress_level += 2
            elif answer == 'Sometimes':
                stress_level += 1
        if stress_level >= 15:
            result = 'High Stress'
        elif stress_level >= 5:
            result = 'Moderate Stress'
        else:
            result = 'Low Stress'
        return render_template('index.html', result=result, questions=questions, enumerate=enumerate)
    return render_template('home.html', questions=questions, enumerate=enumerate)

if __name__ == '__main__':
    app.run(debug=True)
