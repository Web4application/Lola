npm install -g vercel
https://github.com/Web4application/script_analyzer_bot.git
python3 -m venv venv
source venv/bin/activate  # Use venv\Scripts\activate on Windows
pip install -r requirements.txt

cd backend
pip install fastapi uvicorn
touch main.py

npx create-next-app@latest [lola-ai] [https://nextjs-boilerplate-web4application.vercel.app]
