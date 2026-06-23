# 💊 MedInfo — Medication Information Translator

A Python desktop application that lets users look up medication information,
get AI-simplified summaries in plain English, and check for active drug recalls.

## Features

- Fetches real drug data from the openFDA API
- Simplifies complex medical text using Google Gemini AI
- Checks for active drug recall notices
- Saves search history locally
- Clean dark-themed GUI built with Tkinter

## Project Structure

medinfo/
├── .env
├── main.py
├── gui.py
├── models/
│   └── medication.py
├── services/
│   ├── fda_client.py
│   ├── recall_checker.py
│   └── ai_translator.py
├── storage/
│   └── history.py
├── utils/
│   └── validators.py
└── data/
    └── (history.json is auto-generated here on first search)

## Setup

1. Clone the repository
2. Install dependencies:
   pip install -r requirements.txt

3. Create a .env file in the root directory and add your Gemini API key:
   GEMINI_API_KEY="your-api-key-here"

   Get a free API key at: https://aistudio.google.com

## Running the App

GUI version:
   python gui.py

Terminal version:
   python main.py

## APIs Used

- openFDA Drug Label API — https://api.fda.gov/drug/label.json
- openFDA Drug Enforcement API — https://api.fda.gov/drug/enforcement.json
- Google Gemini AI — https://aistudio.google.com
