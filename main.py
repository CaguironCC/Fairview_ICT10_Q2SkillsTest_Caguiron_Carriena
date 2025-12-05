from pyscript import document

# Dictionary of club information
clubs_data = {
    "glee": {
        "name": "GLEE Club",
        "description": "A choral group that performs at school events.",
        "meeting_time": "Monday 03:00-05:00 PM",
        "location": "High School Music Room",
        "moderator": "Mr. Denver Martin",
        "category": "Non-academic"
    },
    "dance": {
        "name": "DANCE CLUB",
        "description": "Learn various dance styles and perform at school events.",
        "meeting_time": "Tuesday 03:00-05:00 PM",
        "location": "Teatro Preciosa",
        "moderator": "Mr. Alfred Cases",
        "category": "Non-academic"
    },
    "math": {
        "name": "MATH CLUB",
        "description": "Engage in mathematical problem solving and prepare for competitions.",
        "meeting_time": "Monday 02:30-03:00 PM",
        "location": "Room 404",
        "moderator": "Mr. Nicole Gabuya",
        "category": "Academic"
    },
    "communications": {
        "name": "COMMUNICATION ARTS CLUB",
        "description": "Develop skills in public speaking, debate, and media communication.",
        "meeting_time": "Wednesday 03:00-04:00 PM, Friday 03:00-04:00 PM",
        "location": "Room 406",
        "moderator": "Ms. Yannis Fernandez",
        "category": "Academic"
    },
    "social": {
        "name": "SOCIAL SCIENCE CLUB",
        "description": "Discuss and explore topics in history, geography, and social sciences.",
        "meeting_time": "Tuesday 03:00-04:00 PM",
        "location": "Room 409",
        "moderator": "Mr. Roberto Lim",
        "category": "Academic"
    },
    "volleyball": {
        "name": "VOLLEYBALL VARSITY",
        "description": "Competitive volleyball team representing the school in tournaments.",
        "meeting_time": "Wednesday 03:00-04:00 PM",
        "location": "Quadrangle",
        "moderator": "Mr. Adrian Ruiz",
        "category": "Non-academic"
    }
}

def display_club_info(e=None):
    """
    Display information for the selected club.
    This function retrieves the selected club from the dropdown
    and displays its information in the message area.
    """
    try:
        # Get the selected club value from the dropdown
        club_select = document.getElementById("clubs")
        selected_value = club_select.value
        
        if not selected_value:
            # If no club is selected
            message_div = document.getElementById("message")
            message_div.innerHTML = "<strong>Please select a club from the dropdown menu.</strong>"
            return
        
        # Get club data from the dictionary
        club = clubs_data.get(selected_value)
        
        if club:
            # Format the club information
            club_info = f"""
            {club['name']}
            \t• Description: {club['description']}
            \t• Meeting Time: {club['meeting_time']}
            \t• Location: {club['location']}
            \t• Moderator/Advisor: {club['moderator']}
            \t• Category: {club['category']}
            """
            
            # Display the information
            message_div = document.getElementById("message")
            message_div.innerHTML = club_info
        else:
            message_div = document.getElementById("message")
            message_div.innerHTML = "<strong>Club information not found.</strong>"
    
    except Exception as error:
        # Handle any errors
        message_div = document.getElementById("message")
        message_div.innerHTML = f"<strong>Error loading club information:</strong> {str(error)}"

# Initialize by setting up an event listener
def setup():
    """
    Initialize the application.
    This function sets up the event listener for the button.
    """
    try:
        # Get the button element
        button = document.getElementById("get-info-btn")
        
        # Set the button click handler
        button.onclick = display_club_info
        
        # Initial message
        message_div = document.getElementById("message")
        message_div.innerHTML = "<strong>Select a club to see information here...</strong>"
    
    except Exception as error:
        print(f"Setup error: {error}")
