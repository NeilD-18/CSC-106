


def read_precipitation_data(filename):
    """Read the precipitation data from filename into a dictionary that is
    mapping months to lists of measurements.

    """

    precip_dict = {}
    file = open(filename, "r")

    for line in file: 
      line = line.strip()
      data = line.split(",")
      if data[1] == "Month":
        pass
      else: 
        data1 = data[2:]
        updated_data = []
        for x in data1:
          if x != "":
            updated_data.append(data)
        precip_dict[data[1]] = data[data1]
      
    file.close()
    return precip_dict

def write_summary(monthly_data, filename):
    """Write a summary of the given precipitation dictionary to a file
    with the given filename. For each month it should write the month,
    total precipitation, average, precipitation, minimum and maximum
    precipitation that month to a new file. The format of the new file
    should be:
		January,3.55,0.12,0.0,0.86
		February,3.3,0.12,0.0,1.1
		...
		December,4.41,0.14,0.0,1.21
    """
    file = open(filename, "w")

    list_of_months = []

    for key in monthly_data.keys():
      list_of_months.append(key)
    
    print(list_of_months)
    list_of_summaries = []
   
    for value_list in monthly_data.values():
      total = 0

      print(value_list)
      
      for value in value_list:

        if value != "": 
          total += float(value)
      
      print(total)
      avg = total/len(value_list)
      min_precip = min(value_list)
      max_precip = max(value_list)

      summary = "," + str(total) +"," + str(avg) + "," + str(min_precip) + "," + str(max_precip)

      list_of_summaries.append(summary)
    
    for x in range(len(list_of_months)):
      write = list_of_months[x] + list_of_summaries[x]
      file.write(write)
      file.write("\n")
      
      


    file.close()
      

      


precipitation_data = read_precipitation_data("/home/dateraon/Desktop/Coding Projects/Classwork/Writing to files practice/precipitation_cleaned.csv")
write_summary(precipitation_data, "/home/dateraon/Desktop/Coding Projects/Classwork/Writing to files practice/precip_summary.csv")
