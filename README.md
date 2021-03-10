# hw1
Created on 110.2.28


Q1: How to setup and run your program？
A1: I use the following code to create the file "python_data_analysis_for_homework_1.py" where the codes are stored:

$ cd ~/ee2405
$ git clone https://github.com/whywhytellmewhy/hw1.git
$ cd ~/ee2405/hw1
$ mbed new python_data_analysis --scm none
$ cd python_data_analysis
$ code python_data_analysis_for_homework_1.py &

And then edit the "python_data_analysis_for_homework_1.py" file.
A brief outline about what the codes do and the purpose to use them is in the following:
(1) Part. 1 --> Import .csv module
(2) Part. 2 --> Read ALL cwb weather data in 108060018.csv and store them into a list
(3) Part. 3 --> Filter out data of those interesting "station_id" values ("C0A880" or "C0F9A0" or "C0G640" or "C0R190" or "C0X260") 
            --> Pick out their "station_id" and "TEMP" values in the format form 
            --> Remove the data whose value of the TEMP (temperature) column is '-99.000' or '-999.000'.
            --> Sort "station_id" in lexicographical order
            --> Compare the "TEMP" values from data of the same "station_id" and remove the smaller ones from the list, until there is only one datum left for each "station_id"
            --> If all "TEMP" values among data of the same "station_id" are '-99.000' or '-999.000,' then change the maximum "TEMP" value into "'None'"
(4) Part. 4 --> Print out the result to the terminal

For more details, please refer to the comments of the codes in "python_data_analysis_for_homework_1.py".

To run the program, I type the following codes in the terminal:
$ python3 python_data_analysis_for_homework_1.py

And it popped out that
[['C0A880', 21.7], ['C0F9A0', 28.2], ['C0G640', 26.9], ['C0R190', 30.6], ['C0X260', 28.5]]
[1]+  Done                    code python_data_analysis_for_homework_1.py


Q2: What are the results？
A2: The results was
[['C0A880', 21.7], ['C0F9A0', 28.2], ['C0G640', 26.9], ['C0R190', 30.6], ['C0X260', 28.5]]

