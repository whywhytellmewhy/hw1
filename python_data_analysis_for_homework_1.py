# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb ALL weather data in 108060018.csv
cwb_filename = '108060018.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)
#=======================================

# Part. 3
#=======================================
# Analyze data (pick out data) depending on groups in need (whose "station_id" is "C0A880" or "C0F9A0" or "C0G640" or "C0R190" or "C0X260" ) and store them into target_data_1
# So there are only data with "station_id" of "C0A880" or "C0F9A0" or "C0G640" or "C0R190" or "C0X260" being left (picked out)
target_data_1 = list(filter(lambda item: item['station_id'] == 'C0A880' or item['station_id'] == 'C0F9A0' or item['station_id'] == 'C0G640' or item['station_id'] == 'C0R190' or item['station_id'] == 'C0X260', data))


# Pick out only "station_id" and "TEMP" values from the data in target_data_1
# And store them in the format form (a two-dimensional matrix, called target_data, whose columns and rows mean different "station_id" and "TEMP," respectively, and for different rows, the "station_id" data have one-to-one corresponding to the "TEMP" data) in order to match the form of the problem's suggestion
# For the convenience in later calculation, I use "float()" function to change the datatype of "TEMP" from char to float numbers, and "station_id" remains char type
target_data = [[column['station_id'],float(column['TEMP'])] for column in target_data_1]


# Determine those whose "TEMP" values are -99.000 or -999.000, and change these numbers to the value of "-1" in order to show their speciality (in later calculation, when the maximum value is "-1," we can know that there exists no valid value at all, so we can therefore print "'None'")
for k in range(0,len(target_data_1)):
    if target_data[k][1]==-99.000 or target_data[k][1]==-999.000:
        target_data[k][1]=-1


# To sort "station_id" in alphabetical order, in order to print in alphabetical order at later stage
for i in range(0,len(target_data_1)):
    for j in range(i,len(target_data_1)):
        if target_data[i][0]>target_data[j][0]:  # When the ASCII code for the former is greater than that of the latter, then change the order of these two
            x=target_data[i]                     # Put the data of the former into x, the buffer
            target_data[i]=target_data[j]        # Put the data of the latter into the former
            target_data[j]=x                     # Put the data of the buffer into the latter


# Add a special label to denote the end of the data (I choose "['-1',-1]" because it is not possible to have this data in a valid target_data)
target_data.append(['-1',-1])


# Compare the "TEMP" data and remove the smaller one
term=target_data[0][0]                                  # Initialize the variable "term" to be the first value of "station_id"
maxi=target_data[0][1]                                  # Initialize the variable "maxi" to be the first value of "TEMP"
t=1                                                     # Comparison starts from column number "1"

while term !='-1':                                      # Do comparison and deletion until arriving at the terminal data, ['-1',-1] (the special label to denote the end of the data)
    if term !=target_data[t][0]:                        # To make sure that we are comparing values of "TEMP" from the data of the SAME "station_id"; if not, that means the comparison of the previous one has been done, and then we can start a new comparison with a new "station_id" value
        term=target_data[t][0]                          # Because we start a new comparison, initialize the variable
        maxi=target_data[t][1]                          # Because we start a new comparison, initialize the variable
        t=t+1                                           # Continue to compare with the next index
    else:                                               # If we are comparing values of "TEMP" from the data of the SAME "station_id," then we continue to do the comparison
        if maxi <target_data[t][1]:                     # If this "TEMP" is greater than the previous maximum, that means this number is the new maximum of all the data of the same "station_id" before (including) this one
            maxi=target_data[t][1]                      # Set the new maximum value to the variable
            target_data.remove(target_data[t-1])        # Remove the data having the previous maximum from the target_data list
        else:                                           # If this "TEMP" is NOT greater than the previous maximum, that means the maximum remains the same
            target_data.remove(target_data[t])          # So remove this data from the target_data list



# Up to now, there have been only 6 data left in the target_data list, where the first 5 data are those whose "TEMP" value is the highest among all data of the same "station_id" type, while the last data is "['-1',-1]"
# Remove the last data of the list because we don't need to print it out
target_data.remove(target_data[-1])


# Determine whose maximum "TEMP" value is "-1," for which it means that there exists no valid "TEMP" value at all, so we can therefore print out "'None'" So change their "TEMP" values to "'None'"
for y in range(0,len(target_data)):
    if target_data[y][1]==-1:
        target_data[y][1]='None'

#=======================================

# Part. 4
#=======================================
# Print the result
print(target_data)
#========================================