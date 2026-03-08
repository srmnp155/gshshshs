from flask import Blueprint, request, render_template
from services.quadratic_solver import solve_quadratic

calculator_bp = Blueprint('calculator', __name__, template_folder='../templates')

@calculator_bp.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None
    if request.method == 'POST':
        try:
            a = float(request.form.get('a', 0))
            b = float(request.form.get('b', 0))
            c = float(request.form.get('c', 0))
            result = solve_quadratic(a, b, c)
        except ValueError:
            error = 'Please enter valid numeric values for a, b, and c.'
    return render_template('index.html', result=result, error=error)
