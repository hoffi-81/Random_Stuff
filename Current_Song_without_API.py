import pywinctl as pwc

win = pwc.getAllAppsWindowsTitles()

if "Spotify.exe" in win:
     current_title = win["Spotify.exe"][0]  # Initialize with the current title
     print(current_title)
     while True:
          win = pwc.getAllAppsWindowsTitles()  # Get the updated list of window titles
          new_title = win["Spotify.exe"][0]

          # Check if the window title has changed
          if current_title != new_title:
               print(new_title)  # Print the new title
               current_title = new_title  # Update the current title