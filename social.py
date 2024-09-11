from saver_e import event
class SocialEventOrganizer(event):
    def __init__(self):
        self.event_manager = self.load_from_file('another_store/event.json')
        print("Welcome to Mari's Event Planning Website!")

    def view(self):
        if len(self.event_manager) == 0:
            print("Sorry, there's nothing here!")
        else:
            for event in self.event_manager:
                print("========")
                print(f"Title: {event['title']}")
                print(f"Name: {event['name']}")
                print(f"Age: {event['age']}")
                print(f"Gender: {event['gender']}")
                print(f"Date: {event['date']}")
                print(f"Location: {event['location']}")
                print(f"Maximum Number of Attendees: {event['max_attendees']}")
                print("========")

    def searching(self):
        event_title = input("Enter the name of the event you want to search for: ")
        found = False
        for event in self.event_manager:
            if event['title'] == event_title:
                print("=======")
                print(f"Title: {event['title']}")
                print(f"Name: {event['name']}")
                print(f"Age: {event['age']}")
                print(f"Gender: {event['gender']}")
                print(f"Date: {event['date']}")
                print(f"Location: {event['location']}")
                print(f"Maximum Number of Attendees: {event['max_attendees']}")
                print("=======")
                found = True
                break
        if not found:
            print("Event not found!")

    def user_choice(self):
        while True:
            command = input("Enter 'c' to create an event, 'cancel' to cancel an event, 'v' to view events, 's' to search event by title, 'e' to exit: ")
            if command == "c":
                event_title = input("Enter the event title: ")
                organizer_name = input("Enter the organizer's name: ")
                organizer_age = int(input("Enter the organizer's age: "))
                organizer_gender = input("Enter the organizer's gender (M/F): ")
                event_date = input("Enter the event date (yyyy-mm-dd): ")
                event_location = input("Enter the event location: ")
                maximum_num_of_attendees = int(input("Enter the maximum number of attendees: "))
                self.event_manager.append({
                    "title": event_title,
                    "name": organizer_name,
                    "age": organizer_age,
                    "gender": organizer_gender,
                    "date": event_date,
                    "location": event_location,
                    "max_attendees": maximum_num_of_attendees
                })
                self.save_to_file(self.event_manager,'another_store/event.json')
                print("Congratulations! You have successfully created an event!")

            elif command == "cancel":
                event_title = input("Enter the title of the event you want to cancel: ")
                event_to_remove = None
                for event in self.event_manager:
                    if event["title"] == event_title:
                        event_to_remove = event
                        break
                if event_to_remove:
                    self.event_manager.remove(event_to_remove)
                    print("Event canceled successfully!")
                else:
                    print("Event not found!")

            elif command == "v":
                self.view()

            elif command == "s":
                self.searching()

            elif command == "e":
                break

            else:
                print("Invalid command! Please try again.")

# Usage
ma = SocialEventOrganizer()
ma.user_choice()