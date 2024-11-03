# Safety Education Hub - Tunis

A comprehensive web application built to enhance safety awareness and provide educational resources for residents and visitors in Tunis. The platform combines machine learning predictions, educational content, and data visualization to create a holistic safety resource.

## Core Features

### 1. Safety Prediction System
- District-based safety analysis
- Public transport availability consideration
- Real-time safety level predictions
- User-friendly interface for quick assessments

### 2. Educational Resources
- Curated self-defense training videos
- Downloadable safety guides
- Emergency response documentation
- Professional safety techniques

### 3. Statistics Dashboard
- Visual representation of safety data
- Transport availability analysis
- District-wise safety metrics
- Interactive data visualization

## Technologies Used

## Machine Learning : SafeHer: AI-Powered Safety Prediction Model 🛡️

https://colab.research.google.com/drive/1I9QMAUryYvViDGFVpLkeH02AdwKZeT2h?usp=sharing

## About The Model
SafeHer leverages advanced machine learning algorithms to predict safety risk levels in real-time, specifically designed to enhance women's safety in Tunisia's urban areas. Our model processes 20 distinct features, including environmental factors, temporal data, and community-reported incidents, to generate accurate safety risk assessments on a scale of 1-5.

## How It Works 🔍
The model combines multiple data points:
- **Location Intelligence**: Precise GPS coordinates and district-specific safety patterns
- **Environmental Factors**: Street lighting, police presence, and crowd density
- **Time-Based Analysis**: Hour of day, weekend/weekday patterns, and seasonal variations
- **Community Insights**: Active shops, public transport availability, and incident reports
- **Infrastructure Assessment**: Emergency services proximity and safety infrastructure

## Performance Metrics 📊
- **Accuracy**: 93% success rate in predicting risk levels
- **Real-Time Processing**: Instant risk assessment for immediate decision-making
- **Comprehensive Coverage**: Analyzes 20+ safety indicators

## Real-World Applications 🌍
From a quick safety check during a morning commute to comprehensive route planning for evening activities, SafeHer serves as a reliable companion for women navigating urban spaces. The model's predictions help users:
- Plan travel times strategically
- Stay informed about area-specific risks
- Make data-driven safety decisions

## Technical Innovation 💡
Built using state-of-the-art machine learning techniques, including Random Forest Classification and advanced feature engineering, SafeHer represents a breakthrough in predictive safety technology. Our model doesn't just predict risk – it empowers users with actionable safety intelligence.

> "Because every woman deserves to walk without fear, powered by data-driven confidence."



### Frontend
- HTML5/CSS3 for structure and styling
- JavaScript for interactive features
- Chart.js for data visualization
- Responsive design for mobile compatibility
- Font Awesome for icons

### Backend
- **Flask**: Python web framework
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Scikit-learn**: Machine learning implementation
- **PyPDF2**: PDF file handling
- **OpenAI**: Advanced text processing
- **Joblib**: Model persistence

### Data Storage
- CSV files for statistical data
- PDF documents for educational content
- Structured data organization

## Setup Instructions

1. Clone the repository
```bash
git clone [repository-url]
cd [project-directory]
```

2. Create and activate virtual environment
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Configure environment variables
```bash
cp .env.example .env
# Edit .env with your configurations
```

5. Run the application
```bash
python app.py
```

## Project Structure
```
safety-hub/
├── app.py                 # Main application file
├── requirements.txt       # Project dependencies
├── README.md             # Documentation
├── .env                  # Environment variables
├── static/
│   ├── uploads/          # PDF resources
│   │   ├── iasc_emergency_response.pdf
│   │   └── Personal_Safety_guide.pdf
│   ├── css/             # Stylesheets
│   └── js/              # JavaScript files
├── templates/            # HTML templates
│   ├── base.html        # Base template
│   ├── learn.html       # Educational content
│   ├── predict.html     # Safety prediction
│   ├── stats.html       # Statistics dashboard
│   └── submit.html      # Data submission
└── models/              # ML models
    └── safety_model.joblib
```

## API Endpoints

- `/` - Home page
- `/predict` - Safety prediction interface
- `/learn` - Educational resources
- `/stats` - Statistics dashboard
- `/submit` - Incident submission
- `/downloads/<filename>` - File downloads

## Development

### Prerequisites
- Python 3.8+
- pip package manager
- Virtual environment
- Web browser

## Security Features

- Input validation
- Secure file handling
- Protected API endpoints
- Error handling
- Data sanitization

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details



## Future Enhancements

- Mobile application :
