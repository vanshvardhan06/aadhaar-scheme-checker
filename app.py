from flask import Flask, render_template, request

app = Flask(__name__)

# Dummy data for Aadhaar owners
aadhaar_data = [
    {'aadhaar_number': '123456789012', 'name': 'Amit Sharma', 'address': '123 Main Street, Delhi', 'eligible_schemes': ['PMJDY', 'PM-KISAN'], 'dob': '1990-05-15', 'gender': 'Male'},
    {'aadhaar_number': '234567890123', 'name': 'Pooja Reddy', 'address': '456 Park Lane, Mumbai', 'eligible_schemes': ['PM Ujjwala', 'PM-KISAN'], 'dob': '1988-03-22', 'gender': 'Female'},
    {'aadhaar_number': '345678901234', 'name': 'Ravi Kumar', 'address': '789 Oak Road, Bangalore', 'eligible_schemes': ['Ayushman Bharat', 'PMJDY'], 'dob': '1995-11-10', 'gender': 'Male'},
    {'aadhaar_number': '456789012345', 'name': 'Anjali Patel', 'address': '321 Rose Avenue, Jaipur', 'eligible_schemes': ['PMJDY', 'PM Ujjwala', 'Ayushman Bharat'], 'dob': '1992-07-18', 'gender': 'Female'},
    {'aadhaar_number': '567890123456', 'name': 'Vikram Singh', 'address': '987 Palm Drive, Hyderabad', 'eligible_schemes': ['PM-KISAN', 'PM Ujjwala'], 'dob': '1987-12-02', 'gender': 'Male'},
    {'aadhaar_number': '678901234567', 'name': 'Neha Gupta', 'address': '654 Green Street, Kolkata', 'eligible_schemes': ['Ayushman Bharat', 'PM-KISAN'], 'dob': '1994-09-25', 'gender': 'Female'},
    {'aadhaar_number': '789012345678', 'name': 'Rohit Verma', 'address': '987 Elm Street, Pune', 'eligible_schemes': ['PMJDY', 'Ayushman Bharat'], 'dob': '1991-01-30', 'gender': 'Male'},
    {'aadhaar_number': '890123456789', 'name': 'Sushmita Das', 'address': '159 Lily Road, Chennai', 'eligible_schemes': ['PM Ujjwala', 'PMJDY'], 'dob': '1993-06-12', 'gender': 'Female'},
    {'aadhaar_number': '901234567890', 'name': 'Aakash Yadav', 'address': '258 Mango Lane, Lucknow', 'eligible_schemes': ['PM-KISAN', 'PM Ujjwala', 'Ayushman Bharat'], 'dob': '1989-02-20', 'gender': 'Male'},
    {'aadhaar_number': '102345678901', 'name': 'Rina Bhagat', 'address': '369 Lotus Avenue, Surat', 'eligible_schemes': ['PMJDY', 'Ayushman Bharat'], 'dob': '1990-10-03', 'gender': 'Female'},
    {'aadhaar_number': '213456789012', 'name': 'Mohit Chauhan', 'address': '741 Jasmine Street, Delhi', 'eligible_schemes': ['PMJDY', 'PM Ujjwala', 'PM-KISAN'], 'dob': '1986-04-17', 'gender': 'Male'},
    {'aadhaar_number': '324567890123', 'name': 'Isha Singh', 'address': '852 Willow Drive, Bangalore', 'eligible_schemes': ['Ayushman Bharat', 'PM-KISAN'], 'dob': '1996-08-05', 'gender': 'Female'},
    {'aadhaar_number': '435678901234', 'name': 'Shivani Kumar', 'address': '963 Orchid Road, Mumbai', 'eligible_schemes': ['PMJDY', 'PM Ujjwala'], 'dob': '1993-04-22', 'gender': 'Female'},
    {'aadhaar_number': '546789012345', 'name': 'Harsh Vardhan', 'address': '258 Bluebell Street, Ahmedabad', 'eligible_schemes': ['PM Ujjwala', 'Ayushman Bharat'], 'dob': '1988-01-19', 'gender': 'Male'},
    {'aadhaar_number': '657890123456', 'name': 'Divya Mehta', 'address': '147 Maple Road, Chennai', 'eligible_schemes': ['PM-KISAN', 'Ayushman Bharat'], 'dob': '1992-11-11', 'gender': 'Female'}
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/entry')
def entry():
    return render_template('entry.html')
    
@app.route('/scheme-info')
def scheme_info():
    return render_template('scheme-info.html')

@app.route('/check_eligibility', methods=['GET'])
def check_eligibility():
    aadhaar_number = request.args.get('aadhar')  # Extract Aadhaar number from query parameter
    
    # Check if the Aadhaar number exists in the data
    for person in aadhaar_data:
        if person['aadhaar_number'] == aadhaar_number:
            eligible_schemes = person['eligible_schemes']
            return render_template('eligible-scheme.html', name=person['name'], dob=person['dob'], address=person['address'], gender=person['gender'], aadhaar=aadhaar_number, schemes=eligible_schemes)

    return "Aadhaar Number not eligible for any scheme", 404  # If not found, return 404 error

if __name__ == '__main__':
    app.run(debug=True)
