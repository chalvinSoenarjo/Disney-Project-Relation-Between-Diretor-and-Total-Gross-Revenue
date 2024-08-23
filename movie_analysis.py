import pandas as pd

def calculate_average_gross_by_director(movie_data, director_name):
    """
    Calculate the average gross revenue for movies directed by a specific director.

    Args:
    - movie_data (DataFrame): A DataFrame containing movie data, including 'director' and 'total_gross' columns.
    - director_name (str): The name of the director to filter and calculate the average gross for.

    Returns:
    - float: The average gross revenue for movies directed by the specified director.
    """
    try:
        # Filter the DataFrame to include only movies directed by the specified director
        director_movies = movie_data[movie_data['director'] == director_name]

        # Calculate the average gross revenue for the director's movies
        average_gross = director_movies['total_gross'].mean()

        return average_gross
    except Exception as e:
        raise ValueError(f"Error calculating average gross: {str(e)}")

# Unit tests for the calculate_average_gross_by_director function
def test_calculate_average_gross():
    movie_data = pd.DataFrame({
        'movie_title': ['Movie1', 'Movie2', 'Movie3', 'Movie4'],
        'director': ['Director1', 'Director2', 'Director1', 'Director2'],
        'total_gross': [1000000, 2000000, 1500000, 2500000]
    })

    # Test for a director with movies
    assert calculate_average_gross_by_director(movie_data, 'Director1') == 1250000.0

    # Test for a director with no movies
    assert calculate_average_gross_by_director(movie_data, 'Director3') == 0.0

if __name__ == '__main__':
    test_calculate_average_gross()
    print("All tests passed.")
