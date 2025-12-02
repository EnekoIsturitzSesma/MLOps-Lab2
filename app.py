import gradio as gr
import requests

API_URL = "https://firstcontainer-latest.onrender.com/predict"

def obtain_pred():
    try:
        response = requests.get(API_URL, timeout=10)
        if response.status_code == 200:
            data = response.json()
            return f"Predicted label: {data.get('label', 'No label field found')}"
        else:
            return f"Error: API returned status {response.status_code}"
    except Exception as e:
        return f"Error contacting API: {e}"

demo = gr.Interface(
    fn=obtain_pred,
    inputs=[],
    outputs="text",
    title="Random Prediction Demo",
    description="This app calls the API hosted on Render to obtain a random prediction."
)

if __name__ == "__main__":
    demo.launch()
