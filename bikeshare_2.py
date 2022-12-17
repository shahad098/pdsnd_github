import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
def Hello():
    print('Hello!')


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    print('Hello!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Enter the city (chicago, new york city, washington) : ')
    city = city.casefold()
    while city not in CITY_DATA:
        city = input('invalid input.try again')
        city = city.casefold()

    # get user input for month (all, january, february, ... , june)
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    month = input('Enter the month from January to June OR Enter "all : ')
    month = month.lower()
    while month not in months:
        month = input('invalid input. Please try again')
        month = month.lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = input('Enter the day  OR Enter "all" : ')
    day = day.casefold()
    while day not in days:
        day = input('invalid input. Please try again!')
        day = day.casefold()

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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    
    
    # name of the month to filter by, or "all" to apply no month filter
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        #define the month
        df = df[df['month'] == month]

        
        
    # week
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

        

    return df





def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0]
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    print('most common month:', months[common_month-1])

    # display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    common_day = df['day_of_week'].mode()[0]
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    print('most common day:', days[common_day])

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('most common start hour:', common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print(' most commonly used start station: ', df['Start Station'].mode()[0])


    # display most commonly used end station

    print('ost commonly used end station: ', df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip

    print('most frequent combination of start station and end station trip:',df.groupby(['Start Station', 'End Station']).size().nlargest(1))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("total travel time is equal =", df['Trip Duration'].sum())


    # display mean travel time
    print("mean travel time is equal =", df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    if 'Gender Year' in df.columns:

        user_type = df.groupby(['User Type'])['User Type'].count()
        print(user_type)

    # Display counts of gender
    if 'Gender Year' in df.columns:
        gender = df.groupby(['Gender'])['Gender'].count()
        print(gender)

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('earliest, most recent, and most common year of birth')
        print('earliest:', df['Birth Year'].min())
        print('recent:', df['Birth Year'].max())
        print('Most Common year of Birth:', df['Birth Year'].mode()[0])


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
        
        choose = ['yes','no']
        user_choose = input('want to see 5 lines of raw data,? Enter yes or no please.\n')
        
        while user_choose.lower() not in choose:
            user_choose = input('please Enter Yes or No:\n')
            user_choose = user_choose.lower()
        n = 0        
        while True :
            if user_choose.lower() == 'yes':
        
                print(df.iloc[n : n + 5])
                n += 5
                user_choose = input('\nWould you like to see more data? Enter yes or no please.\n')
                while user_choose.lower() not in choose:
                    user_choose = input('Enter yes or no please:\n')
                    user_choose = user_choose.lower()
            else:
                break  
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
