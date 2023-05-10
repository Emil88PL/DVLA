import re

license_plate = input("Enter Licenseplate: \n").upper()

lenght_traveled = input("How far did you travel: \n" )
time_traveled = input("How long did you travel: \n")

speed = int(lenght_traveled) / int(time_traveled)

license_plate = re.sub(r"([A-Z]{2}\d{2})([A-Z]{3})", r"\1 \2", license_plate)

print("Speed was: ", speed, "\n")

if license_plate:
    if speed > 60:
        file = open("penalty_speed.txt", "a")
        file.write("License plate: " + str(license_plate) + " Have over: " + str(speed) + "km/h!""\n")
        file.close()
        print("Saved to txt file \n")
   # print(license_plate)
else:
    print("Licenseplate is not standard")


dvla = open("dvla_db.txt", "r")

    

key = license_plate

index = {}
while True:
    line = dvla.readline()
    if not line: break
    fields = line.split(",")
    index[fields[0]] = dvla.tell() - len(line)
    


if key in index.keys():
    dvla.seek(index[key])
    print("Correct address: ", dvla.readline(-2))
    #print("wrong one: " , dvla.readline())
else:
    print("No data found")
    print(license_plate)
    print(dvla.readline())

dvla.close()