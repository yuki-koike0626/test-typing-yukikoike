
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
            body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }
            #word { font-size: 24px; margin: 20px; }
            #input { font-size: 18px; padding: 5px; }
            #score { margin: 20px; }
            #speed { margin: 20px; }
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
