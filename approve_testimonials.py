# approve_testimonials.py
import json
from testimonial_class import Testimonial

# Load testimonials from a JSON file
def load_testimonials():
    try:
        with open('testimonials.json', 'r') as f:
            testimonials_data = json.load(f)
            return [Testimonial(**t) for t in testimonials_data]
    except FileNotFoundError:
        return []

# Save testimonials to a JSON file
def save_testimonials(testimonials):
    with open('testimonials.json', 'w') as f:
        json.dump([t.__dict__ for t in testimonials], f)

# Approve a testimonial
def approve_testimonial(index):
    testimonials = load_testimonials()
    pending_testimonials = [t for t in testimonials if not t.approved]
    
    if index < len(pending_testimonials):
        pending_testimonials[index].approved = True
        print(f"Approved testimonial from: {pending_testimonials[index].name}")
        save_testimonials(testimonials)
    else:
        print("Invalid index. No testimonial found.")

def main():
    testimonials = load_testimonials()
    pending_testimonials = [t for t in testimonials if not t.approved]

    # Display pending testimonials
    print("\nPending Testimonials:")
    for idx, testimonial in enumerate(pending_testimonials):
        print(f"[{idx}] {testimonial}")

    # Approve testimonial by index
    if pending_testimonials:
        try:
            index = int(input("Enter the index of the testimonial to approve: "))
            approve_testimonial(index)
        except ValueError:
            print("Invalid input. Please enter a number.")
    else:
        print("No pending testimonials.")

if __name__ == '__main__':
    main()

