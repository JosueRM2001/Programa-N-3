from flask import Flask, render_template_string

app = Flask(__name__)

# Main page
@app.route('/')
def hello_world():
    return render_template_string('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Flask Web Page</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    transition: background-color 0.5s;
                }
                .container {
                    text-align: center;
                    margin-top: 100px;
                }
                button {
                    padding: 10px 20px;
                    font-size: 16px;
                    cursor: pointer;
                }
            </style>
        </head>
        <body id="body">
            <div class="container">
                <h1>This is a simple webpage created with Python and Flask</h1>
                <button onclick="changeColor()">Change Color</button>
            </div>
            
            <script>
                // Function to change the background color
                function changeColor() {
                    const colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#FF8C00'];
                    const randomColor = colors[Math.floor(Math.random() * colors.length)];
                    document.getElementById('body').style.backgroundColor = randomColor;
                }
            </script>
        </body>
        </html>
    ''')

if __name__ == '__main__':
    # Make the Flask server listen on all interfaces
    app.run(host='0.0.0.0', port=5000)

 
