# Weather CLI

A command-line weather application built with Python that retrieves current weather information using the OpenWeatherMap API.

## Features

* Enter a city name
* Find the city's latitude and longitude
* Get current weather information
* Display:

  * Temperature
  * Humidity
  * Wind speed
  * Weather description
  * City name
  * Latitude and longitude
* Handles invalid city names
* Handles API request errors
* Keeps the API key secure using environment variables

## Technologies Used

* Python
* Requests
* OpenWeatherMap API
* python-dotenv
* Git & GitHub

## What I Learned

This project helped me practice:

* Working with REST APIs
* Understanding HTTP requests and responses
* Using the `requests` library
* Working with JSON data
* Accessing nested JSON data
* Using API endpoints
* Handling API errors with `try/except`
* Using environment variables
* Protecting API keys with `.env`
* Using `.gitignore`
* Managing dependencies with `requirements.txt`
* Using Git and GitHub

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/subayr-apdi/weather-cli.git
cd weather-cli
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create a `.env` file

Create a file named `.env` in the project folder:

```text
api=YOUR_OPENWEATHERMAP_API_KEY
```

Replace `YOUR_OPENWEATHERMAP_API_KEY` with your own API key.

### 4. Run the application

```bash
python weather.py
```

Enter a city name when prompted.

## Security

The API key is stored in `.env` and `.env` is included in `.gitignore`, so the API key is not uploaded to GitHub.

## Project Purpose

This project is part of my journey toward becoming a Data Engineer. I built it to strengthen my Python skills and learn how real applications communicate with external APIs.
