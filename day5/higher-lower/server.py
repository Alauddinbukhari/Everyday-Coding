from flask import Flask
import random 
app=Flask(__name__)

random_num= random.randint(0,9)
print(random_num)

@app.route("/")
def home():
    return '<h1>Guess a number between 0 and 9</h1>'\
            '<div style="width:100%;height:0;padding-bottom:80%;position:relative;"><iframe src="https://giphy.com/embed/5VKbvrjxpVJCM" width="100%" height="100%" style="position:absolute" frameBorder="0" class="giphy-embed" allowFullScreen></iframe></div><p><a href="https://giphy.com/gifs/5VKbvrjxpVJCM">via GIPHY</a></p>'

@app.route("/<int:number>")
def number_checker(number):
    value=""
    if number==random_num:
       value="somevalue"\
        '<iframe src="https://giphy.com/embed/vKHKDIdvxvN7vTAEOM" width="480" height="398" style="" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/theoffice-the-office-tv-episode-818-vKHKDIdvxvN7vTAEOM">via GIPHY</a></p>'

    elif number>random_num:
       value= "too high"

    elif number<=random_num:
        value="too low"
    
    return value


if __name__ =="__main__":
    app.run(debug=True)