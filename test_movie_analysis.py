import pandas as pd

from movie_analysis import calculate_average_gross_by_director

def test_calculate_average_gross():
    movie_data = pd.DataFrame({
        'movie_title': ['Movie1', 'Movie2', 'Movie3', 'Movie4'],
        'director': ['Director1', 'Director2', 'Director1', 'Director2'],
        'total_gross': [1000000, 2000000, 1500000, 2500000]
    })

    # Test for a director with movies
    result1 = calculate_average_gross_by_director(movie_data, 'Director1')
    assert result1 == 1250000.0, f"Test 1 failed. Result: {result1}"

    # Test for a director with no movies
    result2 = calculate_average_gross_by_director(movie_data, 'Director3')
    assert result2 is None, f"Test 2 failed. Result: {result2}"

if __name__ == '__main':
    try:
        test_calculate_average_gross()
        print("Success")
    except AssertionError as e:
        print("Some tests failed. Check the test results.")
        print(e)
