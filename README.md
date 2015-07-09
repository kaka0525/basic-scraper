# Scraping Health Inspection Data
Jesse Klein and Karen Wong

Use this script from the command line to parse through local health inspection data. Pass additional arguments to control the sorting of the results. Enter 'averagescore', 'highscore', or 'mostinspections' for the first argument to sort according to the score or total inspections data. Enter the number of listings to see as the second argument. Optionally add 'reversed' to sort in reversed order for the third argument. We referred to the argparse docs in the Python standard library for its use.