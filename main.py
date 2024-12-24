
from flask import Flask, render_template_string, request, jsonify
import random
import time

app = Flask(__name__)

words = [
    "python", "programming", "keyboard", "computer", "algorithm",
    "developer", "typing", "practice", "software", "coding"
]

def get_random_word():
    return random.choice(words)

@app.route('/')
def home():
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>タイピングゲーム</title>
        <style>
            @keyframes gradient {
                0% { background-position: 0% 50%; }
                50% { background-position: 100% 50%; }
                100% { background-position: 0% 50%; }
            }
            body { 
                font-family: Arial, sans-serif; 
                text-align: center; 
                margin: 0; 
                padding-top: 50px; 
                min-height: 100vh;
                background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
                background-size: 400% 400%;
                animation: gradient 15s ease infinite;
                color: white;
            }
            #word { 
                font-size: 32px; 
                margin: 20px;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
            }
            #input { 
                font-size: 18px; 
                padding: 10px;
                border: none;
                border-radius: 5px;
                width: 300px;
                margin: 20px;
            }
            #score, #speed { 
                margin: 20px;
                font-size: 20px;
                text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
            }
            h1 {
                color: white;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
            }
        </style>
    </head>
    <body>
        <h1>タイピングゲーム</h1>
        <div id="word"></div>
        <input type="text" id="input" placeholder="ここにタイプしてください">
        <div id="score">スコア: 0</div>
        <div id="speed"></div>

        <script>
            let score = 0;
            let startTime;

            function getNewWord() {
                fetch('/word')
                    .then(response => response.json())
                    .then(data => {
                        document.getElementById('word').textContent = data.word;
                        startTime = new Date();
                    });
            }

            document.getElementById('input').addEventListener('keypress', function(e) {
                if (e.key === 'Enter') {
                    const input = this.value;
                    const word = document.getElementById('word').textContent;
                    const endTime = new Date();
                    const timeElapsed = (endTime - startTime) / 1000;
                    
                    if (input === word) {
                        score++;
                        const wpm = (word.length / 5) / (timeElapsed / 60);
                        document.getElementById('speed').textContent = `タイピング速度: ${wpm.toFixed(1)} WPM`;
                    }
                    
                    document.getElementById('score').textContent = `スコア: ${score}`;
                    this.value = '';
                    getNewWord();
                }
            });

            getNewWord();
        </script>
    </body>
    </html>
    '''
    return render_template_string(html)

@app.route('/word')
def new_word():
    return jsonify({'word': get_random_word()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
