from flask import Flask, request, render_template, send_file, jsonify
from ultralytics import YOLO
from PIL import Image
import os
import uuid

# Initialiser l'application Flask
app = Flask(__name__)

# Charger le modèle YOLO
model = YOLO("yolov5_trained_model.pt")

# Dossier temporaire pour stocker les images
UPLOAD_FOLDER = "temp_images"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "file" not in request.files:
            return jsonify({"error": "Erreur : Aucun fichier envoyé."}), 400
        
        file = request.files["file"]
        if file.filename == "":
            return jsonify({"error": "Erreur : Aucun fichier sélectionné."}), 400

        try:
            # Convertir l'image en RGB
            img = Image.open(file.stream).convert("RGB")

            # Générer un nom de fichier unique
            unique_id = str(uuid.uuid4())
            temp_file_path = os.path.join(UPLOAD_FOLDER, f"{unique_id}_uploaded.jpg")
            result_file_path = os.path.join(UPLOAD_FOLDER, f"{unique_id}_result.jpg")
            img.save(temp_file_path)

            # Faire une prédiction avec YOLO
            results = model.predict(source=temp_file_path, save=False, imgsz=640)

            # Vérifier les détections
            if not results[0].boxes:
                return jsonify({"message": "Aucune détection trouvée dans l'image. Veuillez essayer une autre image."}), 200

            # Générer l'image avec les prédictions
            output_image = results[0].plot()
            Image.fromarray(output_image).save(result_file_path)

            # Retourner l'image résultante
            return send_file(result_file_path, mimetype="image/jpeg")

        except Exception as e:
            return jsonify({"error": f"Erreur lors du traitement de l'image : {str(e)}"}), 500

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
