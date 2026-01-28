import subprocess
import time

def run_sudo_command(command, cwd=None):
    try:
        subprocess.Popen(['sudo'] + command, cwd=cwd)
        print(f"Started command: {' '.join(command)}")
    except Exception as e:
        print("Error occurred:", e)

def move_mouse_to_coordinates(coords):
    for x, y in coords:
        print(f"Moving mouse to: ({x}, {y})")  
        result = subprocess.run(['xdotool', 'mousemove', str(x), str(y)], capture_output=True, text=True)
        if result.returncode != 0:
            print(f"xdotool error: {result.stderr}")  
        
        click_result = subprocess.run(['xdotool', 'click', '1'], capture_output=True, text=True)
        if click_result.returncode != 0:
            print(f"xdotool click error: {click_result.stderr}")  
        
        time.sleep(1)  

        if (x, y) == (950, 349):
            subprocess.run(['xdotool', 'key', 'ctrl+a'])  
            subprocess.run(['xdotool', 'key', 'Delete'])            
            subprocess.run(['xdotool', 'key', 'ctrl+v'])
            time.sleep(1)  

if __name__ == "__main__":
    commands_to_run = [
        ['torctl', 'start'],               
    ]

    for command in commands_to_run:
        run_sudo_command(command)

    
        run_sudo_command(['./OpenRA-Red-Alert-x86_64.AppImage'])
        time.sleep(2)  
        run_sudo_command(['./OpenRA-Red-Alert-x86_64.AppImage'])
        time.sleep(20)  
        subprocess.run(['xdotool', 'key', 'alt+ctrl+Right'])

        coordinates = [
            (354, 492),
            (777, 338)
        ]
        move_mouse_to_coordinates(coordinates)
        

    # Use Alt+Ctrl+Right Arrow to switch workspaces after the second run
        run_sudo_command(['./OpenRA-Red-Alert-x86_64.AppImage'])
        time.sleep(2)
        run_sudo_command(['./OpenRA-Red-Alert-x86_64.AppImage'])
        time.sleep(20)  
        subprocess.run(['xdotool', 'key', 'alt+ctrl+Right'])

        
        move_mouse_to_coordinates(coordinates)
        
        run_sudo_command(['./OpenRA-Red-Alert-x86_64.AppImage'])
        time.sleep(2)   
        run_sudo_command(['./OpenRA-Red-Alert-x86_64.AppImage'])
        time.sleep(20)  
        subprocess.run(['xdotool', 'key', 'alt+ctrl+Right'])

        
        move_mouse_to_coordinates(coordinates)             
 


        run_sudo_command(['./OpenRA-Red-Alert-x86_64.AppImage'])
        time.sleep(2)
        run_sudo_command(['./OpenRA-Red-Alert-x86_64.AppImage'])
        time.sleep(20)  

        # Move mouse and perform clicks
        move_mouse_to_coordinates(coordinates)
    #temp time in the code to reowredr the bots
    time.sleep(15) 

    # After the loop, run the spamer.py script  
    run_sudo_command(['python3', 'spamer.py'])
    run_sudo_command(['python3', 'oneclick.py'])

   
   
    input("Press Enter to exit the script...")
