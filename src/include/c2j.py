import sys, os
import csv
import json
import codecs
import StringIO


def get_json_from_csv(csv_data, delimiter=','):
    """ 
    Use this function to convert csv to json within a program (no reading/writing files)

    Input:  csv formated string
            delimiter - sometimes you will find csv that is formated with alternate delimiters
                        common examples include: | \t ; : 
                        use this optional perameter if you are dealing with csv that is 
                        delimited with anyting other than a comma
    Output: json
    """

    # temporarily write csv to a file
    f = open('csvfile', 'w')
    f.write(csv_data)
    f.close()
    f = open('csvfile')

    # parse csv
    with f as csvfile:
        csv.register_dialect('dialect', delimiter=delimiter)
        readCSV = csv.reader(csvfile, dialect='dialect')

        try:
            json_data = []
            rows = []
            headers = next(readCSV)
            for row in readCSV:
                d = dict()
                for i, header in enumerate(headers):
                    d[header] = row[i]
                json_data.append(d)
        except (UnicodeDecodeError, UnicodeEncodeError):
            print >> sys.stderr, "CSV Format Error"
            pass

    # destroy temporary file
    f.close()
    os.remove(os.getcwd() + '/csvfile')


    return json_data
