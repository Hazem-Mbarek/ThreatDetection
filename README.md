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

### Code Style
- Follow PEP 8 guidelines
- Use meaningful variable names
- Comment complex logic
- Keep functions focused and small

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

## Contact

Project Link: [repository-url]

## Future Enhancements

- Mobile application
- Real-time alerts
- Community features
- Advanced analytics
- Multi-language support