# chatbot-faq
Web app where the user asks questions and the chatbot responds like a simple AI. Ideal for FAQs from a fictional company.  
Basic logic in Pytho, simulating an AI-like model using dictionaries, the project is running locally (not dockerized)  
to facilitate the design.  

It uses following technologies:    

✅ Flask App for backend  
✅ React (Vite) for frontend  

__________________________________________________________________________________________________

📂 Project Structure    

chatbot-faq/       # Root directory   
├── backend/  
│   └── venv       # Recommended to avoid conflicts  
│   └── app.py     # Flask app  
│   └── Dockerfile (optional)  
├── frontend/  
│   ├── vite.config.js  
│   └── src/  
│       ├── App.jsx   # Renderization  
│       └── main.jsx  
│   └── Dockerfile (optional)  
├── package.json (auto generated by Vite)  
├── docker-compose.yml (optional)  
 
___________________________________________________________________________________________________

🚀 Development Step by Step    

Step 1️⃣: Configuring Development Environmen  t  
Before installing Flask, ensure Python and pip are up to date (Terminal Linux):     
sudo apt update && sudo apt upgrade -y    
sudo apt install python3 python3-pip -y    

Step 2️⃣: Create directories in your Project folder  
cd Projects  
mkdir chatbot-faq/backend  

Open VS Code (or other) and navigate to your Project directory:  
code .  

Step 3️⃣: Create app.py  (/backend)   

Step 4️⃣: Create Virtual Environment (recommended)   
Using a virtual environment helps avoid conflicts between dependencies:    

cd backend  
python3 -m venv venv       # For Linux/Mac    
source venv/bin/activate   # For Linux/Mac     
venv\Scripts\activate      # For Windows   

==> Inside the virtual environment (Linux), install Flask:   
pip install Flask     

Step 5️⃣:  Create a project React (Vite) for the frontend  
cd ..  
npm create vite@latest frontend --template react  

Choose a Framework and a Variant (e.g React and JavaScript) an install NPM (Node Package Manager):  
cd frontend  
npm install  

Step 6️⃣:  Add following Proxy to the default vite.config.js   
export default {  
...server: {  
....proxy: {  
......'/chat': 'http://localhost:5001'  
.....}  
...}  
}  

Step 7️⃣:  Edit the App.jsx  

Step 8️⃣:  Run the app  
In Terminal #1: Activate Virtual Environment  
cd backend  
source venv/bin/activate   # ✅ Linux / WSL  

==> Install Flask inside the venv (Only for the first time)  
pip install flask flask-cors  

==> Run the backend with Flask  
python3 app.py  

Step 9️⃣:  Run the development server on JavaScript/Node.js (with frameworks React, Vite).    
In Terminal #2:   
cd frontend  
npm run dev  

Step 9️⃣:  Open the browser with http://localhost:5173 and try some questions (please see dictionaries on app.py)  

🔹 Summary    
✅ Flask is used to build the web application (the logic in the backend).    
✅ React is the engine of your frontend UI, the main tool used to build the user interface (UI) of the web application.  
✅ Vite is the environment you develop in — fast, modern, and super smooth.  
✅ Virtual environment keeps dependencies organized.

📜 License  
MIT License — use freely, with attribution. Contributions welcome!  
Created by geeky4dev – feel free to fork, contribute, or star 🌟 the project!  
