from flask import Flask, render_template, request
import face_recognition
import os

# Création de l'application web Flask
app = Flask(__name__)

# Route pour la page d'accueil
@app.route('/', methods = ['GET', 'POST'])   # par défaut c'est GET (on peut avoir aussi 'PUT')

def index():
    return render_template('compare.html')


# Route pour la page d'accueil => Comparer avec une deuxième image
@app.route('/compare', methods = ['GET', 'POST'])   # par défaut c'est GET (on peut avoir aussi 'PUT')

#def compare():
   # return render_template('compare.html')


# Récupération de l'image 1 et enregistrement
@app.route('/image1', methods = ['POST'])   # par défaut c'est GET (on peut avoir aussi 'PUT')
def image1():

    #Suppresion de l'ancienne image
    if os.path.exists('image_viz.jpg'):
        os.remove('image_viz.jpg')

    image = request.files['image_viz']
    image.save('image_viz.jpg')
    return "Enregistrée avec succès!"


# Récupération de l'image 2 et enregistrement
@app.route('/image2', methods = ['GET', 'POST'])   
def image2():
    image = request.files['image_viz2']
    image.save('image_viz2.jpg')
    return "Enregistrée avec succès aussi!"


# On crée une nouvelle route: prédiction de l'image 2 par rapport à l'image 1
@app.route('/predict', methods=['GET', 'POST'])
def predict():

    #Suppresion de l'ancienne image
    if os.path.exists('image_viz.jpg'):
        os.remove('image_viz.jpg')

    image = request.files['image_viz']
    image.save('image_viz.jpg')

    if os.path.exists('image_viz2.jpg'):
        os.remove('image_viz2.jpg')
    image = request.files['image_viz2']
    image.save('image_viz2.jpg')

    known_image = face_recognition.load_image_file('image_viz.jpg')
    unknown_image = face_recognition.load_image_file('image_viz2.jpg')
    biden_encoding = face_recognition.face_encodings(known_image)[0]
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
    results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
    #print(str(results))
    return str(results)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
