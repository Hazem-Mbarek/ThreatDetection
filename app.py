from flask import Flask, render_template, request, jsonify, send_from_directory
import joblib
import numpy as np
import random
import pandas as pd
from datetime import datetime
import os
from openai import OpenAI

app = Flask(__name__)

# Load the model and scaler
try:
    model = joblib.load('safety_predictor_model.joblib')
    scaler = joblib.load('scaler.joblib')
except Exception as e:
    print(f"Error loading model: {e}")

# Complete street name to encoding mapping
street_mapping = {
    "Avenue Habib Bourguiba": 0,
    "Avenue Hédi Nouira": 1,
    "Avenue Kheireddine Pacha": 2,
    "Avenue Louis Braille": 3,
    "Avenue Mohamed Ali": 4,
    "Avenue Mohamed V": 5,
    "Avenue Taieb Mehiri": 6,
    "Avenue de Londres": 7,
    "Avenue de Paris": 8,
    "Avenue de la Liberté": 9,
    "Avenue de la République": 10,
    "Avenue du 14 Janvier": 11,
    "Avenue du Stade": 12,
    "Boulevard de la Terre": 13,
    "Rue Hannibal": 14,
    "Rue Jamaa Ezzitouna": 15,
    "Rue Mohamed V": 16,
    "Rue Pierre de Coubertin": 17,
    "Rue Sidi Ben Arous": 18,
    "Rue d'Algérie": 19,
    "Rue d'Iran": 20,
    "Rue de Marseille": 21,
    "Rue de la Kasbah": 22,
    "Rue de la Plage": 23,
    "Rue des Entrepreneurs": 24,
    "Rue des Jasmins": 25,
    "Rue des Orangers": 26,
    "Rue des Sports": 27,
    "Rue des Suffetes": 28,
    "Rue du Caire": 29,
    "Rue du Lac Michigan": 30,
    "Rue du Lac Victoria": 31,
    "Rue du Lac Windermere": 32,
    "Rue du Musée": 33,
    "Rue du Pacha": 34,
    "Rue du Port": 35,
    "Souk El Attarine": 36,
    "Unknown": 37
}

# Load API key from environment variable instead
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

@app.route('/')
@app.route('/predict')
def predict_page():
    return render_template('index.html')

@app.route('/submit')
def submit_page():
    return render_template('submit.html')

@app.route('/predict_safety', methods=['POST'])
def predict_safety():
    try:
        request_data = request.get_json()
        hour = request_data.get('hour', 12)
        street = request_data.get('street', 'Avenue Habib Bourguiba')
        
        if not (0 <= hour <= 23):
            return jsonify({
                'status': 'error',
                'message': 'Hour must be between 0 and 23'
            }), 400

        is_night = 1 if (hour >= 20 or hour < 6) else 0

        # Define the feature columns in the correct order
        feature_columns = [
            "Lat", "Long", "Street_Lights", "Police_Presence", 
            "Emergency_Services", "Crowd_Level", "Active_Shops", 
            "Public_Transport", "Incident_Reports", "Emergency_Calls", 
            "Tourist_Season", "Hour", "Is_Weekend", "Is_Night", 
            "District_Encoded", "Street_Encoded", "Area_Risk_Score", 
            "Time_Risk_Score", "Street_Incident_Score", "Safety_Infrastructure"
        ]

        data = {
            "Lat": random.uniform(36.70, 36.90),
            "Long": random.uniform(10.10, 10.30),
            "Crowd_Level": random.randint(1, 5),
            "Active_Shops": random.randint(0, 39),
            "Incident_Reports": random.randint(0, 7),
            "Emergency_Calls": random.randint(0, 24),
            "Street_Lights": random.choice([0, 1]),
            "Police_Presence": random.choice([0, 1]),
            "Emergency_Services": random.choice([0, 1]),
            "Public_Transport": random.choice([0, 1]),
            "Tourist_Season": random.choice([0, 1]),
            "Hour": hour,
            "Is_Night": is_night,
            "Is_Weekend": random.choice([0, 1]),
            "District_Encoded": random.randint(0, 7),
            "Street_Encoded": street_mapping.get(street, 37),
            "Area_Risk_Score": random.uniform(1.0, 5.0),
            "Time_Risk_Score": random.uniform(1.0, 5.0),
            "Street_Incident_Score": random.uniform(1.0, 5.0),
            "Safety_Infrastructure": random.randint(0, 5)
        }

        features = [[data[feature] for feature in feature_columns]]
        scaled_features = scaler.transform(features)
        prediction = model.predict(scaled_features)[0]
        
        return jsonify({
            'status': 'success',
            'message': f'Predicted Risk Level: {int(prediction)} (1=Safest, 5=Most Dangerous)'
        })

    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/submit_incident', methods=['POST'])
