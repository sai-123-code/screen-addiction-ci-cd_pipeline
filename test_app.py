import pytest
from app import app
import json


@pytest.fixture
def client():
    return app.test_client()


def test_home_page_loads(client):
    """Test GET request to home page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Smartphone Addiction Level Predictor" in response.data

def test_valid_post_request(client):
    """Test POST request with valid input"""
    data = {
        'Age': 17,
        'Gender': 'Female',
        'Daily_Usage_Hours': 7,
        'Sleep_Hours': 6,
        'Academic_Performance': 85,
        'Social_Interactions': 6,
        'Exercise_Hours': 2,
        'Anxiety_Level': 3,
        'Depression_Level': 2,
        'Self_Esteem': 4,
        'Parental_Control': 1,
        'Screen_Time_Before_Bed': 1,
        'Phone_Checks_Per_Day': 80,
        'Apps_Used_Daily': 12,
        'Time_on_Social_Media': 3,
        'Time_on_Gaming': 2,
        'Time_on_Education': 2,
        'Phone_Usage_Purpose': 'Social Media',
        'Family_Communication': 8,
        'Weekend_Usage_Hours': 10
    }
    response = client.post("/", data=data)
    assert response.status_code == 200
    assert b"Predicted Addiction Level" in response.data

def test_missing_required_field(client):
    """Missing field should trigger error"""
    data = {
        'Age': 17,
        'Gender': 'Female',
        # Missing 'Daily_Usage_Hours'
        'Sleep_Hours': 6,
        'Academic_Performance': 85,
        'Social_Interactions': 6,
        'Exercise_Hours': 2,
        'Anxiety_Level': 3,
        'Depression_Level': 2,
        'Self_Esteem': 4,
        'Parental_Control': 1,
        'Screen_Time_Before_Bed': 1,
        'Phone_Checks_Per_Day': 80,
        'Apps_Used_Daily': 12,
        'Time_on_Social_Media': 3,
        'Time_on_Gaming': 2,
        'Time_on_Education': 2,
        'Phone_Usage_Purpose': 'Social Media',
        'Family_Communication': 8,
        'Weekend_Usage_Hours': 10
    }
    response = client.post("/", data=data)
    assert b"Error" in response.data or b"Bad Request" in response.data
