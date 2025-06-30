#Student id: w1823431

# Function to validate credit input
def get_credit_input(prompt):
    while True:
        try:
            credit = int(input(prompt))
            if credit in range(0, 121, 20):  # Must be one of {0, 20, 40, 60, 80, 100, 120}
                return credit
            else:
                print("Out of range. Please enter a value in {0, 20, 40, 60, 80, 100, 120}.")
        except ValueError:
            print("Integer required. Please enter a valid number.")

# Function to determine progression outcome
def determine_outcome(pass_credit, defer_credit, fail_credit):
    if pass_credit + defer_credit + fail_credit != 120:
        return "Total incorrect"
    elif pass_credit == 120:
        return "Progress"
    elif pass_credit == 100:
        return "Progress (module trailer)"
    elif fail_credit >= 80:
        return "Exclude"
    else:
        return "Do not progress - module retriever"

# Function to display a horizontal histogram
def display_horizontal_histogram(outcomes):
    print("\nHorizontal Histogram")
    for outcome, count in outcomes.items():
        print(f"{outcome} {count} : {'*' * count}")
    total_students = sum(outcomes.values())
    print(f"\n{total_students} outcomes in total")

# Function to display a vertical histogram
def display_vertical_histogram(outcomes):
    print("\nVertical Histogram")
    
    headers = ["Progress", "Progress (module trailer)", "Do not progress - module retriever", "Exclude"]
    counts = [outcomes.get(header, 0) for header in headers]

    # Print the headers
    print("  ".join(f"{header:^10}" for header in headers))  # Center the headers with fixed spacing

    # Find the maximum count to determine the number of rows needed
    max_count = max(counts)
    
    # Print each row of stars
    for i in range(max_count):
        row = ""
        for count in counts:
            if count > i:
                row += "  *  " # Add a star for this row
            else:
                row += "     " # Add spacing
        print(row)

# Main program
def main():
    # Dictionary to track progression outcomes
    outcomes = {
        "Progress": 0,
        "Progress (module trailer)": 0,
        "Do not progress - module retriever": 0,
        "Exclude": 0
    }
    
    while True:
        print("\nEnter credits for a student")
        pass_credit = get_credit_input("Please enter your credits at pass: ")
        defer_credit = get_credit_input("Please enter your credits at defer: ")
        fail_credit = get_credit_input("Please enter your credits at fail: ")

        outcome = determine_outcome(pass_credit, defer_credit, fail_credit)
        
        if outcome == "Total incorrect":
            print("Total incorrect. Please re-enter the data.")
            continue

        print(f"\n{outcome}")
        # Map the outcome to the correct key in the dictionary
        if outcome == "Progress":
            outcomes["Progress"] += 1
        elif outcome == "Trailer":
            outcomes["Trailing"] += 1
        elif outcome == "Retriever":
            outcomes["Retriever"] += 1
        elif outcome == "Excluded":
            outcomes ["Excluded"] += 1
        
        # Ask if user wants to continue or quit
        cont = input("\nWould you like to enter another set of data? (Enter 'y' for yes or 'q' to quit): ").strip().lower()
        if cont == 'q':
            break

    # Display both horizontal and vertical histograms after exiting the loop
    display_horizontal_histogram(outcomes)
    display_vertical_histogram(outcomes)

# Run the program
if __name__ == "__main__":
    main()
