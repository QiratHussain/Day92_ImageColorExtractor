from flask import Flask, render_template, request
import colorgram


def check_colors(image):
    colors_list=[]
    colors = colorgram.extract(image, 6)
    for color in colors:
        rgb = color.rgb
        proportion = color.proportion 
        hex_color = f"#{rgb.r:02x}{rgb.g:02x}{rgb.b:02x}" 
        colors_list.append(f"HEX: {hex_color} | RGB: ({rgb.r}, {rgb.g}, {rgb.b}) | Occurrence: {proportion:.2%}")
    return colors_list

app= Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    image = request.files["image"]
    extracted= check_colors(image.stream)
    return render_template("index.html", colors_data= extracted )


if __name__=="__main__":
    app.run(debug=True)

