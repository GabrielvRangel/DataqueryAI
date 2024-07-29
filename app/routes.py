from flask import Blueprint, request, jsonify, render_template
from .services.database import generate_sql, execute_query

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template('index.html')

@main_bp.route('/ask', methods=['POST'])
def ask():
    user_query = request.form['query']
    try:
        sql_query = generate_sql(user_query)
        result = execute_query(sql_query)
        return jsonify({'query': sql_query, 'result': result})
    except Exception as e:
        return jsonify({'error': str(e), 'query': sql_query})
