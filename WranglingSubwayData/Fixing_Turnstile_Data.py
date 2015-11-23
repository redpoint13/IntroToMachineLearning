import csv

def fix_turnstile_data(path, filenames):
    '''
    Filenames is a list of MTA Subway turnstile text files. A link to an example
    MTA Subway turnstile text file can be seen at the URL below:
    http://web.mta.info/developers/data/nyct/turnstile/turnstile_110507.txt
    
    As you can see, there are numerous data points included in each row of the
    a MTA Subway turnstile text file. 

    You want to write a function that will update each row in the text
    file so there is only one entry per row. A few examples below:
    A002,R051,02-00-00,05-28-11,00:00:00,REGULAR,003178521,001100739
    A002,R051,02-00-00,05-28-11,04:00:00,REGULAR,003178541,001100746
    A002,R051,02-00-00,05-28-11,08:00:00,REGULAR,003178559,001100775
    
    Write the updates to a different text file in the format of "updated_" + filename.
    For example:
        1) if you read in a text file called "turnstile_110521.txt"
        2) you should write the updated data to "updated_turnstile_110521.txt"

    The order of the fields should be preserved. Remember to read through the 
    Instructor Notes below for more details on the task. 
    
    In addition, here is a CSV reader/writer introductory tutorial:
    http://goo.gl/HBbvyy

    You can see a sample of the turnstile text file that's passed into this 
    function and the the corresponding updated file in the links below:

    Sample input file:
    https://www.dropbox.com/s/mpin5zv4hgrx244/turnstile_110528.txt
    Sample updated file:
    https://www.dropbox.com/s/074xbgio4c39b7h/solution_turnstile_110528.txt
    '''
    # open the file for reading
    f_in = open(path+filenames, 'r')
    # create file to update with the new data
    f_out = open(path + 'updated_' + filenames, 'w')
    print(f_out)
    # create reader and writer based on file specs
    reader_in = csv.reader(f_in, delimiter=',')
    writer_out = csv.writer(f_out, delimiter=',',lineterminator="\n")

    # uncomment if first line of csv contains header row
    # reader_in.next()

    for line in reader_in:
        # your code here
        # print(line)
        common_1 = line[0]
        common_2 = line[1]
        common_3 = line[2]
        counter = 3
        while counter < len(line):
            # print(counter)
            element_1 = line[counter]
            element_2 = line[counter + 1]
            element_3 = line[counter + 2]
            element_4 = line[counter + 3]
            element_5 = line[counter + 4]

            new_line = [common_1, common_2, common_3, element_1, element_2,
                        element_3, element_4, element_5]
            # print(new_line)
            writer_out.writerow(new_line)
            counter = counter + 5
    f_in.close()
    f_out.close()

path_to = "C:\Users\Tony\Documents\GitHub\IntroDataScience\dataWrangling\\"
filename = "turnstile_110507.txt"
fix_turnstile_data(path_to, filename)


