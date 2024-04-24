 Define the survey data structure
survey_data = {
    "District1": {
        "Mandal1": {
            "Village1": ["Survey1", "Survey2", "Survey3"],
            "Village2": ["Survey4", "Survey5"]
        },
        "Mandal2": {
            "Village3": ["Survey6", "Survey7"],
            "Village4": ["Survey8", "Survey9", "Survey10"]
        }
    },
    "District2": {
        "Mandal3": {
            "Village5": ["Survey11", "Survey12", "Survey13"]
        },
        "Mandal4": {
            "Village6": ["Survey14"]
        }
    }
}

# Function to get survey numbers
def get_survey_numbers(district, mandal, village):
    try:
        surveys = survey_data[district][mandal][village]
        print("Survey numbers for {}, {}, {}: {}".format(district, mandal, village, surveys))
    except KeyError:
        print("Invalid district, mandal, or village combination.")

# Example usage
get_survey_numbers("District1", "Mandal1", "Village1")
get_survey_numbers("District2", "Mandal4", "Village6")
get_survey_numbers("District3", "Mandal1", "Village1")  # Invalid combination

