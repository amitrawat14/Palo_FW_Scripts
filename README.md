# Palo_FW_Scripts
Scripts to find if rule is open in single of multiple Vsys environment.


Add this for bigger command output in the script
    pager_cli ='set cli pager off \n'
    
    pager_cli = pager_cli.encode()
    
    session.send(pager_cli)
    
    time.sleep(2)
    
    pager_output = session.recv(9999)
    
    print(pager_output.decode())
