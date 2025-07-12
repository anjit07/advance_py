from app.model.staff import Staff
staff_details = {
        "name": "Amit",
        "empCode": "009754",
        "address":"New Delhi"
    }


staff_list = [staff_details]

def get_staff_list()-> any:
    return staff_list

def add_staff(new_staff:Staff) -> any:
    staff_list.append(new_staff)
    return new_staff
