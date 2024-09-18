'''
    @Author: VEMULA DILEEP
    @Date: 17-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 11:10
    @Title : Find the fewest notes to be returned for Vending Machine.
'''

def find_fewest_notes(change):
    """
    Finds the minimum number of notes to be returned as change and 
    the respective denominations.
    
    Parameters:
    change (int): The amount of change in Rs to be returned.
    
    Returns:
    tuple: A tuple containing the total number of notes and a dictionary with notes and their counts.
    """
    notes = [1000, 500, 100, 50, 10, 5, 2, 1]
    note_count = {}
    total_notes = 0
    
    for note in notes:
        if change >= note:
            count = change // note
            change = change % note
            note_count[note] = count
            total_notes += count
    
    return total_notes, note_count


def main():
    """
    Main function to take user input and calculate the minimum notes to return as change.
    """
    change = int(input("Enter the amount of change to be returned: "))
    
    if change <= 0:
        print("Please enter a valid amount greater than 0.")
    else:
        total_notes, note_count = find_fewest_notes(change)
        print(f"Minimum number of notes needed: {total_notes}")
        print("Notes distribution:")
        for note, count in note_count.items():
            print(f"{note} Rs: {count}")


if __name__ == "__main__":
    main()
