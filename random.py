#!/usr/bin/env python
# coding: utf-8

# # Random password generator

# In[ ]:


import string
import random
length = int(input("Enter password length: "))
print('''Choose character set for password from these : 
1. Digits
2. Letters
3. Special characters
4. Exit''')
characterList = ""
while(True):
    choice = int(input("Pick a number "))
    if(choice == 1):
        characterList += string.ascii_letters
    elif(choice == 2):
        characterList += string.digits
    elif(choice == 3):
        characterList += string.punctuation
    elif(choice == 4):
         break
    else:
        print("Please pick a valid option!")
password = []
for i in range(length):
    randomchar = random.choice(characterList)
    password.append(randomchar)
print("The random password is " + "".join(password))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # WEATHER FORECASTING APP

# In[2]:


import tkinter as tk
import requests
def get_weather():
    city = city_entry.get()
    url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=b9821a4b7c46c98de4ebb57990dd8098&units=metric"
    response = requests.get(url)
    weather_data = response.json()
    if weather_data["cod"] != "404":
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        description = weather_data["weather"][0]["description"]
        weather_label.config(text=f"Temperature: {temperature}°C\nHumidity: {humidity}%\nDescription: {description}")
    else:
        weather_label.config(text="City not found")
# Create the main window
window = tk.Tk()
window.title("Weather Forecast App")
# Create and place widgets
city_label = tk.Label(window, text="Enter city:")
city_label.pack()
city_entry = tk.Entry(window)
city_entry.pack()
get_weather_button = tk.Button(window, text="Get Weather", command=get_weather)
get_weather_button.pack()
weather_label = tk.Label(window, text="")
weather_label.pack()
# Run the application
window.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




