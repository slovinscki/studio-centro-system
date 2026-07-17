#Split the service in 2 categories: Session OR Event
def ask_service_category():
    valid_categories = ["session", "event"]

    service_category = input(
        "Choose session or event: "
    ).strip().lower()

    while service_category not in valid_categories:
        print("Invalid category. Please enter session or event.")

        service_category = input(
            "Choose session or event: "
        ).strip().lower()

    return service_category

#Customers in advanced pregnancy (32 weeks) should be consulted by GP prior to session  
def collect_pregnancy_information():
    while True:
        pregnancy_week_input = input(
            "Enter the current pregnancy week: "
        ).strip()

        if not pregnancy_week_input.isdigit():
            print("Invalid value. Please enter a whole number.")
            continue

        pregnancy_week = int(pregnancy_week_input)

        if pregnancy_week < 1 or pregnancy_week > 42:
            print("Invalid pregnancy week. Enter a value from 1 to 42.")
            continue

        break

    pregnancy_information = {
        "pregnancy_week": pregnancy_week,
        "recommended_period": 28 <= pregnancy_week <= 32,
        "requires_operator_decision": pregnancy_week > 32,
    }

    if pregnancy_week < 28:
        print(
            "Notice: the ideal period for a maternity session "
            "is between 28 and 32 weeks."
        )

    elif pregnancy_week <= 32:
        print("The customer is within the ideal maternity session period.")

    else:
        print(
            "Warning: the customer is above the studio's recommended "
            "limit of 32 weeks."
        )

        decision = input(
            "Does the operator approve this scheduling exception? "
            "(yes/no): "
        ).strip().lower()

        while decision not in ["yes", "no"]:
            print("Invalid answer. Please enter yes or no.")

            decision = input(
                "Does the operator approve this scheduling exception? "
                "(yes/no): "
            ).strip().lower()

        pregnancy_information["scheduling_exception_approved"] = (
            decision == "yes"
        )

    return pregnancy_information


def collect_session_information():
    valid_session_types = [
        "maternity",
        "corporate",
        "fifteenth_birthday",
        "couple",
        "family",
        "female_portrait",
        "birthday",
    ]

    session_type = input(
        "Enter the session type: "
    ).strip().lower()

    while session_type not in valid_session_types:
        print("Invalid session type. Please try again.")

        session_type = input(
            "Enter the session type: "
        ).strip().lower()

    session_information = {
        "service_category": "session",
        "session_type": session_type,
    }

    if session_type == "maternity":
        pregnancy_information = collect_pregnancy_information()
        session_information.update(pregnancy_information)

    location_required_session_types = [
        "corporate",
        "couple",
        "family",
        "female_portrait",
    ]

    if session_type in location_required_session_types:
        location = input(
            "Enter the desired session location: "
        ).strip()

        while not location:
            print("Location cannot be empty.")

            location = input(
                "Enter the desired session location: "
            ).strip()

        session_information["location"] = location

    return session_information


def main():
    selected_category = ask_service_category()
    print("Selected category:", selected_category)

    if selected_category == "session":
        inquiry = collect_session_information()
        print("Collected information:", inquiry)

    elif selected_category == "event":
        print("Event collection has not been implemented yet.")
        
# Day two: session location collection added.
main()
