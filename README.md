## terminalNotes
This is a python script that I created that is a functional notes app and calendar in the terminal
When your terminal opens then your calendar will only display.
The calendar is color coded so that for each day if you have 1 note it will be green, 2 yellow, and 3 or more will be red
This is so that if you wish to put quick reminders that have been piling up, you will notice. 
</br></br>There is a remove notes function, display all notes function, add note, view note, and clear display. 
 The notes save to a json file created called "notes.json", which can be changed to your liking, and reset after each month. The previous month will be saved to a text file called "last_run_month.txt" for a month then overwritten with the next month.
 </br></br>When adding a note, you only have to enter the day for that month. 
 </br>To quit the notes app, enter 7, q, e, or exit (case insensitive)

 1) When adding to ZSH, BASH, KSH (add to .zshrc, .bashrc, .kshrc)</br>
    - Run app.py every time the terminal opens (only displays calendar)</br>
      `python3 /PATH/TO/FILE/app.py`</br>
    - Function to run notes.py (run notes options)</br>
      `function notes() { python3 /PATH/TO/FILE/notes.py }`</br>
      
2) When adding to fish (add to .config/fish/config.fish)</br>
    - Run app.py every time the terminal opens (only displays calendar)</br>
      `python3 /PATH/TO/FILE/app.py`</br>
    - Function to run notes.py (run notes options)</br>
      `function notes`</br>
        `python3 /PATH/TO/FILE/notes.py`</br>
     `end`</br>

3) When adding to C Shell (add to .cshrc)</br>
   - Run app.py every time the terminal opens (only displays calendar)</br>
     `python3 /PATH/TO/FILE/app.py`</br>
   - Function to run notes.py (run notes options)</br>
     `alias notes 'python3 /PATH/TO/FILE/notes.py'`</br>

<subscript>(^You do not need the dashes above when adding to your config file^)</subscript></br>
>To apply changes do:</br>
>source <filename></br>

>If you aren't sure what shell you are running do:</br>
>echo $SHELL</br>

If you are running into any issues please contact me
