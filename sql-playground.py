# sql-playground.py

from database_connection import connect_to_db

# SQL Query to create the farmers_data table
CREATE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS farmers_data (
    sr_no SERIAL PRIMARY KEY, 
    uid VARCHAR(50) NOT NULL UNIQUE, 
    program_year INT NOT NULL, 
    farmer_name VARCHAR(100) NOT NULL, 
    plantation_type_dense_fruit VARCHAR(50),
    total_land_area_acre DECIMAL(10, 2),
    area_f4f_acre DECIMAL(10, 2),
    district VARCHAR(100),
    block VARCHAR(100),
    water_available BOOLEAN DEFAULT FALSE,
    electricity_available BOOLEAN DEFAULT FALSE,
    kml_uploaded BOOLEAN DEFAULT FALSE,
    contract_uploaded BOOLEAN DEFAULT FALSE,
    land_record_uploaded BOOLEAN DEFAULT FALSE,
    cc_training_uploaded BOOLEAN DEFAULT FALSE,
    soil_sample_collected BOOLEAN DEFAULT FALSE,
    cc_training_date DATE,
    drone_ortho_taken BOOLEAN DEFAULT FALSE,
    farmer_payment_collected BOOLEAN DEFAULT FALSE,
    farmer_payment_date DATE,
    amount DECIMAL(12, 2),
    mode_collection_cash_upi_banktransfer VARCHAR(20),
    contract_date DATE,
    baseline_survey BOOLEAN DEFAULT FALSE,
    plantation_date DATE,
    trees_planted INT,
    mango_native INT DEFAULT 0,
    mango_grafted_kesar INT DEFAULT 0,
    lemon_sai_sharbati INT DEFAULT 0,
    sitaphal_native INT DEFAULT 0,
    sitaphal_golden INT DEFAULT 0,
    sitaphal_balanagar INT DEFAULT 0,
    awala INT DEFAULT 0,
    awala_grafted INT DEFAULT 0,
    peru INT DEFAULT 0,
    peru_sardar INT DEFAULT 0,
    chincha INT DEFAULT 0,
    chincha_grafted INT DEFAULT 0,
    jamun INT DEFAULT 0,
    jamun_bhardoli INT DEFAULT 0,
    chikku INT DEFAULT 0,
    orange INT DEFAULT 0,
    mosambi INT DEFAULT 0,
    dalimb INT DEFAULT 0,
    ramphal INT DEFAULT 0,
    drumstick_koimb INT DEFAULT 0,
    bamboo INT DEFAULT 0,
    karwand INT DEFAULT 0,
    arjun INT DEFAULT 0,
    katesawar INT DEFAULT 0,
    karanj INT DEFAULT 0,
    kaduneem INT DEFAULT 0,
    kanchan INT DEFAULT 0,
    kadamb INT DEFAULT 0,
    bhendi INT DEFAULT 0,
    shirish INT DEFAULT 0,
    ain INT DEFAULT 0,
    pimpal INT DEFAULT 0,
    vad INT DEFAULT 0,
    tamhan INT DEFAULT 0,
    waval INT DEFAULT 0,
    palas INT DEFAULT 0,
    babhul INT DEFAULT 0,
    bakul INT DEFAULT 0
);
"""

# Function to create the table if it doesn't exist
def create_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute(CREATE_TABLE_QUERY)
        connection.commit()
        print("Table created successfully!")
    except Exception as e:
        print(f"Error creating table: {e}")
    finally:
        cursor.close()

# Function to insert data into the farmers_data table
def insert_farmer_data(connection, data):
    try:
        cursor = connection.cursor()

        # Define the insert query
        query = """
        INSERT INTO farmers_data (
            uid, program_year, farmer_name, plantation_type_dense_fruit,
            total_land_area_acre, area_f4f_acre, district, block,
            water_available, electricity_available, kml_uploaded,
            contract_uploaded, land_record_uploaded, cc_training_uploaded,
            soil_sample_collected, cc_training_date, drone_ortho_taken,
            farmer_payment_collected, farmer_payment_date, amount,
            mode_collection_cash_upi_banktransfer, contract_date,
            baseline_survey, plantation_date, trees_planted
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        # Data to be inserted
        values = (
            data["uid"], data["program_year"], data["farmer_name"],
            data["plantation_type_dense_fruit"], data["total_land_area_acre"],
            data["area_f4f_acre"], data["district"], data["block"],
            data["water_available"], data["electricity_available"],
            data["kml_uploaded"], data["contract_uploaded"],
            data["land_record_uploaded"], data["cc_training_uploaded"],
            data["soil_sample_collected"], data["cc_training_date"],
            data["drone_ortho_taken"], data["farmer_payment_collected"],
            data["farmer_payment_date"], data["amount"],
            data["mode_collection_cash_upi_banktransfer"], data["contract_date"],
            data["baseline_survey"], data["plantation_date"], data["trees_planted"]
        )

        # Execute the query
        cursor.execute(query, values)

        # Commit the transaction
        connection.commit()

        print("Data inserted successfully!")
    except Exception as e:
        print(f"Error inserting data: {e}")
    finally:
        cursor.close()

# Main logic to connect and execute SQL operations
if __name__ == "__main__":
    # Connect to the database
    connection = connect_to_db()

    if connection:
        # Create the table
        create_table(connection)

        # Example data to insert for the first farmer
        farmer_data= {
            "uid": "F128",
            "program_year": 2025,
            "farmer_name": "Ramesh Kumar",
            "plantation_type_dense_fruit": "Mango",
            "total_land_area_acre": 5.5,
            "area_f4f_acre": 2.0,
            "district": "Pune",
            "block": "Haveli",
            "water_available": True,
            "electricity_available": True,
            "kml_uploaded": True,
            "contract_uploaded": True,
            "land_record_uploaded": True,
            "cc_training_uploaded": False,
            "soil_sample_collected": True,
            "cc_training_date": None,
            "drone_ortho_taken": True,
            "farmer_payment_collected": True,
            "farmer_payment_date": "2025-01-15",
            "amount": 1500.0,
            "mode_collection_cash_upi_banktransfer": "UPI",
            "contract_date": "2025-01-10",
            "baseline_survey": True,
            "plantation_date": "2025-01-20",
            "trees_planted": 400
        }

        # Insert the first farmer data
        insert_farmer_data(connection, farmer_data)

        
        # Close the connection
        connection.close()
