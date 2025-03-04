# 🌾 Farmer Detail Form and Insights Dashboard  

A Flask-based application for collecting, verifying, and storing farmer details, integrated with PostgreSQL and Tableau for creating insightful dashboards to improve processes.  

---

## 🚀 Features  
✅ **Data Collection**:  
   - Collects key details from farmers via an intuitive HTML form.  
   - Includes fields like Farmer's Name, Field Manager's Details, and more (10-13 inputs).  

✅ **Data Validation**:  
   - Ensures accurate data.  
   - Shows a 🔔 **flash message** if errors are detected, prompting corrections.  

✅ **Database Integration**:  
   - Stores verified data in a **PostgreSQL** database.
   -  <img src="images/database.png" width="800" />

     

✅ **Tableau Integration**:  
   - Connects PostgreSQL to Tableau to deliver actionable dashboards and key insights.
   - <img src="images/dashboard.png" width="800" />

---

## 🛠️ Prerequisites  
Ensure the following are installed:  
- **Python** (3.8 or later)  
- **Flask**:  
  ```bash  
  pip install flask psycopg2

  git clone https://github.com/your-repo/farmer-detail-form.git  
  cd farmer-detail-form
  
  python -m venv venv  
  source venv/bin/activate


  CREATE TABLE farmer_details (  
    id SERIAL PRIMARY KEY,  
    farmer_name VARCHAR(100),   
    contact_number VARCHAR(15),  
    address TEXT,  
    -- Add other fields as required  
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  
  );


  app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/farmer_data'


  python app.py  


farmer-detail-form/  
├── app.py              # Flask backend logic  
├── templates/          # HTML templates for the form  
├── schema.sql          # SQL schema for database setup  
└── README.md           # Project documentation  

<img src="images/form.png" width="800" />




