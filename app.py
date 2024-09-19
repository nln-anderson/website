from flask import Flask, render_template, request, redirect, url_for
from testimonial_class import Testimonial
import json

app = Flask(__name__)

# Database of testimonials

# Load testimonials from the JSON file
def load_testimonials():
    try:
        with open('testimonials.json', 'r') as f:
            testimonials_data = json.load(f)
            return [Testimonial(**t) for t in testimonials_data]
    except FileNotFoundError:
        return []
    
# Save testimonials to the JSON file
def save_testimonials(testimonials):
    with open('testimonials.json', 'w') as f:
        json.dump([t.__dict__ for t in testimonials], f)

@app.route('/')
def index():
    testimonials = load_testimonials()
    # Only show approved testimonials
    approved_testimonials = [t for t in testimonials if t.approved]
    return render_template('index.html', testimonials=approved_testimonials)

@app.route('/submit', methods=['POST'])
def submit_testimonial():
    name = request.form['name']
    school = request.form['school']
    message = request.form['message']
    
    # Create a new Testimonial object (unapproved by default)
    new_testimonial = Testimonial(name, school, message)
    testimonials = load_testimonials()
    testimonials.append(new_testimonial)
    save_testimonials(testimonials)

    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)