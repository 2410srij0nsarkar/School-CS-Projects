# SUB
import mysql.connector as sc
import tkintermapview as tmp
import customtkinter as ct
from CTkListbox import CTkListbox


def Template_Map():
    global coordinates

    # Connect to Database
    pw = "YOUR_SQL_PASSWORD"
    # Enter your password here
    db = "India"
    con = sc.connect(host="localhost", user="root", password=pw, database=db)

    if not con.is_connected():
        print("Not Connected!")

    else:
        # Retrieve Essential Records from Database
        cur = con.cursor()

        cur.execute("select Cities from cities where Country = 'India';")
        cities = cur.fetchall()

        cur.execute("select Latitude from cities where Country = 'India';")
        lats = cur.fetchall()

        cur.execute("select Longitude from cities where Country = 'India';")
        longs = cur.fetchall()

        # Convert Element Tuples to Individual Elements
        for i in range(len(cities)):
            (a,) = cities[i]
            (b,) = lats[i]
            (c,) = longs[i]
            cities[i] = a
            lats[i] = b
            longs[i] = c

        con.commit()
        con.close()

    if switch_var.get() == "on":
        # Mark every City on Map
        numcities = len(cities)
        for i in range(numcities):
            city = cities[i]
            # Secondary check for duplicate markers
            city_key = city.capitalize()
            if city_key in coordinates:
                continue

            lat = float(lats[i])
            long = float(longs[i])

            marker = map_widget.set_marker(
                lat, long, text=city, font=("Fixedsys", 20, "bold")
            )
            map_widget.set_position(lat, long)

            coordinates[city_key] = marker

        # Set Status Label
        statstr.set("Template Toggled!")
        status_label.configure(text_color="green", bg_color="black")

    elif switch_var.get() == "off":
        # Delete all Template Markers

        for place in list(coordinates.keys()):
            if place.title() in cities:
                coordinates[place].delete()
                del coordinates[place]

        # Set Status Label
        statstr.set("Toggle Off!!")
        status_label.configure(text_color="red", bg_color="black")


def markbut():
    global coordinates

    # Status Label Check
    try:
        # Get Coordinates and Place Details
        data = cordsentry.get()
        cords = tuple(data.split())
        name = nameentry.get()

        # Check for Empty Place Name
        if name.strip() == "":
            name = "Default"

        # Flag - Empty Dictionary
        flag = False

        for mark in coordinates.values():
            flag = True

            # Check for Existing Coordinates
            lat, long = mark.position
            lat = str(lat)
            long = str(long)

            if cords == (lat, long):
                # Set Status Label
                statstr.set("Coordinates Already Marked!")
                status_label.configure(text_color="yellow", bg_color="black")
                break

            else:
                if name.capitalize() not in coordinates:
                    # Convert from String to Float
                    (lat, long) = cords
                    lat = float(lat)
                    long = float(long)

                    # Set Map Marker using Coordinates
                    marker = map_widget.set_marker(
                        lat, long, text=name, font=("Fixedsys", 20, "bold")
                    )
                    map_widget.set_position(lat, long)

                    # Append to Marker List
                    coordinates[name.capitalize()] = marker

                    # Set Status Label
                    statstr.set("Location Marked!")
                    status_label.configure(text_color="green", bg_color="black")
                    break

                else:
                    # Set Status Label
                    statstr.set("Place Already Exists!")
                    status_label.configure(text_color="yellow", bg_color="black")
                    break

        # Code for Empty Dictionary
        if not flag:
            # Convert from String to Float
            (lat, long) = cords
            lat = float(lat)
            long = float(long)

            # Set Map Marker using Coordinates
            marker = map_widget.set_marker(
                lat, long, text=name, font=("Fixedsys", 20, "bold")
            )
            map_widget.set_position(lat, long)

            # Append to Marker List
            coordinates[name.capitalize()] = marker

            # Set Status Label
            statstr.set("Location Marked!")
            status_label.configure(text_color="green", bg_color="black")

    except ValueError:
        # Set Status Label
        statstr.set("Please Enter Valid Coordinates...")
        status_label.configure(text_color="red", bg_color="black")

    # CLear Entries
    nameentry.delete(0, ct.END)
    cordsentry.delete(0, ct.END)


