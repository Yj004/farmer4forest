from flask import Flask, render_template, request, flash, redirect, url_for
from database_connection import connect_to_db
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flash messages


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/", methods=['POST'])
def form():
    if request.method == 'POST':
        try:
            # Collect form data
            farmer_data = {
                "uid": request.form['uid'].strip(),
                "program_year": request.form['program_year'].strip(),
                "farmer_name": request.form['farmer_name'].strip(),
                "plantation_type_dense_fruit": request.form['plantation_type_dense_fruit'].strip(),
                "total_land_area_acre": float(request.form['total_land_area_acre']),
                "area_f4f_acre": float(request.form['area_f4f_acre']),
                "district": request.form['district'].strip(),
                "block": request.form['block'].strip(),
                "water_available": 'water_available' in request.form,
                "electricity_available": 'electricity_available' in request.form,
                "kml_uploaded": 'kml_uploaded' in request.form,
                "contract_uploaded": 'contract_uploaded' in request.form,
                "land_record_uploaded": 'land_record_uploaded' in request.form,
                "cc_training_uploaded": 'cc_training_uploaded' in request.form,
                "soil_sample_collected": 'soil_sample_collected' in request.form,
                "cc_training_date": request.form['cc_training_date'].strip(),
                "drone_ortho_taken": 'drone_ortho_taken' in request.form,
                "farmer_payment_collected": 'farmer_payment_collected' in request.form,
                "farmer_payment_date": request.form['farmer_payment_date'].strip(),
                "amount": float(request.form['amount']),
                "mode_collection_cash_upi_banktransfer": request.form['mode_collection_cash_upi_banktransfer'].strip(),
                "contract_date": request.form['contract_date'].strip(),
                "baseline_survey": 'baseline_survey' in request.form,
                "plantation_date": request.form['plantation_date'].strip(),
                "trees_planted": int(request.form['trees_planted'])
            }

            # Validation
            errors = []
            if len(farmer_data['uid']) < 3:
                errors.append("UID must be at least 3 characters long.")
            if farmer_data['total_land_area_acre'] <= 0:
                errors.append("Total Land Area must be greater than 0.")
            if farmer_data['trees_planted'] < 351:
                errors.append("Number of trees planted must be greater than 350.")
            try:
                datetime.strptime(farmer_data['cc_training_date'], '%Y-%m-%d')
                datetime.strptime(farmer_data['farmer_payment_date'], '%Y-%m-%d')
                datetime.strptime(farmer_data['contract_date'], '%Y-%m-%d')
                datetime.strptime(farmer_data['plantation_date'], '%Y-%m-%d')
            except ValueError:
                errors.append("One or more dates are invalid.")

            # Flagging logic: No electricity and no water
            if not farmer_data["water_available"] and not farmer_data["electricity_available"]:
                flash("Farmer has no electricity and no water. Data flagged for review.", "error")
                return redirect(url_for('index'))

            # Flash errors if any
            if errors:
                for error in errors:
                    flash(error, "error")
                return redirect(url_for('index'))

            # Check if UID exists
            if check_uid(farmer_data['uid']):
                flash(f"Error: UID {farmer_data['uid']} already exists in the database!", "error")
                return redirect(url_for('index'))

            # Insert data into the database
            save_to_database(farmer_data)
            flash("Form submitted successfully!", "success")
            return redirect(url_for('index'))

        except Exception as e:
            flash(f"An unexpected error occurred: {e}", "error")
            return redirect(url_for('index'))


def check_uid(uid):
    """Check if UID exists in the database."""
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        query = "SELECT uid FROM FARMERS_DATA WHERE uid = %s"
        cursor.execute(query, (uid,))
        result = cursor.fetchone()
        return result is not None
    except Exception as e:
        flash(f"Database error: {e}", "error")
        return False
    finally:
        if conn:
            cursor.close()
            conn.close()


def save_to_database(data):
    """Insert validated data into the database."""
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        query = """
        INSERT INTO FARMERS_DATA (uid, program_year, farmer_name, plantation_type_dense_fruit,
        total_land_area_acre, area_f4f_acre, district, block, water_available, electricity_available,
        kml_uploaded, contract_uploaded, land_record_uploaded, cc_training_uploaded, soil_sample_collected,
        cc_training_date, drone_ortho_taken, farmer_payment_collected, farmer_payment_date, amount,
        mode_collection_cash_upi_banktransfer, contract_date, baseline_survey, plantation_date, trees_planted)
        VALUES (%(uid)s, %(program_year)s, %(farmer_name)s, %(plantation_type_dense_fruit)s,
        %(total_land_area_acre)s, %(area_f4f_acre)s, %(district)s, %(block)s, %(water_available)s, 
        %(electricity_available)s, %(kml_uploaded)s, %(contract_uploaded)s, %(land_record_uploaded)s, 
        %(cc_training_uploaded)s, %(soil_sample_collected)s, %(cc_training_date)s, %(drone_ortho_taken)s, 
        %(farmer_payment_collected)s, %(farmer_payment_date)s, %(amount)s, 
        %(mode_collection_cash_upi_banktransfer)s, %(contract_date)s, %(baseline_survey)s, 
        %(plantation_date)s, %(trees_planted)s)
        """
        cursor.execute(query, data)
        conn.commit()
    except Exception as e:
        flash(f"Database error: {e}", "error")
    finally:
        if conn:
            cursor.close()
            conn.close()


if __name__ == '__main__':
    app.run(debug=True)
