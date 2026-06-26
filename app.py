from flask import Flask, render_template, request, url_for
from attendance import Subject
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('form.html')


@app.route('/form', methods=['POST'])
def form():
    n = int(request.form['num'])
    return render_template('dynamic_form.html', n=n)


@app.route('/result', methods=['POST'])
def result():
    try:
        subjects = []
        names = []
        percentages = []

        n = int(request.form['n'])

        for i in range(n):
            name = request.form[f'name{i}']
            attended = int(request.form[f'attended{i}'])
            total = int(request.form[f'total{i}'])

            sub = Subject(name, attended, total)
            data = sub.get_report()

            subjects.append(data)
            names.append(data["name"])
            percentages.append(data["percent"])

        # CREATE GRAPH
        if not os.path.exists('static'):
            os.makedirs('static')

        plt.figure()
        plt.bar(names, percentages)
        plt.xlabel("Subjects")
        plt.ylabel("Attendance %")
        plt.title("Attendance Analysis")

        plt.savefig('static/graph.png')
        plt.close()

        return render_template('result.html', subjects=subjects, graph=True)

    except:
        return "Invalid Input! Please enter valid numbers."


if __name__ == '__main__':
    app.run(debug=True)