def search_place():
    global coordinates
    global copyentry

    # Clear Copyable Coordinates
    copyentry.configure(state="normal")
    copyentry.delete(0, ct.END)

    # Get Searched Place Name
    place = searchentry.get().capitalize()

    # Status Label Check
    if place in coordinates:
        # Retrieve Marker Coordinates
        marker = coordinates[place]
        (lat, long) = marker.position

        # Place Marker on Searched Address
        map_widget.set_zoom(20)
        map_widget.set_position(lat, long)

        # Display Copyable Coordinates
        copyentry.insert(0, f"{lat} {long}")
        copyentry.configure(state="readonly")

        # Set Status Label
        statstr.set("Place Found!")
        status_label.configure(text_color="green", bg_color="black")

    else:
        # Set Status Label
        statstr.set("Could not find Place...")
        status_label.configure(text_color="red", bg_color="black")

    # Clear Entry
    searchentry.delete(0, ct.END)


def update_locations():

    # Make it globally accessible
    global locbox
    locbox.delete(0, ct.END)

    # Insert Places into Listbox
    for cords in coordinates:
        locbox.insert(ct.END, cords)


def delete():
    global coordinates

    # Get Deletion
    name = delentry.get().capitalize()

    # Find Required Place
    for plc, mark in coordinates.items():
        # Status Label Check
        if name == plc:
            # Center Map on Marker
            lat, long = mark.position
            map_widget.set_position(lat, long)

            # Delete Marker
            mark.delete()
            del coordinates[plc]

            # Set Status Label
            statstr.set("Place Deleted!")
            status_label.configure(text_color="red", bg_color="black")

            break

    else:
        # Set Status Label
        statstr.set("Could not find Marker!")
        status_label.configure(text_color="red", bg_color="black")

    # Clear Entry
    delentry.delete(0, ct.END)


# MAIN
app = ct.CTk()
app.title("PROJECT INDIA")
app.geometry("1920x1080")
app.config(background="Black")

# Make Title
Title = ct.CTkLabel(
    master=app,
    text="INDIA:REIMAGINED",
    font=("Fixedsys", 70, "bold"),
    fg_color="Black",
    text_color="Red",
)
Title.place(relx=0.5, rely=0.1, anchor=ct.CENTER)

# Create Map Frame
mapframe = ct.CTkFrame(master=app, width=800, height=500)
mapframe.place(relx=0.501, rely=0.6, anchor=ct.CENTER)

# Make Map Label
maplabel = ct.CTkLabel(
    master=app,
    text="MAP",
    font=("Orbitron", 30, "bold"),
    fg_color="Black",
    text_color="Yellow",
)
maplabel.place(relx=0.5, rely=0.2, anchor=ct.CENTER)

# Add Map Widget to Frame
map_widget = tmp.TkinterMapView(mapframe, width=800, height=500, corner_radius=0)
map_widget.pack()

# Set Default Position
st_lat, st_long = 12.9165237, 77.6430373
map_widget.set_position(st_lat, st_long)

# Set A Zoom Level
map_widget.set_zoom(20)
map_widget.place(relx=0.5, rely=0.5, anchor=ct.CENTER)

# Generalise Used Screen Positions
left_relx = 0.1
right_relx = 0.9

# Intiialize Coordinates Dictionary
coordinates = {}

# Instruction Label
insttxt = "Right Click to get Coordinates!"
instlabel = ct.CTkLabel(
    master=app,
    text=insttxt,
    font=("Orbitron", 15, "italic"),
    fg_color="Black",
    text_color="cyan",
)
instlabel.place(relx=left_relx, rely=0.1, anchor=ct.CENTER)

# Status Label and Status String
statstr = ct.StringVar(value="")
status_label = ct.CTkLabel(
    master=app, text="", font=("Verdana", 16), bg_color="Black", textvariable=statstr
)
status_label.place(relx=left_relx, rely=0.85, anchor=ct.CENTER)

