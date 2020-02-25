import random
import numpy as np
import cv2
from flask import Flask, request, jsonify


# from server.data import dataset
# import sys
# import os

# # Workaround to make packages work in both Jupyter notebook and Python
# module_root_name = "AgeEstimator"
# module_paths = [
#     os.path.abspath(os.path.join('..')),
#     os.path.abspath(os.path.join('../..'))
# ]
# module_paths = list(
#     filter(lambda x: x.endswith(module_root_name), module_paths))
# module_path = module_paths[0] if len(module_paths) == 1 else ""
# if module_path not in sys.path:
#     sys.path.append(module_path)


app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024


@app.route('/api/predict_age', methods=['POST'])
def predict_age():
    try:
        file = request.files['file']
        file_name = file.filename
        print(file.filename)
        nparr = np.fromstring(file.read(), np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        # TODO call the model / resize

        message = "Succeed!"
        age_cnn = random.randint(20, 60)
        age_regression = random.randint(34, 48)
        age_cluster = random.randint(2, 80)
        ages = {
            "cnn": age_cnn,
            "regression": age_regression,
            "clustering": age_cluster,
        }
    except Exception:
        message = "Invalid format"
        ages = None

    return jsonify({
        "name": file_name,
        "message": message,
        "ages": ages,
    })


app.run(port=5000, debug=True)
