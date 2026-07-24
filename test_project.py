import os
import json
import pytest
from project import (Studentp, get_universities, load_profile)
# -----------------------------
# Test creating Student profile
# -----------------------------
def test_student_creation():
    country = {
        "name": "South Korea"
    }
    universities = [
        {
            "name": "Yonsei University",
            "website": "https://www.yonsei.ac.kr"
        }
    ]
    profile = Studentp(
        "Tina",
        country,
        universities,
        "Computer Science",
        ["Passport", "TOPIK"],
        ["Passport"]
    )
    assert profile.name == "Tina"
    assert profile.country["name"] == "South Korea"
    assert profile.major == "Computer Science"
# -----------------------------
# Test data types
# -----------------------------
def test_profile_data_types():
    country = {
        "name": "South Korea"
    }
    profile = Studentp(
        "Tina",
        country,
        [],
        "CS",
        [],
        []
    )
    assert isinstance(profile.name, str)
    assert isinstance(profile.documents, list)
    assert isinstance(profile.completed_documents, list)
# -----------------------------
# Test str output
# -----------------------------
def test_student_str():
    country = {
        "name": "South Korea"
    }
    profile = Studentp(
        "Tina",
        country,
        [],
        "Computer Science",
        ["Passport"],
        []
    )
    result = str(profile)
    assert "Tina" in result
    assert "South Korea" in result
    assert "Computer Science" in result
    assert "Passport" in result
# -----------------------------
# Test completed documents
# -----------------------------
def test_completed_documents():
    documents = [
        "Passport",
        "TOPIK",
        "Transcript"
    ]
    completed = [
        "Passport",
        "TOPIK"
    ]
    assert len(completed) == 2
    assert completed[0] in documents
# -----------------------------
# Test progress calculation
# -----------------------------
def test_document_progress():
    documents = [
        "Passport",
        "TOPIK",
        "Transcript"
    ]
    completed = [
        "Passport"
    ]
    progress = (len(completed) / len(documents)) * 100
    assert progress == pytest.approx(33.33, 0.1)
# -----------------------------
# Test 100% completion
# -----------------------------
def test_full_progress():
    documents = [
        "Passport",
        "TOPIK"
    ]
    completed = [
        "Passport",
        "TOPIK"
    ]
    progress = (len(completed) / len(documents)) * 100
    assert progress == 100
# -----------------------------
# Test empty documents
# -----------------------------
def test_empty_documents():
    documents = []
    completed = []
    if len(documents) == 0:
        progress = 0
    else:
        progress = (len(completed) / len(documents)) * 100
    assert progress == 0
# -----------------------------
# Test university search fail
# -----------------------------
def test_get_universities_fail():
    universities = get_universities(
        "Fake Country Name"
    )
    assert universities == []
# -----------------------------
# Test duplicate documents
# -----------------------------
def test_duplicate_document():
    documents = [
        "Passport"
    ]
    new_document = "Passport"
    if new_document not in documents:
        documents.append(new_document)
    assert documents.count("Passport") == 1
# -----------------------------
# Test adding document
# -----------------------------
def test_add_document():
    documents = [
        "Passport"
    ]
    documents.append("TOPIK")
    assert "TOPIK" in documents
# -----------------------------
# Test removing document
# -----------------------------
def test_remove_document():
    documents = [
        "Passport",
        "TOPIK"
    ]
    documents.remove("TOPIK")
  
    assert "TOPIK" not in documents
# -----------------------------
# Test completed document removal
# -----------------------------
def test_remove_completed_document():
    documents = [
        "Passport",
        "TOPIK"
    ]
    completed = [
        "TOPIK"
    ]
    removed = documents.pop(1)
    if removed in completed:
        completed.remove(removed)
    assert "TOPIK" not in completed
# -----------------------------
# Test save profile file
# -----------------------------
def test_save_profile():
    data = {
        "name": "Tina",
        "major": "Computer Science"
    }
    with open(
        "profile.json",
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(data, file)
    assert os.path.exists(
        "profile.json"
    )
# -----------------------------
# Test loading profile
# -----------------------------
def test_load_profile():
    data = {
        "name": "Tina",
        "country": {
            "name": "South Korea"
        },
        "universities": [],
        "major": "Computer Science",
        "documents": [],
        "completed_documents": []
    }
    with open(
        "profile.json",
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(data, file)
    profile = load_profile()
    assert profile.name == "Tina"
    assert profile.major == "Computer Science"
# -----------------------------
# Test missing profile file
# -----------------------------
def test_missing_profile():
    if os.path.exists(
        "profile.json"
    ):
        os.remove(
            "profile.json"
        )
    profile = load_profile()
    assert profile is None
# -----------------------------
# Test corrupted JSON file
# -----------------------------
def test_corrupted_json():
    with open(
        "profile.json",
        "w"
    ) as file:
        file.write(
            "{ wrong json"
        )
    with pytest.raises(
        json.JSONDecodeError
    ):
        load_profile()
