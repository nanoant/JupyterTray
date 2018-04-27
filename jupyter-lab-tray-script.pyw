import jupyterlab.labapp

server = None


def shutdown(tray):
    global server
    if server is not None:
        server.io_loop.add_callback_from_signal(server.io_loop.stop)
    else:
        print('Server is not initialized')


def tray_thread():
    import win32tray
    hover_text = "Jupyter Lab Server"
    menu_options = ()
    win32tray.SysTrayIcon('favicon.ico', hover_text, menu_options, on_quit=shutdown, default_menu_index=1)


def main():
    global server
    import threading
    tray = threading.Thread(target=tray_thread)

    server = jupyterlab.labapp.LabApp.instance()
    server.initialize()

    tray.start()
    server.start()
    tray.join()


if __name__ == '__main__':
    import ctypes
    ctypes.windll.user32.SetProcessDPIAware()
    main()
