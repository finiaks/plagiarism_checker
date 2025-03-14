import os
from flask import Blueprint, request, jsonify
from app.file_handler import extract_text
from app.text_processing import preprocess_text
from app.plagiarism_check import check_plagiarism
from app.database import session, PlagiarismCheck

main = Blueprint("main", __name__)

@main.route("/api/upload", methods=["POST"])
def upload_file():
    file = request.files["file"]
    reference_file = request.files["reference_file"]

    if file and reference_file:
        file_path = os.path.join("uploads", file.filename)
        ref_path = os.path.join("uploads", reference_file.filename)

        file.save(file_path)
        reference_file.save(ref_path)

        text1 = preprocess_text(extract_text(file_path, file.filename.split(".")[-1]))
        text2 = preprocess_text(extract_text(ref_path, reference_file.filename.split(".")[-1]))

        similarity_score = check_plagiarism(text1, text2)
        result = "Plagiarized" if similarity_score > 0.5 else "Unique"

        new_entry = PlagiarismCheck(file_name=file.filename, similarity_score=similarity_score, result=result)
        session.add(new_entry)
        session.commit()

        return jsonify({"filename": file.filename, "score": round(similarity_score * 100, 2), "result": result})

    return jsonify({"error": "Files missing"}), 400
