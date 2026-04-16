"""CodeHS Python Practice Basics — question 3. Add the official exercise title from CodeHS."""
Write a function that takes in a number of people and a number of groups. The people will be split up into the groups evenly (there might be left over people). Return the number of people that are left over after creating the even groups.
def left_over(num_people,num_groups):
    return num_people-num_people//num_groups*num_groups