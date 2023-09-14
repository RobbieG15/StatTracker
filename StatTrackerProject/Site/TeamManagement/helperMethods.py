from .models import *
import csv

def handle_input_file(file, org, team):
    csvReader = csv.reader(file, delimiter=',')
    line_count = 0
    for row in csvReader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')\
                
        else:
            player = Player.create(
                first_name = row[0],
                last_name = row[1],
                number = row[2],
                team = team
            )
            if len(Player.objects.filter(number = player.number)) == 0:
                player.save()
        line_count += 1
