from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Generate a random number
random_number = random.randint(1, 100)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/guess", methods=["POST"])
def guess():
    global random_number
    user_guess = int(request.json.get("guess"))
    
    if user_guess < random_number:
        return jsonify({"message": "Higher!"})
    elif user_guess > random_number:
        return jsonify({"message": "Lower!"})
    else:
        random_number = random.randint(1, 100)  # Reset game
        return jsonify({
            "message": "🎉 Well Done, You got it correct!"
        })
    
if __name__ == "__main__":
    app.run()