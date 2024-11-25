# howlong
Small script to calculate time difference from now to a chosen date.

## how to use

supported date formats are: 
- dd/mm/yyyy 
- dd/mm/yyy HH
- dd/mm/yyy HH:mm
- dd/mm/yyy HH:mm:ss
- dd.mm.yyyy
- dd.mm.yyy HH:mm
- dd.mm.yyy HH:mm:ss
- dd.mm.yyyy HH:mm:ss

### use with python
`~/howlong $ python howlong.py "01/12/2024 12:00:14"`

`~/howlong $ Time from 25/11/2024 08:17:23 to 01/12/2024 12:00:14: 6 days, 3 hours, 42 minutes, 50 seconds`

or

`~/howlong $ python3 howlong.py "01/12/2024 `

`~/howlong $ Time from 25/11/2024 08:09:50 to 01/12/2024: 5 days, 15 hours, 50 minutes, 9 seconds`

### use with binary

move the binary to /bin 

`~/howlong $ sudo mv howlong /bin`

`sudo chmod +x /bin/howlong`

then just type in from anywhere:

`~ $ howlong 01/12/2024`

