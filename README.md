# 🎯 Quiz Game

An interactive quiz application built with Streamlit that tests your knowledge across multiple categories.

## 📚 Categories

- 🌍 **Capitals** - Test your geography knowledge
- 👑 **Presidents** - Learn about world leaders
- 💰 **Currencies** - Know your money
- 📜 **History** - Journey through time

## ✨ Features

- Multiple choice questions
- Real-time score tracking
- Progress bar
- Instant feedback on answers
- Performance evaluation
- Category selection
- Restart functionality

## 🚀 Live Demo

[Try it here!](#) *(Coming soon - Streamlit deployment)*

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/kanouar926-prog/quiz-game.git
cd quiz-game
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the app:
```bash
streamlit run quiz_app.py
```

## 📁 Project Structure
```
quiz-game/
├── quiz_app.py          
├── questions.json       
├── requirements.txt     
└── README.md           

## 🎮 How to Play

1. Choose a category
2. Answer multiple-choice questions
3. Submit your answer to see if you're correct
4. View your final score and performance rating
5. Restart or try a different category!

## 🧩 Technologies Used

- Python 3.x
- Streamlit
- JSON

## 📝 Adding More Questions

Edit `questions.json` to add more questions in this format:
```json
{
  "category_name": [
    {
      "question": "Your question?",
      "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
      "answer": "Correct Option"
    }
  ]
}
```

## 👨‍💻 Author

Khchichine Mohamed Anouar - [GitHub Profile](https://github.com/kanouar926-prog)




# Virtual environment
venv/
env/

# Python cache
__pycache__/
*.py[cod]
*$py.class

# Streamlit cache
.streamlit/

# OS files
.DS_Store
Thumbs.db

# IDE
.vscode/
.idea/
*.swp
