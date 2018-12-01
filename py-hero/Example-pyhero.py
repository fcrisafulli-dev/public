import pyhero

print("Loading chart . . .")

chart = pyhero.Chart("Sample",20)
chart.import_chart("sample.pyhero")

print("Playing Sample")

while chart.end_check() == False:
    chart.print_chart()
    #keys = input("> ")
    chart.submit([0,0,1,0,0],autostep=True)
    #chart.submit([
     #   keys[0],
      #  keys[1],
      #  keys[2],
      #  keys[3],
      #  keys[4]],autostep=True)

print("Score: %s/%s"%(chart.score,chart.max_score))