# Mark Label
marktxt = "Mark any Place!"
marklabel = ct.CTkLabel(
    master=app,
    text=marktxt,
    font=("Orbitron", 15, "italic"),
    fg_color="Black",
    text_color="cyan",
)
marklabel.place(relx=left_relx, rely=0.3, anchor=ct.S)

# Mark Button
mark = ct.CTkButton(
    master=app,
    text="MARK",
    font=("Fixedsys", 45),
    width=200,
    height=50,
    bg_color="Black",
    command=markbut,
)
mark.place(relx=0.1, rely=0.4, anchor=ct.S)

# Coordinates Entry Box
cordsentry = ct.CTkEntry(
    master=app,
    width=200,
    height=50,
    corner_radius=10,
    bg_color="Black",
    placeholder_text="Enter Coordinates Here...",
    font=("Verdana", 14),
)
cordsentry.place(relx=left_relx, rely=0.5, anchor=ct.S)

# PLace Name Entry Box
nameentry = ct.CTkEntry(
    master=app,
    width=200,
    height=50,
    corner_radius=10,
    bg_color="Black",
    placeholder_text="Enter Place Name...",
    font=("Verdana", 14),
)
nameentry.place(relx=left_relx, rely=0.6, anchor=ct.S)

# Search Entry
searchentry = ct.CTkEntry(
    master=app,
    width=250,
    height=40,
    corner_radius=10,
    bg_color="Black",
    placeholder_text="Search Marker...",
    font=("Verdana", 14),
)
searchentry.place(relx=left_relx, rely=0.7, anchor=ct.CENTER)

# Search Button
search_button = ct.CTkButton(
    master=app,
    text="SEARCH",
    font=("Fixedsys", 45),
    width=250,
    height=40,
    bg_color="Black",
    command=search_place,
)
search_button.place(relx=left_relx, rely=0.79, anchor=ct.CENTER)

# Copyable Entry Label
copyentry = ct.CTkEntry(
    master=app,
    width=250,
    border_width=0,
    fg_color="transparent",
    bg_color="Black",
    text_color="cyan",
    font=("Verdana", 14),
    placeholder_text="Copyable Coordinates!",
)

copyentry.configure(state="readonly")
copyentry.place(relx=left_relx + 0.02, rely=0.9, anchor=ct.CENTER)

# Locations Label
loctxt = "Click to Update the Locations List!"
loclabel = ct.CTkLabel(
    master=app,
    text=loctxt,
    font=("Orbitron", 15, "italic"),
    fg_color="Black",
    text_color="cyan",
)
loclabel.place(relx=right_relx, rely=0.3, anchor=ct.CENTER)

# Locations Button
loc = ct.CTkButton(
    master=app,
    text="LOCATIONS",
    font=("Fixedsys", 40),
    width=150,
    height=50,
    bg_color="Black",
    command=update_locations,
)
loc.place(relx=right_relx, rely=0.4, anchor=ct.S)

# Locations Frame
loc_frame = ct.CTkFrame(app)
loc_frame.place(relx=right_relx, rely=0.6, anchor=ct.S)

# Locations Widget
locbox = CTkListbox(loc_frame)
locbox.pack()

# Delete Button
delete_button = ct.CTkButton(
    master=app,
    text="DELETE",
    font=("Fixedsys", 45),
    width=180,
    height=50,
    bg_color="Black",
    command=delete,
)
delete_button.place(relx=right_relx, rely=0.79, anchor=ct.CENTER)

# Delete Entry
delentry = ct.CTkEntry(
    master=app,
    width=200,
    height=50,
    corner_radius=10,
    bg_color="Black",
    placeholder_text="Enter Place...",
    font=("Verdana", 14),
)
delentry.place(relx=right_relx, rely=0.7, anchor=ct.CENTER)

# Template Toggle Setup
switch_var = ct.StringVar(value="off")

template = ct.CTkSwitch(
    master=app,
    text="TEMPLATE",
    font=("Fixedsys", 45),
    width=180,
    height=50,
    bg_color="Black",
    command=Template_Map,
    variable=switch_var,
    onvalue="on",
    offvalue="off",
)
template.place(relx=0.85, rely=0.1, anchor=ct.CENTER)

app.mainloop()
