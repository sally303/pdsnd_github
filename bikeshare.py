## this file is brought from Project 2. 

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    done_choice_city = False
    
    while not done_choice_city :
       print('Would you like to see data for Chicago, New York, or Washington?')
       user_city_input = input()
       user_city_input_l = user_city_input.lower()
    
       if user_city_input_l == 'chicago' or user_city_input_l == 'new york' or user_city_input_l == 'washington' :
           done_choice_city =  True
           
    city = user_city_input_l
    
    
    ##  Ask user ,, Would you like to filter the data by month, day, or not at all?
    done_choice_filter = False
    
    while not done_choice_filter :
        print('Would you like to filter the data by month, day, both or not at all? Type "none" for no time filter.')
        user_filter_input = input()
        user_filter_input_l = user_filter_input.lower()
        
        match user_filter_input_l:
            case "month":
                month = enter_month()
                day = ''
                done_choice_filter =  True
                
            case "day":
                month = ''
                day = enter_day()
                done_choice_filter =  True
                
            case "both":
                month = enter_month()
                day = enter_day()
                done_choice_filter =  True
                
            case "none":
                print("You choose no time filter")
                month = ''
                day = ''
                done_choice_filter =  True
                
            case _:
                done_choice_filter =  False
                
    
    print('-'*40)
    return city, month, day


def enter_month():
    # get user input for month (all, january, february, ... , june)  
    done_choice_month = False
    
    while not done_choice_month :
        print('Which month? January, February, March, April, May, or June?')
        user_month_input = input()
        user_month_input_l = user_month_input.lower()
    
        if user_month_input_l == 'january' or user_month_input_l == 'february' or user_month_input_l == 'march' or user_month_input_l == 'april' or user_month_input_l == 'may' or user_month_input_l == 'june':
            done_choice_month =  True
    
    return user_month_input_l    
        
    


def enter_day():
    # get user input for day of week (all, monday, tuesday, ... sunday)
    done_choice_day = False
    
    while not done_choice_day :
        #print('Which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?')
        print('Which day? Please type your response as an integer (e.g., 1=Sunday).')
        user_day_input = input()
        user_day_input_int = int(user_day_input)
        
        match user_day_input_int:
            case 1:
                user_day_input_str = 'Sunday'
                done_choice_day =  True
                
            case 2:
                user_day_input_str = 'Monday'
                done_choice_day =  True
            
            case 3:
                user_day_input_str = 'Tuesday'
                done_choice_day =  True
                
            case 4:
                user_day_input_str = 'Wednesday'
                done_choice_day =  True
            
            case 5:
                user_day_input_str = 'Thursday'
                done_choice_day =  True
                
            case 6:
                user_day_input_str = 'Friday'
                done_choice_day =  True
                
            case '7':
                user_day_input_str = 'Saturday'
                done_choice_day =  True
                
            case _:
                done_choice_day =  False
        
    return user_day_input_str
    
    
    
    
    
    

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    
    CITY_DATA = { 
                    'chicago'       : 'chicago.csv',
                    'new york city' : 'new_york_city.csv',
                    'washington'    : 'washington.csv' 
                }


    if city == 'chicago' :
        file_name='chicago.csv'
    elif city == 'new york' :
        file_name='new_york_city.csv'
    elif city =='washington' :
        file_name='washington.csv'
    else : 
        file_name = ''
    
    if file_name != '' :
        df = pd.read_csv(file_name)
        print('file' , file_name , ' type:', type(df))
        print('file' , file_name , ' has shape:', df.shape)
        
        columns= df[['Start Time', 'End Time', 'Trip Duration', 'Start Station', 'End Station', 'User Type']]

        
        #df.get(["Start Time", "End Time", "Trip Duration", "Start Station","End Station", "User Type"])
'''        
        if month !='' and day !='':
            print(columns.head())
        elif month !='' and day =='':
            print(12)
        elif month =='' and day !='':
            print(34)
        else :
            print(columns.head())
'''
    exit()
    df = 8
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month


    # display the most common day of week


    # display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station


    # display most commonly used end station


    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time


    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    print("WELCOME TO SALLY's BIKESHARE!")
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
