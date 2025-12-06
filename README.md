# PyDing Timeaid
PyDing is a timeaid tool authored by [Rose A-Hill](https://github.com/RoseAHill) with the intent to assist in time management. A timeaid is a tool that assists with "Time Blindness" (when you lose track of time easily). It achieves this by playing sounds at various time intervals throughout the day.

## Features
- Plays sounds at specific intervals during each hour between specific hours of the day, not playing during set sleep hours.
- Preloaded with three default sounds:
  - Four various soft dings for the hour
  - Double dings for the half hour
  - A single ding for the 15 and 45 minute mark.
- Defaults sleep hours to 10pm to 8am.
- Prints the time every 5 minutes, starting at the first 5 minute interval, including at the ding times.
- Prints when the program played a ding.

### Current Customizations
- Ability to swap out the sounds (.mp3 format), including setting a separate sound for the different 15 and 45 minute mark.

## Planned Customizations & Icebox Features
- Customizable within the config.ini file using a text editor:
  - Changing the sleep hours
  - Changing the minute marks at which the dings play during
  - Setting a folder name change rather to change the sounds, rather than swapping out the sounds in the current folder
- GUI interface option rather than the terminal
- GUI interface to edit the config.ini rather than using a text editor

## Usage
Currently this app is shipped as a simple python script. It is meant to be left open and running on a machine with an audible default audio output device, ideally speakers.

### Dependencies
__Required:__
- Python 3
- Pip

__Optional Dependencies:__
- Text Editor (for editing the configuration)
- Git (for updates)
- Python Virtual Environment tool (If you know what you're doing)

### Installation
1. Download & extract the zip folder found in Releases (or use Git) into an empty folder (optionally, initiate a virtual environment for the same directory)
2. After installing Python and Pip, from the folder where you saved `clock.py`, run `pip install -r requirements.txt`
4. After pip finished, run the command `python clock.py`. If unsuccessful try `python3 clock.py`.
5. Keep the terminal window open for as long as you want.
6. Restart the window if you wish to make any alterations to the config file or the script.

### Sound File Configuration
1. Create a folder with four .mp3 files, one for each time titled the following:
   - `hour_00.mp3`
   - `quarter_15.mp3`
   - `half_30.mp3`
   - `quarter_45.mp3`
2. Rename the `current` folder to something unique and rename the new custom folder as `current`.