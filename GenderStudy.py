#!/usr/bin/python

import math
import subprocess
import optparse
import sys
import os

class calc_genders:
   
    def __init__(self, group_name, text_file, opts):
        my_dictionary_male = {}
        my_dictionary_female = {}
        my_dictionary_female_long = {}
        my_dictionary_male_long = {}
        array=[]
        self.female_count = 0
        self.male_count = 0
        self.unsureCount = 0
        self.Summary = open("Summary.txt","a")
        my_dictionary_male = self.create_dict("male_short_list.txt")
        my_dictionary_female = self.create_dict("female_short_list.txt")
        text = open(text_file)
        for line in text:
            full_name = line.split(",")
            array.append(full_name[0]+'\n')
        female_first_count = open("female_first_count.txt","w")
        male_first_count = open("male_first_count.txt", "w")
        unknown = open("unknown_first.txt","w")
        second_unknown = open("unknown_second.txt","w")
        female_long = open("female_long_list.txt")
        k = 1
        for line in female_long:
            my_dictionary_female_long[line] = k
            k  = k + 1
        male_long = open("male_long_list.txt")
        l = 1
        for line in male_long:
            my_dictionary_male_long[line] = l
            l  = l + 1
        first_unknown_list = self.separate_names(array, my_dictionary_female,my_dictionary_male, female_first_count, male_first_count, unknown, False)
        second_unknown_list = self.separate_names(first_unknown_list, my_dictionary_female_long, my_dictionary_male_long, female_first_count, male_first_count, second_unknown, True)
        self.create_summary(group_name)

    def create_summary(self, group_name):
        print float(self.female_count)/self.male_count
        self.Summary.write("For "+ str(group_name) + ", the proportion of males to females:"+ "\n")
        self.Summary.write("     There were " + str(self.female_count) + " females"+ "\n")
        self.Summary.write("     There were " + str(self.male_count)+ " males"+ "\n")
        self.Summary.write("     There were " + str(self.unsureCount)+ " unsure names"+ "\n")
        self.Summary.write("The ratio of females to males is " + str(float(self.female_count)/self.male_count)+ "\n")
        self.Summary.write("     Percent female: " + str((float(self.female_count)/(self.female_count+self.male_count)*100))+"%"+ "\n")
        self.Summary.write("     Percent male: " + str((float(self.male_count)/(self.female_count+self.male_count)*100))+"%"+ "\n")
        self.Summary.write(" --------------------------------------------------------------------------------------"+ "\n")
        self.Summary.write(" "+ "\n")


    def create_dict(self, python_string):
        my_dictionary = {}
        text = open(python_string)
        i = 1
        for line in text:
            my_dictionary[line] = i
            i  = i + 1  
        return my_dictionary 

    def separate_names(self, search_array, dictionary_female, dictionary_male, female_first_count, first_count_male, unsure, tf):
        unknown = []
        for i in range(len(search_array)):
            name = str(search_array[i])
            female_name = False
            male_name = False
            if name in dictionary_female:
                female_name = True
            if name in dictionary_male:
                male_name = True
            if female_name and male_name:
                female_rank = dictionary_female[name]
                male_rank = dictionary_male[name]
                if female_rank < male_rank:
                    female_name = True
                    male_name = False
                else:
                    female_name = False
                    male_name = True
            if female_name:
                female_first_count.write(name)
                self.female_count = self.female_count + 1
            elif male_name:
                first_count_male.write(name)
                self.male_count = self.male_count + 1
            if not female_name and not male_name:
                unknown.append(name)
                unsure.write(name)
                if tf:
                    self.unsureCount = self.unsureCount + 1
        return unknown

def setup_options():
    parser=optparse.OptionParser()
    parser.add_option('--title', dest='group_name', help='Title of group to be analyzed', default='Students in program')
    parser.add_option('--textfile', dest='text_file_name', help="Specify title of text file to be analyzed", default='')
    opts=parser.parse_args()
    return opts


if __name__ == '__main__':
    opts, parser=setup_options()
    country = calc_genders(opts.group_name, opts.text_file_name, opts)







