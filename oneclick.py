import subprocess
import time

# Coordinates
x_old, y_old = 705, 805 #reload server list
x_third, y_third = 777, 338 #click on first server slot
x_new, y_new = 779, 364 #click on server slot 2
x_old1, y_old1 = 1093, 589 #click the abort button

def click_at(x, y, button='1'):
    subprocess.run(['xdotool', 'mousemove', str(x), str(y), 'click', button])

def run_sudo_command(command):                
    try:
        subprocess.Popen(['sudo'] + command)
        print(f"Started command: {' '.join(command)}")
    except Exception as e:
        print("Error occurred:", e)

while True:
    
    click_at(x_old, y_old)

    time.sleep(0.25)
    
    click_at(x_old, y_old)

    time.sleep(0.25)
    
    click_at(x_old, y_old)

    time.sleep(0.25)
    
    click_at(x_old, y_old)

    time.sleep(1)
 
    click_at(x_third, y_third)
    click_at(x_third, y_third)
    time.sleep(0.1)
    click_at(x_third, y_third)
    click_at(x_third, y_third)
    time.sleep(0.1)
    click_at(x_third, y_third)
    click_at(x_third, y_third)
    time.sleep(0.1)
    click_at(x_third, y_third)
    click_at(x_third, y_third)
    time.sleep(0.1)
    click_at(x_third, y_third)
    click_at(x_third, y_third)
    click_at(x_third, y_third)
    click_at(x_third, y_third)
    time.sleep(0.1)
    click_at(x_third, y_third)
    click_at(x_third, y_third)
    time.sleep(0.1)
    click_at(x_third, y_third)
    click_at(x_third, y_third)
    time.sleep(0.1)
    click_at(x_third, y_third)
    click_at(x_third, y_third)
    time.sleep(0.1)
    click_at(x_third, y_third)
    click_at(x_third, y_third)
    
    time.sleep(0.25)
    
    click_at(x_new, y_new)
    click_at(x_new, y_new)
    time.sleep(0.1)
    click_at(x_new, y_new)
    click_at(x_new, y_new)
    time.sleep(0.1)
    click_at(x_new, y_new)
    click_at(x_new, y_new)
    time.sleep(0.1)
    click_at(x_new, y_new)
    click_at(x_new, y_new)
    click_at(x_new, y_new)
    click_at(x_new, y_new)
    time.sleep(0.1)
    click_at(x_new, y_new)
    click_at(x_new, y_new)
    time.sleep(0.1)
    click_at(x_new, y_new)
    click_at(x_new, y_new)
    time.sleep(0.1)
    click_at(x_new, y_new)
    click_at(x_new, y_new)
   
    time.sleep(0.5)
    
    click_at(x_old, y_old)

    time.sleep(0.25)
    
    click_at(x_old, y_old)

    time.sleep(0.25)
    
    click_at(x_old, y_old)

    time.sleep(0.25)
    
    click_at(x_old, y_old)

    time.sleep(0.25)
    time.sleep(0.5)
    
    click_at(x_old, y_old)

    time.sleep(0.25)
    
    click_at(x_old, y_old)

    time.sleep(0.25)
    
    click_at(x_old, y_old)

    time.sleep(0.25)
    
    click_at(x_old, y_old)

    time.sleep(0.25)
    
    click_at(x_third, y_third)
    click_at(x_third, y_third)
    time.sleep(0.1)
    click_at(x_third, y_third)
    click_at(x_third, y_third)
    time.sleep(0.1)
    click_at(x_third, y_third)
    click_at(x_third, y_third)
    time.sleep(0.1)
    click_at(x_third, y_third)
    click_at(x_third, y_third)
    time.sleep(0.1)
    click_at(x_third, y_third)
    click_at(x_third, y_third)
    click_at(x_third, y_third)
    click_at(x_third, y_third)
    time.sleep(0.1)
    click_at(x_third, y_third)
    click_at(x_third, y_third)
    time.sleep(0.1)
    click_at(x_third, y_third)
    click_at(x_third, y_third)
    time.sleep(0.1)
    click_at(x_third, y_third)
    click_at(x_third, y_third)
    time.sleep(0.1)
    click_at(x_third, y_third)
    click_at(x_third, y_third)
    
    time.sleep(0.25)
    
    click_at(x_new, y_new)
    click_at(x_new, y_new)
    time.sleep(0.1)
    click_at(x_new, y_new)
    click_at(x_new, y_new)
    time.sleep(0.1)
    click_at(x_new, y_new)
    click_at(x_new, y_new)
    time.sleep(0.1)
    click_at(x_new, y_new)
    click_at(x_new, y_new)
    click_at(x_new, y_new)
    click_at(x_new, y_new)
    time.sleep(0.1)
    click_at(x_new, y_new)
    click_at(x_new, y_new)
    time.sleep(0.1)
    click_at(x_new, y_new)
    click_at(x_new, y_new)
    time.sleep(0.1)
    click_at(x_new, y_new)
    click_at(x_new, y_new)
   
   
    time.sleep(23)
    
    run_sudo_command(['torctl', 'chngid'])
    
    time.sleep(3)
    
    click_at(x_old1, y_old1)
    click_at(x_old1, y_old1)
    time.sleep(0.1)
    click_at(x_old1, y_old1)
    click_at(x_old1, y_old1)
    time.sleep(0.1)
    click_at(x_old1, y_old1)
    click_at(x_old1, y_old1)
    time.sleep(0.1)
    click_at(x_old1, y_old1)
    click_at(x_old1, y_old1)
    time.sleep(0.1)    
    click_at(x_old1, y_old1)
    click_at(x_old1, y_old1)
    time.sleep(0.1)
    click_at(x_old1, y_old1)
    click_at(x_old1, y_old1)
    time.sleep(0.1)
    click_at(x_old1, y_old1)
    click_at(x_old1, y_old1)
    time.sleep(0.1)
    click_at(x_old1, y_old1)
    click_at(x_old1, y_old1)
    time.sleep(0.1)
    click_at(x_old1, y_old1)
    click_at(x_old1, y_old1)
    time.sleep(0.1)
    click_at(x_old1, y_old1)
    click_at(x_old1, y_old1)
    time.sleep(0.1)    
    click_at(x_old1, y_old1)
    click_at(x_old1, y_old1)
    time.sleep(0.1)
    click_at(x_old1, y_old1)
    click_at(x_old1, y_old1)
    time.sleep(0.25)
    
    click_at(x_old, y_old)

    time.sleep(0.25)
    
    click_at(x_old, y_old)

    time.sleep(0.25)
    
    click_at(x_old, y_old)

    time.sleep(0.25)
    
    click_at(x_old, y_old)

    time.sleep(0.25)
    
    click_at(x_old, y_old)

    time.sleep(0.25)
    
    click_at(x_old, y_old)

    time.sleep(0.25)
    
    click_at(x_old, y_old)

    time.sleep(0.25)
    time.sleep(0.25)
    
    click_at(x_old, y_old)

    time.sleep(0.25)
    
    click_at(x_old, y_old)

    time.sleep(0.25)
    
    click_at(x_old, y_old)

    time.sleep(0.25)
    
    click_at(x_old, y_old)

    time.sleep(0.25)
    
    click_at(x_old, y_old)

    time.sleep(0.25)
    
    click_at(x_old, y_old)

    time.sleep(0.25)
    
    click_at(x_old, y_old)

    time.sleep(0.25)
    click_at(x_old1, y_old1)
    click_at(x_old1, y_old1)
    time.sleep(0.1)
    click_at(x_old1, y_old1)
    click_at(x_old1, y_old1)
    time.sleep(0.1)  
    click_at(x_old1, y_old1)
    click_at(x_old1, y_old1)
    time.sleep(0.1)
    click_at(x_old1, y_old1)
    click_at(x_old1, y_old1)
    time.sleep(0.1)    
    click_at(x_old1, y_old1)
    click_at(x_old1, y_old1)
    time.sleep(0.1)
    click_at(x_old1, y_old1)
    click_at(x_old1, y_old1)
    time.sleep(0.1)
    click_at(x_old1, y_old1)
    click_at(x_old1, y_old1)
    time.sleep(0.1)
    click_at(x_old1, y_old1)
    click_at(x_old1, y_old1)
    time.sleep(0.1)    
    click_at(x_old1, y_old1)
    click_at(x_old1, y_old1)
    time.sleep(0.1)
    click_at(x_old1, y_old1)
    click_at(x_old1, y_old1)
    time.sleep(0.1)
    click_at(x_old1, y_old1)
    click_at(x_old1, y_old1)
    time.sleep(0.1)
    click_at(x_old1, y_old1)
    click_at(x_old1, y_old1)
    time.sleep(0.1)
    click_at(x_old1, y_old1)
    click_at(x_old1, y_old1)
    time.sleep(0.1)    
    click_at(x_old1, y_old1)
    click_at(x_old1, y_old1)
    time.sleep(0.1)
    click_at(x_old1, y_old1)
    click_at(x_old1, y_old1)
    click_at(x_old1, y_old1)
    click_at(x_old1, y_old1)
    time.sleep(0.1)
    click_at(x_old1, y_old1)
    click_at(x_old1, y_old1)
    time.sleep(0.1)
    click_at(x_old1, y_old1)
    click_at(x_old1, y_old1)
    time.sleep(0.1)  
    click_at(x_old1, y_old1)
    click_at(x_old1, y_old1)
    time.sleep(0.1)
    click_at(x_old1, y_old1)
    click_at(x_old1, y_old1)
    time.sleep(1)     
    click_at(x_old, y_old)

    time.sleep(0.25)
    
    click_at(x_old, y_old)

    time.sleep(0.25)
    
    click_at(x_old, y_old)

    time.sleep(0.25)
    
    click_at(x_old, y_old)

    time.sleep(0.25)
    
    click_at(x_old, y_old)

    time.sleep(0.25)
    
    click_at(x_old, y_old)

    time.sleep(0.25)
    
    click_at(x_old, y_old)

    time.sleep(0.25)
    
    click_at(x_old, y_old)

    time.sleep(0.25)
    time.sleep(0.25)
    
    click_at(x_old, y_old)

    time.sleep(0.25)
    
    click_at(x_old, y_old)

    time.sleep(0.25)
    
    click_at(x_old, y_old)

    time.sleep(0.25)
    
    click_at(x_old, y_old)

    time.sleep(0.25)
    
    click_at(x_old, y_old)

    time.sleep(0.25)
    
    click_at(x_old, y_old)

    time.sleep(0.25)
    
    click_at(x_old, y_old)

    time.sleep(0.25)
    
    
    
