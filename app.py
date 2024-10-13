"""
Install the Google AI Python SDK

python -m venv myenv
source myenv/bin/activate  # On Windows, use `myenv\Scripts\activate`
pip install google-generativeai
"""

from flask import Flask, render_template, request
import os
import google.generativeai as genai

genai.configure(api_key="AIzaSyBWO162C2niYP9V3mMQoDiryWrI3RHoAIo")
# genai.configure(api_key="AIzaSyByJuzCNV4EBW8YMvR9nzwSzeegSYbpV1A")


# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  # "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

def create_model():
  """
  Creates and returns the generative model object.
  """
  model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    # model_name="tunedModels/recipe-distillation-examples-fmsne0yp0au",
    generation_config=generation_config,
  )
  return model.start_chat(history=[])

app = Flask(__name__)
model = None  

@app.route("/", methods=["GET", "POST"])
def index():
  global model
  if model is None:
    model = create_model()

  if request.method == "POST":
    user_query = request.form["query"]
    response = model.send_message(user_query)
    workout_plan = response.text
  else:
    workout_plan = ""

  return render_template("index.html", workout_plan=workout_plan)

# def index():
#   global model
#   if model is None:
#     model = create_model()

#   if request.method == "POST":
#     user_query = request.form["query"]
#     print(f"User Query: {user_query}")
#     # Example query: Give me a recipe for [dish name]
#     response = model.send_message(user_query)
#     print(f"Response: {response}" )
#     recipe = response.text
#   else:
#     recipe = ""

#   return render_template("index.html", workout_plan=recipe)

if __name__ == "__main__":
  app.run(debug=True)



# def index():
#   global model
#   if model is None:
#     model = create_model()

#   if request.method == "POST":
#     user_query = request.form["query"]
#     response = model.send_message(user_query)
#     workout_plan = response.text
#   else:
#     workout_plan = ""

#   return render_template("index.html", workout_plan=workout_plan)

# Tables, formats, agenda