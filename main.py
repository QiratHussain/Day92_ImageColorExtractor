from flask import Flask, render_template

app= Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)

# TODO: 3. image upload function 
# TODO: 4. show the uploaded image
# TODO: 5. extract the colors of images
# TODO: 6. display the colors (or colors and hex codes)
