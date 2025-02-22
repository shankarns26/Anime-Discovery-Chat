# Anime Discovery Chat 🎭

An interactive web application that helps users explore and discover anime through natural conversations. 
Using a modern, intuitive interface, users can browse anime by genres or search for specific titles to get detailed information. 
The application leverages the Jikan API to provide real-time access to MyAnimeList's extensive database of anime content.
Built with Flask and modern web technologies, it offers a seamless and engaging experience for both casual viewers and anime enthusiasts.

## ✨ Key Features

- 🤖 Interactive chatbot interface for natural conversations
- 🎯 Smart anime recommendations based on genres and preferences
- 📚 Detailed information about anime titles including synopsis and visuals
- 🎨 Clean, modern UI design for seamless user experience
- 🔄 Real-time data from MyAnimeList through Jikan API

## 🔬 Technical Overview

The project implements a conversational interface paradigm, combining natural language processing with a structured API integration to create an intuitive anime discovery system.
The architecture follows a client-server model where Flask handles backend requests, while the frontend employs modern JavaScript for asynchronous communication and dynamic content updates.
By utilizing the Jikan API's RESTful endpoints, the application maintains real-time data accuracy without the overhead of managing a local database, while the responsive UI ensures cross-device compatibility.

## Setup and Installation

1. Install Python 3.7 or higher if you haven't already
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
3. Run the application:
   ```
   python app.py
   ```
4. Open your web browser and go to `http://localhost:5000`

## How to Use

1. Start by greeting the chatbot (say "hi" or "hello")
2. When asked about genre, type any of the following genres:
   - Action
   - Adventure
   - Comedy
   - Drama
   - Fantasy
   - Horror
   - Mystery
   - Romance
   - Sci-Fi
   - Slice of Life
   - Sports
   - Supernatural

3. To get information about a specific anime, type:
   "Tell me about [anime name]"

## Technologies Used

- Flask (Python web framework)
- Jikan API (MyAnimeList unofficial API)
- HTML/CSS
- JavaScript
