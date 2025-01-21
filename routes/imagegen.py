from flask import Blueprint, jsonify, request, render_template
from flask_login import login_required
import requests
import logging

imagegen_bp = Blueprint('imagegen', __name__)

def get_models_refiners_samplers():
    try:
        models_response = requests.get("http://127.0.0.1:7860/sdapi/v1/sd-models")
        models_response.raise_for_status()
        models = models_response.json()

        # Assuming refiners are a subset of models with 'refiner' in their title
        refiners = [model for model in models if 'refiner' in model['title']]

        samplers_response = requests.get("http://127.0.0.1:7860/sdapi/v1/samplers")
        samplers_response.raise_for_status()
        samplers = samplers_response.json()

        return models, refiners, samplers
    except requests.exceptions.RequestException as e:
        logging.error(f"Error retrieving models, refiners, and samplers: {e}")
        return [], [], []

@imagegen_bp.route('/imagegen', methods=['GET'])
@login_required
def imagegen_page():
    models, refiners, samplers = get_models_refiners_samplers()
    return render_template('imagegen.html', models=models, refiners=refiners, samplers=samplers)

@imagegen_bp.route('/generate-image', methods=['POST'])
@login_required
def generate_image():
    try:
        prompt = request.form.get('prompt')
        negative_prompt = request.form.get('negative_prompt', '')
        sampler_name = request.form.get('sampler_name', 'Euler a')
        steps = int(request.form.get('steps', 20))
        cfg_scale = int(request.form.get('cfg_scale', 7))
        width = int(request.form.get('width', 512))
        height = int(request.form.get('height', 512))
        restore_faces = request.form.get('restore_faces') == 'on'
        tiling = request.form.get('tiling') == 'on'
        url = "http://127.0.0.1:7860/sdapi/v1/txt2img"

        payload = {
            "prompt": prompt,
            "negative_prompt": negative_prompt,
            "sampler_name": sampler_name,
            "steps": steps,
            "cfg_scale": cfg_scale,
            "width": width,
            "height": height,
            "restore_faces": restore_faces,
            "tiling": tiling
        }

        logging.info(f"Sending payload to Stable Diffusion: {payload}")

        response = requests.post(url, json=payload)
        response.raise_for_status()
        result = response.json()
        image_data = result['images'][0]  # Base64 encoded image
        return jsonify({"image": image_data})
    except requests.exceptions.ConnectionError:
        logging.error("Stable Diffusion WebUI is not running or not accessible.")
        return jsonify({"error": "Stable Diffusion WebUI is not running or not accessible. Please ensure it is running and try again."}), 500
    except requests.exceptions.RequestException as e:
        logging.error(f"Error querying image generation API: {e}")
        return jsonify({"error": "Image generation failed. Please try again later."}), 500
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return jsonify({"error": "An unexpected error occurred. Please try again later."}), 500
