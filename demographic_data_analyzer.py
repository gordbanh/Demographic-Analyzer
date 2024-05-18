import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')
    
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    # race_series = pd.Series(df['race']) - Attempt #1
    # race_count = race_series.value_counts() - Attempt #1
    race_count = df['race'].value_counts()

    # What is the average age of men?
    # create a mask where "sex" column is equal to "Male"
    sex_mask = df['sex'] == 'Male'
    # find the mean age of men using the mask
    average_age_men = df[sex_mask].age.mean().round(1)

    # What is the percentage of people who have a Bachelor's degree?
    # create a mask where "education" column is equal to "Bachelor"
    bachelor_mask = df['education'] == 'Bachelors'
    # calculate the percentage of people who's education is equal to "Bachelor" compared to the total amount of people
    percentage_bachelors = (df[bachelor_mask].education.count() / df['education'].count() * 100).round(1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    # create a mask of "education" where it can be "Bachelor","Masters", or "Doctorate"
    higher_education_mask= (df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')
    # calculate the percentage of people who's education is "Bachelor", "Masters", or "Doctorate" compared to the total amount of people
    higher_education = (df[higher_education_mask].education.count() / df['education'].count() * 100).round(1)
    # calculate the percentage of people who's education is NOT "Bachelor", "Masters", or "Doctorate" compared to the total amount of people
    lower_education = (100 - higher_education).round(1)

    # percentage with salary >50K
    # create a mask of "education" where it can be "Bachelor","Masters", or "Doctorate" AND "salary" > 50K 
    higher_education_rich_mask = ((df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')) & (df['salary'] == ">50K") # Attempt #1
    # create a mask of "education" where it is NOT "Bachelor","Masters", or "Doctorate" AND "salary" > 50K 
    lower_education_rich_mask = ((df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate')) & (df['salary'] == ">50K")
    #higher_education_rich_mask = df['higher_education_mask'].loc['salary'] == ">50k" - Attempt #1 in optimization
    # calculate the percentage of people who's education is "Bachelor", "Masters", or "Doctorate" and make more than 50K compared to the total number of people who have a higher education 
    higher_education_rich = (df[higher_education_rich_mask].salary.count() / df[higher_education_mask].salary.count() * 100).round(1)
    # calculate the percentage of people who's education is not "Bachelor", "Masters", or "Doctorate" and make more than 50K compared to the total number of people who do not have a higher education 
    lower_education_rich = (df[lower_education_rich_mask].salary.count() / df[~higher_education_mask].salary.count() * 100).round(1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    # find minimum hours per week worked in dataframe
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    # create a mask of workers who work the minimum number of hours per week
    min_workers_mask = (df['hours-per-week'] == min_work_hours)
    # create a mask of workers who work the minimum number of hours per week and have a salary of >50K
    min_workers_rich_mask = (df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')
    # number of workers who work the minimum number of hours per week
    num_min_workers = df[min_workers_mask].salary.count()
    # calculate the percentage of workers who work the minimum number of hours per week and have a salary of >50K compared to the total number of people who work the minimum number of hours
    rich_percentage = (df[min_workers_rich_mask].salary.count() / df[min_workers_mask].salary.count() * 100).round(1)

    # What country has the highest percentage of people that earn >50K?
    # find the number of people who earn >50K by country
    # create a mask of people who earn >50K
    rich_mask = df['salary'] == '>50K'
    # find the unique value counts by country in the database and calculate the percentage to total population by country, find the max percentage index, and find the max percentage
    highest_earning_country = (df[rich_mask].get('native-country').value_counts() / df.get('native-country').value_counts() * 100).idxmax()
    highest_earning_country_percentage = (df[rich_mask].get('native-country').value_counts() / df.get('native-country').value_counts() * 100).max().round(1)

    # Identify the most popular occupation for those who earn >50K in India
    # create a mask for people in India who earn >50k
    india_rich_mask = (df['salary'] == '>50K') & (df['native-country'] == 'India')
    # find the unique value counts in India who earn >50K, find the max index
    top_IN_occupation = df[india_rich_mask].get('occupation').value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

calculate_demographic_data()