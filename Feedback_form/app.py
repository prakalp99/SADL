from flask import Flask, request, render_template_string
import re

app = Flask(__name__)

# Simple in-memory storage for feedback
feedback_list = []

def is_safe(input_text):
    # Backend Validation: Check for empty string or potential script tags
    if not input_text or re.search(r"<script.*?>.*?</script>", input_text, re.IGNORECASE):
        return False
    return True

@app.route('/', methods=['GET', 'POST'])
def feedback():
    error = None
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        message = request.form.get('message', '').strip()

        # Validate inputs on the backend
        if not name or not message:
             error = "All fields are required."
        elif not is_safe(name) or not is_safe(message):
             error = "Invalid characters detected (e.g., scripts are not allowed)."
        else:
            feedback_list.append({'name': name, 'message': message})
            return render_template_string(open('success.html').read())

    # Render form with potential error message
    return render_template_string(open('form.html').read(), error=error)

@app.route('/view')
def view_feedback():
    # Simple page to view all submitted feedback
    html = "<h2>All Feedback</h2><ul>"
    for item in feedback_list:
        html += f"<li><strong>{item['name']}:</strong> {item['message']}</li>"
    html += "</ul><a href='/'>Back to Form</a>"
    return html

if __name__ == '__main__':
    app.run(debug=True)