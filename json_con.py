import json

class file:
  @staticmethod
  def save_to_file(data, filename):
    with open(filename,'w') as file: #with statement makes sure the file is opened and closed properly even if an exception occurs
      json.dump(data, file, indent=4)# a function that converts lists or dictionaries into json file and dump it in a file
      #indent=4 means the json data will be a formatted with a indentation of 4 spaces, making it easier to read.
    print(f"data saved to {filename}")


  @staticmethod
  def load_from_file(filename):
    try: #exceptional handling
      with open(filename, 'r') as file:
        return json.load(file)
    except FileNotFoundError:
      print(f"file not found{filename}")
      return []
    except json.JSONDecodeError:
      print(f"There is an error decoding the json file structure at {filename}")
      return []
      