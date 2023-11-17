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
    valid_cities= ['chicago', 'new york city', 'washington']
    city=input("Please input the name of city(chicago, new york city, washington)").lower()
    while city not in valid_cities:
       print("Invalid input. Please try again.")
       city = input("Please enter a valid city name: ").lower() 


    # TO DO: get user input for month (all, january, february, ... , june)
    valid_month=["all","january", "february", "march", "april", "may", "june"]
    month = input("Enter the month (all, January, February, ..., June): ").lower()
    # Check the user's input
    if month not in valid_month:
        print("Invalid input. Please try again.")
        month = input("Please enter a valid month: ").lower()
    


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    valid_day=["all","monday", "tuesday", "wednesday", "thursday", "firday", "saturday","sunday"]
    day= input("Enter the day of week (all, monday, tuesday, ... sunday): ").lower()
    if day not in valid_day:
        print("Invalid input. Please try again.")
        day = input("Please enter a valid day: ").lower()
 



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

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

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
        df = df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    # Find the most common month
    common_month = df['month'].value_counts().idxmax()
    print('The most common month:', common_month)



    # TO DO: display the most common day of week
      # Extract the day of the week from the 'Start Time' column
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # Find the most common day of the week
    common_day = df['day_of_week'].value_counts().idxmax()

    print('The most common day of the week:', common_day)


    # TO DO: display the most common start hour
    df['start_hour'] = df['Start Time'].dt.hour

    # Find the most common day of the week
    common_start_hour = df['start_hour'].value_counts().idxmax()

    print('The most common start_hour:', common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station:', common_start_station)
    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station:', common_end_station)
    # TO DO: display most frequent combination of start station and end station trip
    df['Station Combination'] = df['Start Station'] + ' to ' + df['End Station']
    # Find the most frequent combination of start station and end station
    common_station_combination = df['Station Combination'].mode()[0]
    print('The most frequent combination of start station and end station:', common_station_combination)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = np.sum(df['Trip Duration'])
    def convert_seconds_to_time(seconds):
    
        hours = round(seconds // 3600,1)
        minutes = round((seconds % 3600) // 60,1)
        seconds = round((seconds % 3600) % 60,1)
        return hours,minutes,seconds
    total_travel_time = convert_seconds_to_time(total_travel_time)
    print('Total travel time:', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = np.mean(df['Trip Duration'])

    # Convert mean travel time to appropriate units (e.g., minutes, seconds)
    mean_travel_time = convert_seconds_to_time(mean_travel_time)
    print('Mean travel time:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_counts = df['User Type'].value_counts()
    print('Counts of User Types:')
    for user_type, count in user_counts.items():
        print(f'{user_type}: {count}')

    # TO DO: Display counts of gender
  
    try:
        gender_counts = df['Gender'].value_counts()
        print('Counts of Gender:') 
        for gender, count in gender_counts.items():
            print(f'{gender}: {count}')
    except KeyError:
         print("\nGender data is not available for this city.")


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year = df['Birth Year'].min()
        most_recent_birth_year = df['Birth Year'].max()
        most_common_birth_year = df['Birth Year'].mode()[0]

        print('Earliest Birth Year:', int(earliest_birth_year))
        print('Most Recent Birth Year:', int(most_recent_birth_year))
        print('Most Common Birth Year:', int(most_common_birth_year))
    except KeyError:
        print("\nBirth Year is not available for this city.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        def display_raw_data(df):
         """
        Prompts the user to see raw data and displays it in batches of 5 rows at a time.

         Args:
            df (DataFrame): Pandas DataFrame containing city data.
        """
        i = 0
        raw = input("\nWould you like to see 5 lines of raw data? Enter 'yes' or 'no': ").lower()

        while True:
            if raw == 'no':
                break
            elif raw == 'yes':
                print(df[i:i+5])
                i += 5
                raw = input("\nWould you like to see 5 more lines of raw data? Enter 'yes' or 'no': ").lower()
            else:
                raw = input("\nYour input is invalid. Please enter only 'yes' or 'no': ").lower()



        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
