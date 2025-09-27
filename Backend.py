from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample data structure
career_data = {
    "10th Class": {
        "MPC": {
            "skills": ["Math", "Physics", "Logical Thinking"],
            "next": "Intermediate MPC",
            "jobs": ["Engineer", "Scientist"]
        },
        "BiPC": {
            "skills": ["Biology", "Chemistry"],
            "next": "Intermediate BiPC",
            "jobs": ["Doctor", "Pharmacist"]
        }
    },
    "B.Tech": {
        "CSE": {
            "skills": ["Programming", "Problem Solving"],
            "next": "M.Tech or Job",
            "jobs": ["Software Developer", "Data Analyst"]
        }
    }
}

@app.route('/')
def home():
    return render_template('index.html', levels=career_data.keys())

@app.route('/subgroups', methods=['POST'])
def subgroups():
    level = request.json['level']
    return jsonify(list(career_data.get(level, {}).keys()))

@app.route('/details', methods=['POST'])
def details():
    level = request.json['level']
    subgroup = request.json['subgroup']
    return jsonify(career_data.get(level, {}).get(subgroup, {}))

if __name__ == '__main__':
    app.run(debug=True)
