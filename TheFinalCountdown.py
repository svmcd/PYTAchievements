import time
def countdown(t):
    while t > 0:
        print(t)
        t -= 1
        time.sleep(0.001)
    print("""\                                                            
                                                            
                                  ____                      
                                ,'  , `.              ,---, 
                             ,-+-,.' _ |            ,---.'| 
  .--.--.                 ,-+-. ;   , ||            |   | : 
 /  /    '    ,--.--.    ,--.'|'   |  || ,---.      |   | | 
|  :  /`./   /       \  |   |  ,', |  |,/     \   ,--.__| | 
|  :  ;_    .--.  .-. | |   | /  | |--'/    /  | /   ,'   | 
 \  \    `.  \__\/: . . |   : |  | ,  .    ' / |.   '  /  | 
  `----.   \ ," .--.; | |   : |  |/   '   ;   /|'   ; |:  | 
 /  /`--'  //  /  ,.  | |   | |`-'    '   |  / ||   | '/  ' 
'--'.     /;  :   .'   \|   ;/        |   :    ||   :    :| 
  `--'---' |  ,     .-./'---'          \   \  /  \   \  /   
            `--`---'                    `----'    `----'    
                                                            """)

seconds = int(10000)
countdown(seconds)