import datetime


########################################################################
class MyCache:

    def __init__(self):
        """Constructor"""
        self.cache = {}
        self.max_cache_size = 20

    # ----------------------------------------------------------------------
    def __contains__(self, key):
        """
        Returns True or False depending on whether or not the key is in the
        cache
        """
        return key in self.cache

    def __getitem__(self, key):
        return self.cache[key]

    def __setitem__(self, key, value):
        if len(self.cache) >= self.max_cache_size:
            self.remove_oldest()
        self.cache.__setitem__(key, value)

    def update(self, key, value):
        """
        Update the cache dictionary and optionally remove the oldest item
        """
        key = key.replace("\n", "")
        if key not in self.cache and len(self.cache) >= self.max_cache_size:
            self.remove_oldest()
        # print value
        self.cache[key] = {'date_accessed': datetime.datetime.now(),
                           'value': value}

    def __delitem__(self, key):
        if key in self.cache:
            del self.cache[key]

    def remove_oldest(self):
        """
        Remove the entry that has the oldest accessed date
        """
        oldest_entry = None
        for key in self.cache:
            if oldest_entry is None:
                oldest_entry = key
            elif self.cache[key]['date_accessed'] < self.cache[oldest_entry]['date_accessed']:
                oldest_entry = key
        self.cache.__delitem__(oldest_entry)

    @property
    def size(self):
        """
        Return the size of the cache
        """
        return len(self.cache)

    @property
    def read(self):
        """:return sorted dict on the basic of marks obtained """
        student_records = {}
        for key in self.cache:
            if key is not None:
                student_records.__setitem__(key, self.cache[key]['value'])
        return sort_cache(student_records)


ITEM_STRUCTURE = {"Name": "", "Maths": "", "Science": "", "id": ""}


def sort_cache(dict):
    """function which sort the dict items based on marks percentage(Derived attribute)"""
    def dict_val(x):
        return x[1]['percentage']

    sorted_x = sorted(dict.items(), key=dict_val, reverse=True)
    return sorted_x


def to_dict_item(args):
    try:
        ITEM_STRUCTURE["Name"] = args[0].split("@")[0] + " " + args[0].split("@")[1]
    except IndexError:
        ITEM_STRUCTURE["Name"] = args[0]
    try:
        ITEM_STRUCTURE["Maths"] = args[1].split("@")[1]
    except IndexError:
        ITEM_STRUCTURE["Maths"] = args[1]
    try:
        ITEM_STRUCTURE["Science"] = args[2].split("@")[1]
    except IndexError:
        ITEM_STRUCTURE["Science"] = args[2]
    try:
        ITEM_STRUCTURE["id"] = args[3].split("@")[1]
    except IndexError:
        ITEM_STRUCTURE["id"] = args[3]
    ITEM_STRUCTURE.__setitem__("percentage", (float(ITEM_STRUCTURE["Maths"])) + float(ITEM_STRUCTURE["Science"]) / 2)
    return ITEM_STRUCTURE


def add():
    roll_number = raw_input("Enter student roll number: ")
    name = raw_input("Please enter student name: ")
    maths = raw_input("Please enter maths marks: ")
    science = raw_input("Please enter science marks")
    student_data = to_dict_item((name, maths, science, roll_number))
    student_data["id"] = {'date_accessed': datetime.datetime.now(),
                          'value': {key: value for key, value in d.items() if key != "id"}}
    cache.__setitem__(roll_number, student_data["id"])


def read():
    print "Size of cache is: {}\n".format(cache.size)
    print cache.read


def update():
    roll_number = raw_input("Please enter student roll number: ")
    if cache.__contains__(roll_number):
        print("Please select subject to update marks: ")
        print("1 Maths: ")
        print("2 Science: ")
        ch = int(raw_input("Please enter your choice: "))
        data = cache[roll_number]
        if ch == 1:
            data['value']['Maths'] = raw_input("Marks(100): ")
            data['date_accessed'] = datetime.datetime.now()

        elif ch == 2:
            data['value']['Science'] = raw_input("Marks(100): ")
            data['date_accessed'] = datetime.datetime.now()
        else:
            print("Please select a valid subject")
        cache.update(roll_number, data)
        print("Data updated successfully")
    else:
        print("No record found")


def delete():
    roll_number = raw_input("Please enter roll number to delete record: ")
    if roll_number in cache:
        cache.__delitem__(roll_number)
        print("Record deleted successfully")
    else:
        print("No Record Found")


# FILE_FORMAT = "{} maths@{} science@{} id@{}\n"


def exit():
    with open("pythondataset.txt", "w") as f:
        data_str = ""
        for item in cache.read:
            try:
                name = (item[1]["Name"]).split(" ")[0] + "@" + (item[1]["Name"]).split(" ")[1]
            except IndexError:
                name = item[1]["Name"]
            data = "{} maths@{} science@{} id@{}\n".format(name, item[1]['Maths'], item[1]['Science'], item[0])
            data_str += data
        print data_str
        f.write(data_str)
        f.truncate()
    import sys
    sys.exit(0)


if __name__ == '__main__':
    cache = MyCache()
    with open("pythondataset.txt", "r+") as f:
        data = f.readlines()
        for record in data:
            details = record.split(" ")
            print details
            d = to_dict_item(details)
            cache.update(d["id"], {key: value for key, value in d.items() if key != "id"})
    while cache.__class__:
        choices = ["add", "read", "update", "delete", "exit"]
        for i, choice in enumerate(choices):
            print str(i + 1) + " " + choice + "..."
        try:
            user_choice = int(raw_input("Please enter your choice"))
            if user_choice == 1:
                add()
            elif user_choice == 2:
                read()
            elif user_choice == 3:
                update()
            elif user_choice == 4:
                delete()
            elif user_choice == 5:
                exit()
            else:
                print("wrong input")

        except ValueError:
            print("Please enter valid option")
