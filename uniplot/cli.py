import argparse
from os import path
from uniplot import plot

from . import parse
from . import analysis

file = open("location.txt", "r")
LOC = file.read()
file.close()

def file_location_configuration(args):
    """Allows to set the location from where to get the data file"""
    open("location.txt", "w").close()
    file = open("location.txt", "r+")
    location = input("What file would you like to use? Please write the location: ")

    if path.exists(location):
        file.write(location)
        print("Success! File location was scanned.")
    else:
        print("Error! File does not exist.")

    file.close()

def dump(args):
    """Prints a list with all the information about proteins"""
    for record in parse.uniprot_seqrecords(LOC):
        print(record)

def name_list(args):
    """Prints a list with the lengths of proteins"""
    for record in parse.uniprot_seqrecords(LOC):
        print(record.name)

def proteins_average_lenght(args):
    """Prints the average length of all proteins"""
    print("Average Length is {}".format(analysis.average_len(parse.uniprot_seqrecords(LOC))))

def bar_plot_average_by_taxa(args):
    """Gives bar chart with the average length of top level taxa proteins"""
    av = analysis.average_len_taxa(parse.uniprot_seqrecords(LOC), depth = ())
    plot.plot_bar_show(av)

def pie_plot_average_by_taxa(args):
    """Gives pie chart with the average length of top level taxa proteins"""
    av = analysis.average_len_taxa(parse.uniprot_seqrecords(LOC), depth = ())
    plot.plot_pie_show(av)

def cli():
    """Configures and describes parsing, protein data and help functions"""
    parser = argparse.ArgumentParser(prog = "uniplot", usage = '%(prog)s [options]')

    subparsers = parser.add_subparsers(help = "Sub Command Help")

    subparsers.add_parser("file_location").set_defaults(func = file_location_configuration)
    subparsers.add_parser("dump").set_defaults(func = dump)
    subparsers.add_parser("list").set_defaults(func = name_list)
    subparsers.add_parser("average").set_defaults(func = proteins_average_lenght)
    subparsers.add_parser("bar_average-by-taxa").set_defaults(func = bar_plot_average_by_taxa)
    subparsers.add_parser("pie_average-by-taxa").set_defaults(func = pie_plot_average_by_taxa)

    parser.add_argument('--file_location', help = 'allows the user to set the location of the file'
                                                  'that he wants to use')
    parser.add_argument('--dump', help = 'gives a list with all the information about proteins '
                                         '- protein sequence, ID, name, lenght, description and other '
                                         'related data')
    parser.add_argument('--list', help = 'gives a list with only the lenghts of proteins')
    parser.add_argument('--average', help = 'gives average lenght of all proteins')
    parser.add_argument('--bar_average-by-taxa', help = 'gives average lenght of proteins categorized '
                                                        'by type in a form of a bar chart')
    parser.add_argument('--pie_average-by-taxa', help = 'gives average lenght of proteins categorized '
                                                        'by type in a form of a pie chart')

    args = parser.parse_args()

    args.func(args)
