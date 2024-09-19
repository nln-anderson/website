class Testimonial:
    def __init__(self, name, school, message, approved = False):
        self.name = name
        self.school = school
        self.message = message
        self.approved = approved

    def __repr__(self) -> str:
        return f"Name: {self.name}, School: {self.school}, Message: {self.message}, Approved: {self.approved}"