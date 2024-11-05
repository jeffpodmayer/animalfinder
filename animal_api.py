import tkinter as tk
import requests

# API endpoint and key
API_URL = 'https://api.api-ninjas.com/v1/animals'
API_KEY = "Vfm52mnwlUBEhhMCnii+Ow==kwlqFtMnriD4YDkj"

# Function to get animal data from the API
def get_animal_data(animal_name):
    headers = {
        "X-Api-Key": API_KEY
    }
    # Send request to get specific animal information
    response = requests.get(f"{API_URL}?name={animal_name}", headers=headers)
    if response.status_code == 200:
        return response.json()
    return None

# Function to display animal information
def show_animal_info(animal_name):
    animal_data = get_animal_data(animal_name)
    if animal_data and len(animal_data) > 0:
        animal_info = animal_data[0]  # Get the first animal info from the list

        # Extracting taxonomy information
        taxonomy = animal_info.get('taxonomy', {})
        characteristics = animal_info.get('characteristics', {})

        # Building the information text
        info_text = f"Name: {characteristics.get('common_name', animal_name)}\n"
        info_text += f"Scientific Name: {taxonomy.get('scientific_name', 'Not available')}\n"
        info_text += f"Habitat: {characteristics.get('habitat', 'Not available')}\n"
        info_text += f"Diet: {characteristics.get('diet', 'Not available')}\n"
        info_text += f"Description: {characteristics.get('slogan', 'Not available')}\n"
        info_text += f"Top Speed: {characteristics.get('top_speed', 'Not available')}\n"
        info_text += f"Lifespan: {characteristics.get('lifespan', 'Not available')}\n"
    else:
        info_text = "Error fetching data."

    info_label.config(text=info_text)


# Create the main application window
app = tk.Tk()
app.title("Animal Finder")

# Label to display animal information
info_label = tk.Label(app, text="Welcome to Animal Finder!", font=("Arial", 14))
info_label.pack(pady=20)

# Create a frame for buttons
button_frame = tk.Frame(app)
button_frame.pack(pady=20)

# Create buttons for animal emojis
animal_emojis = {
    "🐶": "Dog",
    "🐱": "Cat",
    "🐰": "Rabbit",
    "🐸": "Frog",
    "🦁": "Lion",
    "🐨": "Koala",
    "🐵": "Monkey",
    "🐆": "Cheetah",
    "🐅": "Tiger",
    "🐻": "Bear",
    "🐘": "Elephant",
    "🐴": "Horse",
    "🐼": "Panda",
    "🦌": "Deer",
    "🦔": "Hedgehog"
}

# Create a button for each animal emoji
for emoji, name in animal_emojis.items():
    button = tk.Button(button_frame, text=emoji, font=("Arial", 30),
                       command=lambda n=name: show_animal_info(n))
    button.pack(side=tk.LEFT, padx=5)

# Start the application
app.mainloop()



