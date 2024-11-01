import tkinter as tk
import requests

# Create the main application window
app = tk.Tk()
app.title("Animal Finder")

# Label to display animal information
info_label = tk.Label(app, text="Welcome to Animal Finder!", font=("Arial", 14))
info_label.pack(pady=20)

# Start the application
app.mainloop()


# # API endpoint and key
# API_URL = 'https://api.api-ninjas.com/v1/animals'

# API_KEY = "Vfm52mnwlUBEhhMCnii+Ow==kwlqFtMnriD4YDkj"

# # Function to get animal data from the API
# def get_animal_data(animal_name):
#     headers = {
#         "X-Api-Key": API_KEY
#     }
#     # Send request to get specific animal information
#     response = requests.get(API_URL + f"?name={animal_name}", headers=headers)
#     if response.status_code == 200:
#         return response.json()
#     return None

# # Function to display animal information
# def show_animal_info(animal_name):
#     animal_data = get_animal_data(animal_name)
#     if animal_data and len(animal_data) > 0:
#         animal_info = animal_data[0]  # Get the first animal info from the list
#         info_text = f"Name: {animal_info['name']}\n"
#         info_text += f"Scientific Name: {animal_info['scientific_name']}\n"
#         info_text += f"Habitat: {animal_info['habitat']}\n"
#         info_text += f"Diet: {animal_info['diet']}\n"
#         info_text += f"Description: {animal_info['description']}\n"
#         info_text += f"Emoji: {animal_info.get('emoji', 'No emoji available')}\n"
#     else:
#         info_text = "Error fetching data."

#     info_label.config(text=info_text)



# # Create a frame for buttons
# button_frame = tk.Frame(app)
# button_frame.pack(pady=20)

# # Create buttons for animal emojis
# animal_emojis = {
#     "🐶": "Dog",
#     "🐱": "Cat",
#     "🐰": "Rabbit",
#     "🐸": "Frog",
#     "🦁": "Lion",
#     "🐨": "Koala",
#     "🐵": "Monkey"
# }

# # Create a button for each animal emoji
# for emoji, name in animal_emojis.items():
#     button = tk.Button(button_frame, text=emoji, font=("Arial", 30), command=lambda n=name: show_animal_info(n))
#     button.pack(side=tk.LEFT, padx=5)




