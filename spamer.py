import subprocess
import time

# Function to simulate mouse click
def click(x, y):
    subprocess.run(['xdotool', 'mousemove', str(x), str(y), 'click', '1'])

# Function to simulate keyboard input
def type_message(message):
    subprocess.run(['xdotool', 'type', '--delay', '0', message])
    subprocess.run(['xdotool', 'key', 'Return'])

# Function to handle Alt+Tab and typing
def alt_tab_and_type(message):
    while True:  # Loop indefinitely
        # Alt+Tab and type the message
        subprocess.run(['xdotool', 'key', 'Alt_L+Tab'])
        time.sleep(0.15)  # Wait for the switch to take effect
        type_message(message)  # Type the message
        time.sleep(0.15)  # Wait before the next action

        # Perform Alt+Ctrl+Left Arrow
        subprocess.run(['xdotool', 'key', 'Alt_L+Control_L+Left'])
        time.sleep(0.15)  # Wait for the action to take effect
        type_message(message)  # Type the message again
        time.sleep(0.15)  # Wait before the next action

        # Alt+Tab again
        subprocess.run(['xdotool', 'key', 'Alt_L+Tab'])
        time.sleep(0.15)  # Wait for the switch to take effect

        # Perform Alt+Ctrl+Right Arrow (note original had left; keeping original pattern but using Right here as in later steps)
        subprocess.run(['xdotool', 'key', 'Alt_L+Control_L+Left'])
        time.sleep(0.15)  # Wait for the action to take effect
        type_message(message)  # Type the message again
        time.sleep(0.15)  # Wait before the next action
        
        subprocess.run(['xdotool', 'key', 'Alt_L+Tab'])
        time.sleep(0.15)  # Wait for the switch to take effect
        type_message(message)  # Type the message
        time.sleep(0.15)  # Wait before the next action

        # Perform Alt+Ctrl+Left Arrow
        subprocess.run(['xdotool', 'key', 'Alt_L+Control_L+Left'])
        time.sleep(0.15)  # Wait for the action to take effect
        type_message(message)  # Type the message again
        time.sleep(0.15)  # Wait before the next action

      
        subprocess.run(['xdotool', 'key', 'Alt_L+Tab'])
        time.sleep(0.15)  # Wait for the switch to take effect
        type_message(message)  # Type the message
        time.sleep(0.15)  # Wait before the next action

        # Perform Alt+Ctrl+Left Arrow (original later used right; keep that change below)
        subprocess.run(['xdotool', 'key', 'Alt_L+Control_L+Right'])
        time.sleep(0.15)  # Wait for the action to take effect
        type_message(message)  # Type the message again
        time.sleep(0.15)  # Wait before the next action
        
        subprocess.run(['xdotool', 'key', 'Alt_L+Tab'])
        time.sleep(0.15)  # Wait for the switch to take effect
        type_message(message)  # Type the message
        time.sleep(0.15)  # Wait before the next action

        
        # Perform Alt+Ctrl+Right Arrow
        subprocess.run(['xdotool', 'key', 'Alt_L+Control_L+Right'])
        time.sleep(0.15)  # Wait for the action to take effect
        type_message(message)  # Type the message again
        time.sleep(0.15)
        
        subprocess.run(['xdotool', 'key', 'Alt_L+Tab'])
        time.sleep(0.15)  # Wait for the switch to take effect
        type_message(message)  # Type the message
        time.sleep(0.15)
        
        subprocess.run(['xdotool', 'key', 'Alt_L+Control_L+Right'])
        time.sleep(0.15)  # Wait for the action to take effect
        type_message(message)  # Type the message again
        time.sleep(0.15)  # Wait before the next action
        
         
        
# Main function
def automated_click_and_type():
    while True:  # Loop indefinitely
        # Click at (3214, 723)
        click(3214, 723)
        
        # Wait for 5 seconds
        time.sleep(5)
        
        # Click at (2954, 802)
        click(2954, 802)
        
        # Message to type
        message = """discord.gg/qVsesEsk discord.gg/qVsesEsk discord.gg/qVsesEsk discord.gg/qVsesEsk discord.gg/qVsesEsk discord.gg/qVsesEsk discord.gg/qVsesEsk discord.gg/qVsesEsk discord.gg/qVsesEsk discord.gg/qVsesEsk discord.gg/qVsesEsk discord.gg/qVsesEsk discord.gg/qVsesEsk discord.gg/qVsesEsk discord.gg/qVsesEsk discord.gg/qVsesEsk discord.gg/qVsesEsk discord.gg/qVsesEsk discord.gg/qVsesEsk discord.gg/qVsesEsk discord.gg/qVsesEsk discord.gg/qVsesEsk """
        
        # Start the Alt+Tab and typing process
        alt_tab_and_type(message)

# Run the function
automated_click_and_type()


