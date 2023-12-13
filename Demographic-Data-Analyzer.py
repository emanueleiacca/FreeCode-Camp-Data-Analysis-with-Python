import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read the data from the CSV file
    df = pd.read_csv('C:/Users/39388/Downloads/adult.data.csv')

    # How many people of each race are represented in this dataset? 
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = df[df['sex'] == 'Male']['age'].mean()

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = (df[df['education'] == 'Bachelors'].shape[0] / df.shape[0]) * 100

    # What percentage of people with advanced education make more than 50K?
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    higher_education_rich = (higher_education[higher_education['salary'] == '>50K'].shape[0] / higher_education.shape[0]) * 100

    # What percentage of people without advanced education make more than 50K?
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education_rich = (lower_education[lower_education['salary'] == '>50K'].shape[0] / lower_education.shape[0]) * 100

    # What is the minimum number of hours a person works per week?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = (num_min_workers[num_min_workers['salary'] == '>50K'].shape[0] / num_min_workers.shape[0]) * 100

    # What country has the highest percentage of people that earn >50K and what is that percentage?
    highest_earning_country = df[df['salary'] == '>50K']['native-country'].value_counts().idxmax()
    highest_earning_percentage = (df[(df['native-country'] == highest_earning_country) & (df['salary'] == '>50K')].shape[0] / df[df['native-country'] == highest_earning_country].shape[0]) * 100

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()

    # Print the results if print_data is True
    if print_data:
        print("Number of each race:\n", race_count)
        print("\nAverage age of men:", round(average_age_men, 1))
        print("\nPercentage with Bachelors degrees:", round(percentage_bachelors, 1))
        print("\nPercentage with higher education that earn >50K:", round(higher_education_rich, 1))
        print("\nPercentage without higher education that earn >50K:", round(lower_education_rich, 1))
        print("\nMin work time:", min_work_hours)
        print("\nPercentage of rich among those who work fewest hours:", round(rich_percentage, 1))
        print("\nCountry with highest percentage of rich:", highest_earning_country)
        print("\nHighest percentage of rich people in country:", round(highest_earning_percentage, 1))
        print("\nTop occupations in India:", top_IN_occupation)

    # Return the calculated values as a dictionary
    return {
        'race_count': race_count,
        'average_age_men': round(average_age_men, 1),
        'percentage_bachelors': round(percentage_bachelors, 1),
        'higher_education_rich': round(higher_education_rich, 1),
        'lower_education_rich': round(lower_education_rich, 1),
        'min_work_hours': min_work_hours,
        'rich_percentage': round(rich_percentage, 1),
        'highest_earning_country': highest_earning_country,
        'highest_earning_percentage': round(highest_earning_percentage, 1),
        'top_IN_occupation': top_IN_occupation
    }

# Run the function to calculate and print the results
calculate_demographic_data()
