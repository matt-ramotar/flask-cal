import os
from flask import Blueprint, render_template
import psycopg2
from app.forms import AppointmentForm

bp = Blueprint('main', __name__, url_prefix='')

CONNECTION_PARAMETERS = {
    'user': os.environ.get('DB_USER'),
    'password': os.environ.get('DB_PASS'),
    'dbname': os.environ.get('DB_NAME'),
    'host': os.environ.get('DB_HOST'),
}


@bp.route('/')
def main():
    form = AppointmentForm()
    with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
        with conn.cursor() as curs:
            curs.execute('''
                SELECT id, name, start_datetime, end_datetime
                FROM appointments
                ORDER BY start_datetime;
                ''')
            rows = curs.fetchall()
            appointments = []
            for row in rows:
                appointments.append({
                    'id': row[0],
                    'name': row[1],
                    'start': row[2],
                    'end': row[3]
                })
    return render_template('main.html', appointments=appointments, form=form)
