"""
    CS5001
    Spring 2022
    Homework 6: Hyperspace BnB
    Katie Davenport

    This program manages guest reservations and bookings on Hyperspace BnB. 
"""

CREDIT_PER_TRIP = 500
RESERVATIONS_PER_WEEK = 1
OUTPUT_FILE = 'bookings.txt'

def load_travelers(travelers_file_name): 
    """
    Function: load_travelers
    Parameter: travelers_file_name (str) - name of file that includes traveler
        information
    Returns: travelers (list) - a list containing traveler information 
    Does: Extracts information from a file and into a nested list.
    """

    travelers = []
    try:
        with open(travelers_file_name, "r") as traveler_file:
            for each in traveler_file:
                if each.count('@') == 2: 
                    traveler = []
                    traveler = each.split('@')
                    if len(traveler[0]) > 0 and len(traveler[1]) > 0 \
                       and len(traveler[2]) > 0: 
                        traveler[2] = traveler[2].strip()
                        travelers.append(traveler)
    except IOError:
        print("A file error occurred.")
    return travelers  
        
def load_requests(request_file_name):
    """
    Function: load_requests
    Parameter: request_file_name (str) - name of file that includes requests
    Returns: requests (list) - contains requests  
    Does: Read in request file and create a nested list. 
    """

    requests = []
    try:
        with open(request_file_name, "r") as request_file:
            for each in request_file:
                request = []
                request = each.split()
                if (len(request)) == 2: 
                    traveler_id = request[0]
                    requests.append(request)
    except IOError:
        print("A file error occurred.")
    return requests 
    
def save_file(reservations):
    """
    Function: save_file
    Parameters: reservations (list) - a list of reservations 
    Returns: None
    Does: Reformats the reservations and saves them to a txt file. 
    """  
    # Format lines for printout.
    if len(reservations) > 0: 
        bookings = []
        for each in reservations:
            line = (each[1] + ' - ' + each[0] + ' - ' + each[5] + '\n')
            bookings.append(line)     

        # Write the file.
        try:
            with open(OUTPUT_FILE, "w") as output_file:
                for line in bookings:
                    output_file.write(line)
        except IOError:
            print("A file error occurred")
        else:
            print("Finished processing reservations. Beam us up Scottie!")
    else:
        print("There are no reservations to process.")    
            

def process_requests(travelers, request_file_name):
    """
    Function: process_requests
    Parameters:
        travelers (list) - traveler information
        request_file_name (str) - name of file containing reservation requests
    Returns:  None 
    Does: Processes reservations and write them to a file named bookings.txt.

    Business logic:
    - Do not book a reservation if the week has already been reserved.
    - Each booking is 500 credits.
    - Do not book a reservation if the alien does not have enough credits.
    """

    # Read in the request file and create a nested list of requests.
    requests = load_requests(request_file_name)

    # Process requests.
    weeks = []
    traveler_list = []
    reservations = []

    # Create traveler id list.
    traveler_id_list = []
    for traveler in travelers:
        traveler_id_list.append(traveler[1])

    if(len(requests)) > 0: 
        for request in requests:
            if request[0] in traveler_id_list: 
                # Append count of requests per week for logic. 
                weeks.append(request[1])
                request.append(weeks.count(request[1]))

                # Append count of requests per traveler for logic.
                traveler_list.append(request[0])
                request.append(traveler_list.count(request[0]))

                # Append traveler credits for logic.
                # Append traveler name for requested printout format. 
                for traveler in travelers:
                    if request[0] == traveler[1]:
                        request.append(int(traveler[2]))
                        request.append(traveler[0])

                # Process reservations according to business logic.
                if (request[2] <= RESERVATIONS_PER_WEEK) and \
                   ((request[3] * CREDIT_PER_TRIP) <= request[4]):
                    reservations.append(request)
            else:
                print("We do not have information for this traveler.")

        # Save file. 
        save_file(reservations)    
  
def main():
    
    process_requests(load_travelers('travelers.txt'), 'requests.txt')
     
if __name__ == "__main__":
    main()
