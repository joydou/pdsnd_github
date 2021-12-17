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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Would you like to see data for Chicago, New York, or Washington?").lower()
   
    while city not in ["chicago", "new york", "washington"]:
        print("Invalid input!")
        city = input("Please enter the right name of the City: ").lower()    
    
    if city =="new york":
        city = "new york city"
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Which month - January, February, March, April, May, or June(or type all for all the months)?").lower()
    
    while month not in ["january", "february", "march", "april", "may", "june","all"]:
        print("Invalid input!")
        month = input("Please enter the right month: ").lower()          
    
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday(or type all for all the days of week)?").lower()
    
    while day not in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"]:
        print("Invalid input!")
        day = input("Please enter the day of a week: ").lower()   

    print('-'*40)
    return city, month, day    

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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
   # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]
        
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]        
    
    df['combination'] = df['Start Station'] + " - - - " + df['End Station']
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    monthlist = ["January", "February", "March", "April", "May", "June"]
    print('Most common month: ', monthlist[popular_month-1])

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most common day of week: ', popular_day)

    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('Most common hour: ', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start = df['Start Station'].mode()[0]
    print('Most commonly used start station: ', popular_start)
    # TO DO: display most commonly used end station
    popular_end = df['End Station'].mode()[0]
    print('Most commonly used end station: ', popular_end)

    # TO DO: display most frequent combination of start station and end station trip
    popular_combi = df['combination'].mode()[0]
    print('Most commonly used combination of start station and end station trip: ', popular_combi)    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum() 
    print("Total travel time: ", modify_time(total_time))

    # TO DO: display mean travel time
    mean_time = int(df['Trip Duration'].mean())
    print("Average travel time: ", modify_time(mean_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def modify_time(time_ss):
    """Change the time in second to hhmmss"""
    ss = time_ss%60;
    hh = time_ss//3600;
    mm = time_ss%3600//60;
    
    if hh < 1:
        time_hhmmss = str(mm)+ "min" + str(ss) + "s"
    else:
        time_hhmmss = str(hh) + "hour" + str(mm) + "min" + str(ss) + "s"
    return time_hhmmss

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Counts of each user type: ")
    print(user_types)

    # TO DO: Display counts of gender
    gender = df['Gender'].value_counts()
    print("\nCounts of gender: ")  
    print(gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    year_earliest = int(df['Birth Year'].min())
    year_recent = int(df['Birth Year'].max())
    year_common = int(df['Birth Year'].mode()[0])
    print("\nEarliest year of birth: ", year_earliest)
    print("Most recent year of birth: ", year_recent)
    print("Most common year of birth: ", year_common)
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def read_raw_data(city):
    """Displays 5 lines of raw data"""
    
    read_data = input('\nWould you like to see 5 lines of raw data? Enter yes or no.\n').lower()        
    while read_data not in ["yes","no"]:
       print("Invalid input!")
       read_data = input("Please enter yes or no: ").lower()
     
    line = 0
    df_raw = pd.read_csv(CITY_DATA[city])    
    while read_data == "yes" and line < len(df_raw.index): 
        print(df_raw.iloc[line : line + 5])
        line += 5
        read_data = input('\nWould you like to see another 5 lines of raw data? Enter yes or no.\n').lower()
        while read_data not in ["yes","no"]:
            print("Invalid input!")
            read_data = input("Please enter yes or no: ").lower()            
    if line >= len(df_raw.index):
        print("End of the file! There is no more raw data to display1")
        

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        read_raw_data(city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
