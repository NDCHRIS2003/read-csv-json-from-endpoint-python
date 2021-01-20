"""
    Author : Ndubuisi Christopher Okpala

    Purpose of the project:    
        This program is written to read data from an API endpoint in json format. The data will be read
        and the content will be stored in json format and csv format. Then the content of the data will 
        be displayed in the console.

    How to execute the python script: python glossary.py
    Ensure that you have python 3 installed in your system
"""

# import the needed modules
import urllib.request as request
import json
import csv
import io


def retrieveDataFromApi(url):
    """ 
    This function will make a request call to a given API endpoint and retrieve data in json format.
    It also contain error handler based on the API call made.
    """
    with request.urlopen(url) as response:
        # this will check if the call to API returns 200 ok else output error message to the user.
        if response.getcode() == 200:
            source = response.read()
            dataset = json.loads(source)
        else:
            print(
                "Please check the url. An error occured while retrieving data from the API")
    return dataset


def saveDataAsJson(jsonFileName, data):
    """
    This function will take a json file name and a json data passed to it, write it and save the data in 
    json format with the given file name
    """
    with open(jsonFileName, "w") as json_file:
        json.dump(data, json_file, indent=4, sort_keys=True)


def saveDataAsCsv(jsonFileName, csvFileName):
    """
    This function will take a json data and a csv file name. It will convert the given json data to csv
    and save it based on the given csv name provided
    """

    with open(jsonFileName, "r") as json_file:
        data = json.load(json_file)
        name_glossary = data["glossary"]
        with io.open(csvFileName, "w", encoding="utf-8", newline='') as csv_file:
            # state the headers of the csv file and this header must be content of the dictionary
            headers = ['term', 'definition']
            csv_writer = csv.DictWriter(
                csv_file, fieldnames=headers, delimiter=',')
            # call the header so as to ensure it appear on the header of the csv
            csv_writer.writeheader()
            csv_writer.writerows(name_glossary)


def printGlossary(fileName):
    """
    This function will read csv file and output the content in a console
    """
    with io.open(fileName, "r", encoding="utf-8", newline='') as csvFile:
        reader = csv.DictReader(csvFile)
        headers = "term           definition"
        print(headers)
        for row in reader:
            print(f"{row['term']}   {row['definition']}")

# --------------------------------------main function----------------------------------------------


def main():
    # define the url endpoint to read data from
    url = "https://api.weather.gov/glossary"
    data = retrieveDataFromApi(url)

    # define the file names to store data in json and csv format
    jsonFileName = "glossary.json"
    csvFileName = "glossary.csv"

    # provide arguments to the defined functions
    saveDataAsJson(jsonFileName, data)
    saveDataAsCsv(jsonFileName, csvFileName)

    # out put the content of the data in the console
    printGlossary(csvFileName)


if __name__ == "__main__":
    main()