def submit_incident():
    try:
        data = request.get_json()
        # Add your incident submission logic here
        
        return jsonify({
            'status': 'success',
            'message': 'Incident reported successfully'
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/stats')
def stats_page():
    # Read the CSV file
    df = pd.read_csv('tunis_safety_data.csv')
    
    # Convert Date_Time to datetime
    df['Date_Time'] = pd.to_datetime(df['Date_Time'])
    
    # Add weekend information
    df['is_weekend'] = df['Date_Time'].dt.day_name().isin(['Saturday', 'Sunday'])
    
    # Calculate statistics
    stats_data = {
        'total_incidents': len(df),
        
        # Weekend vs Weekday Distribution
        'weekend_data': [
            len(df[~df['is_weekend']]),  # Weekdays
            len(df[df['is_weekend']])    # Weekends
        ],
        
        # Public Transport Analysis
        'transport_available': len(df[df['Public_Transport'] == 1]),
        'transport_unavailable': len(df[df['Public_Transport'] == 0]),
    }
    
    return render_template('stats.html', **stats_data)

@app.route('/learn')
def learn_page():
    educational_content = {
        'videos': [
            {
                'title': 'Basic Self-Defense Techniques for Everyone',
                'url': 'https://www.youtube.com/embed/KVpxP3ZZtAc',
                'description': 'Learn fundamental self-defense moves that anyone can master.'
            },
            {
                'title': 'Simple Self Defense Moves',
                'url': 'https://www.youtube.com/embed/ORAOkP1h3R0',
                'description': 'Essential self-defense techniques that could save your life.'
            },
            {
                'title': 'Basic Self Defense Techniques',
                'url': 'https://www.youtube.com/embed/k9Jn0eP-ZVg',
                'description': 'Learn effective self-defense moves for personal safety.'
            },
            {
                'title': 'Self Defense Against Common Attacks',
                'url': 'https://www.youtube.com/embed/MF7reW-hkJE',
                'description': 'Practical defense techniques against common attack scenarios.'
            }
        ],
        'pdfs': [
            {
                'title': 'IASC Emergency Response',
                'filename': 'iasc_emergency_response_preparedness_guidelines_july_2015_rev_october_2016.pdf',
                'description': 'Comprehensive emergency response and preparedness guidelines.'
            },
            {
                'title': 'Personal Safety Guide',
                'filename': 'Personal_Safety_guide.pdf',
                'description': 'Essential guide for personal safety and security awareness.'
            }
        ]
    }
    return render_template('learn.html', **educational_content)

@app.route('/ask_question', methods=['POST'])
def ask_question():
    try:
        data = request.get_json()
        question = data.get('question')
        context = data.get('context')  # video title or PDF name

        # Format the prompt
        prompt = f"Context: Question about {context}\nQuestion: {question}\nPlease provide a helpful and safety-focused answer:"

        # Get response from OpenAI
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful safety and self-defense expert."},
                {"role": "user", "content": prompt}
            ]
        )

        return jsonify({
            'status': 'success',
            'answer': response.choices[0].message.content
        })

    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/downloads/<filename>')
def download_file(filename):
    # Using 'static/uploads' as the directory path
    return send_from_directory('static/uploads', filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)

