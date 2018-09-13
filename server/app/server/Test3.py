from Runner import SlaveRunner

if __name__ == '__main__':
    runner = SlaveRunner('127.0.0.1', 5000)
    main_greenlet = runner.greenlet
    main_greenlet.join()
