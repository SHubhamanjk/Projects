import sounddevice
from scipy.io.wavfile import write
import os

def recorder(fname, sec):
    # Inform the user that recording is starting
    print("Recording has been started...")
    
    # Record audio for the specified duration (sec) with a sampling rate of 44.1 kHz and 2 channels
    reco = sounddevice.rec(int(sec * 44100), samplerate=44100, channels=2)
    
    # Wait for the recording to complete
    sounddevice.wait()

    # Check if the file already exists
    if os.path.exists(fname):
        # Ask for confirmation before overwriting the existing file
        confirm = input("File already exists. Do you want to overwrite it? (yes/no): ")
        if confirm.lower() != "yes":
            print("Recording aborted.")
            return

    # Write the recorded audio to a WAV file with a sampling rate of 44.1 kHz
    write(fname, 44100, reco)
    
    # Inform the user that recording is done
    print("Recording has been done...")

# Ask the user if they want to start recording
per = input("Do you want to start recording? (yes/no): ")

# Check the user's response
if per.lower() == "yes":
    # If yes, ask for the length of the recording in seconds and the file name
    sec = int(input("Enter the length of recording (in seconds): "))
    fname = input("Enter the file name (use .wav as extension name): ")
    
    # Call the recorder function with the specified duration
    recorder(fname, sec)
    
elif per.lower() == "no":
    # If no, thank the user
    print("Thank you")
    
else:
    # If the input is neither yes nor no, inform the user of invalid input
    print("Invalid input")

# Enter a loop to allow the user to record again or exit
while True:
    again = input("Do you want to record again? (yes/no): ")

    # Check the user's response
    if again.lower() == "yes":
        # If yes, ask for the length of the recording in seconds and the new file name
        sec = int(input("Enter the length of recording (in seconds): "))
        fname = input("Enter the new file name (use .wav as extension name): ")
        
        # Call the recorder function with the specified duration
        recorder(fname, sec)
    
    elif again.lower() == "no":
        # If no, thank the user and exit the loop
        print("Thank you")
        break
    
    else:
        # If the input is neither yes nor no, inform the user of invalid input
        print("Invalid input")
