"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    :param record: tuple - with a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """ 
    return record[1]


def convert_coordinate(coordinate):
    """Split the given coordinate into tuple containing its individual components.

    :param coordinate: str - a string map coordinate
    :return: tuple - the string coordinate split into its individual components.
    """
    return (coordinate[0],coordinate[1])


def compare_records(azara_record, rui_record):
    """Compare two record types and determine if their coordinates match.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, tuple(coordinate_1, coordinate_2), quadrant) trio.
    :return: bool - do the coordinates match?
    """
    return tuple(azara_record[1]) == rui_record[1]
     


def create_record(azara_record, rui_record):
    """Combine the two record types (if possible) and create a combined record group.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: tuple or str - the combined record (if compatible), or the string "not a match" (if incompatible).
    """
    
    if compare_records(azara_record, rui_record):
        return (
            azara_record[0],  
            azara_record[1],  
            rui_record[0],    
            rui_record[1],    
            rui_record[2]     
        )
    else:
        return "not a match"   


def clean_up(combined_record_group):
    report = []

    for record in combined_record_group:
        cleaned_record = (
            record[0],  # treasure
            record[2],  # location
            record[3],  # coordinate tuple
            record[4]   # quadrant
        )

        report.append(str(cleaned_record))

    return "\n".join(report) + "\n"