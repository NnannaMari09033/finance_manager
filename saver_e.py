#storng the data in a json file(javascript object notation)
import json 
import os  


class event:
 
  @staticmethod
  def save_to_file(data,socials):
    with open(socials,'w') as file: #with statement makes sure the file is opened and closed properly even if an exception occurs
      json.dump(data, file, indent=4)# a function that converts lists or dictionaries into json file and dump it in a file
      #indent=4 means the json data will be a formatted with a indentation of 4 spaces, making it easier to read.
    print(f"data saved to {socials}")

  @staticmethod
  def load_from_file(socials):
    try: #execptional handling
      with open(socials, 'r'):
       return json.load(socials)
    except FileNotFoundError:
      print("file not found")
      return []
    except json.JSONDecodeError:
      print(f"there's an error decoding the json structure{socials}")
      return []
    
  @staticmethod
  def delete_from_file(data):
    os.remove(data)

  
    
      
       
