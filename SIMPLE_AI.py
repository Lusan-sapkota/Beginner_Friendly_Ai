import pyttsx3 # pip install pyttsx3
import datetime # pip install datetime
import speech_recognition as sr # pip install speechrecognition
import wikipedia as wiki # pip install wikipedia
import smtplib
import webbrowser as wb 
import os
import pyautogui as pg # pip install pyautogui 
import psutil # pip install psutil
import pyjokes # pip install pyjokes

# initializing pyttsx3
engine = pyttsx3.init()

#function for speak
def speak(audio): 
    engine.say(audio)
    engine.runAndWait()

#function for microphone
def takeCommand(): 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        try:
            audio = r.listen(source, timeout=5)
            print("Recognizing.....")
            query = r.recognize_google(audio, language='en-in').lower()
            print(f'you said-: {query}.')
            return query
        except sr.UnknownValueError:
            print("UnknownValueError: Could not understand audio")
            speak("Sorry, I couldn't understand that.")
        except sr.RequestError as e:
            print(f"RequestError: {e}")
            speak("Sorry, there was an error with the speech recognition service.")
        return 'none'

#function for time
def time(): 
    current_time = datetime.datetime.now().strftime('%I:%M:%S')
    speak(f"The current time is {current_time}")

#function for date
def date(): 
    current_date = datetime.datetime.now().strftime('%d/%m/%Y')
    speak(f"The current date is {current_date}")

#function for greetings
def wishMe(): 
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak('Good morning sir')
    elif hour >= 12 and hour < 18:
        speak("Good afternoon sir")
    elif hour >= 18 and hour < 20:
        speak("Good evening sir")
    else:
        speak("Good night sir")
    speak("I have been waiting sir.")
    speak("Jarvis at your service sir, how can i help you!")

#function for sendingEmail
def sendEmail():
    try:
        speak("To whom should I send the email?")
        to = input("Enter the recipient's email address: ")
        speak("What is the subject of the email?")
        subject = takeCommand()
        speak("What should I say in the email?")
        content = takeCommand()
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        # Replace 'your_email@gmail.com' with your email and 'password' with your password
        server.login('your_email@gmail.com', 'password')
        # Use the recipient's email entered by the user
        server.sendmail('your_email@gmail.com', to, f"Subject: {subject}\n\n{content}")
        server.close()
        speak("Email has been sent")
    except Exception as e:
        print(f"Error sending email: {e}")
        speak("Sorry, I couldn't send the email.")

#function for screenshot    
def screenshot():
    try:
        img = pg.screenshot()
        # replace it with the path where you want to save your screenshot and provide a name for it
        img.save('C:\\Users\\HELIOS\\Pictures\\ss.png')
        speak('Screenshot done')
    except Exception as e:
        print(f"Error: {e}")
        speak('Sorry, I encountered an error while taking a screenshot.')
        
#function for cpu usage display    
def cpu(): 
    usage = str(psutil.cpu_percent())
    speak(f'Cpu is at {usage}')
    
#function for battery percentage display    
def battery(): 
    battery = psutil.sensors_battery()
    speak(f'Battery is at {battery.percent}')
    
#function for jokes
def jokes(): 
    joke = pyjokes.get_joke()
    print(joke)
    speak(joke)

#function for wikipedia search
def wikipedia(): 
    speak(f"searching for {query}")
    query = query.replace("wikipedia", "")
    result = wiki.summary(query, sentences = 2)
    print(result)
    speak(result)

# function for web search
def searchInWeb():  
    speak("What should I search?")
    # Put your actual browser path
    firefox_path = "C:/Program Files/Mozilla Firefox/firefox.exe %s"
    search_query = takeCommand().lower()
    google_search_url = f"https://www.google.com/search?q={search_query}"
    # Open a new tab in the browser with the Google search URL
    wb.get(firefox_path).open_new_tab(google_search_url)

#function for notes
def take_note(): 
    while True:
        speak("What should I remember?")
        data = takeCommand()
        speak(f"You said me to remember {data}. Is that correct?")

        check = takeCommand().lower()
        if 'yes' in check:
            with open('data.txt', 'w') as remember:
                remember.write(data)
            speak('Okay, I have remembered it.')
            break
        elif 'no' in check:
            speak('Tell me again.')
            continue

#function to open spotify
def openSpotify():
    speak("opening spotify")
    # put your actual executable path here
    spotifyExecutable = r'C:\\Users\\HELIOS\\AppData\\Roaming\\Spotify\\Spotify.exe'
    if os.path.isfile(spotifyExecutable):
    # Open Spotify using the executable path
        os.startfile(spotifyExecutable)
    else:
        speak("Spotify executable not found.")

#function to play music
def playMusic():
    #replace with your actual songs-directory
    songsDir = "C:/Users/HELIOS/Music"
    songs = os.listdir(songsDir)
    print(songs)
    os.startfile(os.path.join(songsDir, songs[1]))

#code in this block will be run first
if __name__ == "__main__": 
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'time' in query:
            time()
            
        elif 'date' in query:
            date()
            
        elif 'wikipedia' in query:
            wikipedia()

        elif 'search in web' in query:
            searchInWeb()
            
        elif 'open spotify' in query:
            openSpotify()
                
        elif 'play song' in query:
            playMusic()
            
        elif 'take a screenshot' in query :
            screenshot()
            
        elif 'cpu percentage' in query:
            cpu()
            
        elif 'battery percentage' in query:
            battery()
            
        elif 'joke' in query:
            jokes()
            
        elif 'take note' in query:
            take_note()
                
            
        elif 'do you know anything' in query:
            remember = open('data.txt', 'r')
            speak(f"I remember that {remember.read()}")
            
            
        elif 'logout my pc' in query:
            speak("Logging out your pc")
            os.system("Shutdown -l")
            
        elif 'shut down my pc' in query:
            speak("shutting down your pc")
            os.system("Shutdown /s /t 1")
            
        elif 'restart my pc' in query:
            speak("restarting your pc")
            os.system("Shutdown /r /t 1")
            
        elif 'send email' in query:
            try:
                sendEmail()
            except Exception as e:
                print(f"Error: {e}")
                speak("Sorry, I couldn't send the email.")
            
        elif 'exit' and 'offline' in query:
            speak("exiting the program thank you sir!")
            quit()
            
# i have given you steps so you can add as many function as you want you can automate everything like this 
# ask for chatgpt help or comment down if you have any query