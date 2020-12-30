import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv', 'new york city': 'new_york_city.csv', 'washington': 'washington.csv' }

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
    
    input_city = input("What city would you like to filter by? Chicago, New York City or Washington?\n").lower()
	#While loop till we get valid city.
    while input_city not in CITY_DATA:
        print("Please enter a valid city \n")
        print(CITY_DATA.keys())
        input_city = input('Enter a valid city.\n').lower()

# TO DO: get user input for month (all, january, february, ... , june)

    months = ['january', 'february', 'march', 'april', 'may', 'june']
    month = input("Which month would you like to filter by?\n")
    while month.lower() not in months:
        print("You have entered an invalid month")
        print(months)
        month = input('Please enter a valid month \n')

# TO DO: get user input for day of week (all, monday, tuesday, ... sunday)    
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = input('Which day would you like to filter by?\n')
    while day.lower() not in days:
        print("You have entered an invalid day")
        print(days)
        day = input('Please enter a valid day\n')
        print('-' * 40)
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
    df['day_of_week'] = df['Start Time'].dt.day_name
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
        """
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('the most common month is:{}.\n'.format(common_month))
    
    # TO DO: display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    print('the most common day is:{}.\n'.format(common_day_of_week))
    
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('the most common start hour of a day is:{}.\n'.format(common_hour))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    # TO DO: display most commonly used start station
    count_start_station = df.groupby(['Start Station']).size().sort_values(ascending=False).index[0]
    print('The most common Start Station: {}.\n'.format(count_start_station))

    # TO DO: display most commonly used end station
    counts_end_station = df.groupby(['End Station']).size().sort_values(ascending = False).index[0]
    print('The most common End Station: {}.\n'.format(counts_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    popular_station_combination = df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print('The most common Start and End Station combination: {}.\n'.format(popular_station_combination))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is: {}.\n'.format(total_travel_time))

    # TO DO: display mean travel time
    avg_travel_time = df['Trip Duration'].mean()
    print('The average travel time is: {}.\n'.format(avg_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def user_stats(df):
    """"Displays statistics on bikeshare users.
    Args:
        (DataFrame) df- Pandas DataFrame containing city data filtered by month and day
    
    Prints
        count of user type
        count of gender
        year of birth of older user
        year of birth of youngest user
        most common year of birth.
    """
    print('\nCalculating User Stats...\n')
    start_time = time.time()
   
    # TO DO: Display counts of user types
    print('Breakdown of User Types:')
    users = df['User Type'].value_counts()
    print(users)

# TO DO: Display counts of gender
    try:
        print('\nBreakdown of Gender:')
        gender = df['Gender'].value_counts()
        print(gender)
    except:
        print('The city you selected has not gender data.')
        
# TO DO: Display earliest, most recent, and most common year of birth
    try:
        print('\nStatistics pertaining to year of birth:')
        oldest = np.min(df['Birth Year'])
        youngest = np.max(df['Birth Year'])
        pop_year = df['Birth Year'].mode()[0]
        print('Oldest:', oldest)
        print('Youngest:', youngest)
        print('Most Popular:', pop_year)
    except:
        print('No birth year data to share.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def display_raw_data(df):
    i = 0
    raw = input("\nWould you like to see the first 5 rows of raw data? Type 'yes' or 'no'\n").lower()
    pd.set_option('display.max_columns',200)
    while True:
        if raw not in ['yes', 'no']:
            print("Incorrect response. Please try again!")
            raw = input("\nWould you like to see first 5 rows of raw data? Type 'yes' or 'no'\n").lower()
        continue
        print(df[i:i+5])
        raw = input('\nWould you like to see next rows of raw data?\n').lower()
        i += 5

print('-'*40)

   
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
            
if __name__ == "__main__":
    main()