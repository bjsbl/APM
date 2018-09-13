from Runner import MasterRunner

if __name__ == '__main__':
    runner =  MasterRunner('*', 5000)
    main_greenlet = runner.greenlet
    main_greenlet.join()
    
