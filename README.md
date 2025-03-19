## Final Project for ...
can't bother to finish the rest.

### Our program should...
do the following:
- Add students
  - student name should start with capital letters, can contain spaces, cannot contain
    numbers or symbols
  - student ID should contain only numbers, have a length of 6 digits
  - student age should be a positive integer, within the range of 0 <= age <= 100
  - student email should follow this function's output:
    re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)
- Add courses
  - course code should contain only capital letters, and be 3 letters in length
  - course number should consist of a 4 digits number
  - course name should consist of letters and space
  - value of total seats should equal to available seats + number of students enrolled in
    the course (ignore for now...)
- Enrolling students (into a course)
  - 
- Dropping a student from a course
  - 
- viewing available courses
  - 
- view student information
  - 
- Exiting the program gracefully
  - (since we close files after an action is done, all there is to do is just trigger the
    system's exit function)
  - print a goodbye message

### Bugs to hunt down
no bounties offered
- [Optional] perferrably, enroll() function should ask for student ID instead, since it's less
  error prone (for example a long name might be typed with wrong spelling), name might contain
  special characters, and student ID are unique (eg there might be two or three "Muhammed Ali",
  talking from experience)
- Does our program check for duplicates at all? (unique identifier duplicates, such as student_id,
  course_id, etc; stuff like names are allowed to have duplicates (for the reasons i mentioned
  above). also speaking of duplicates make sure that no students are enrolled into the same
  course twice
- now our program doesn't even accept spaces for names, so only first name or last name can be
  used in add_student()

### Possibilities
Possible bugs that could be present in our software (if you think the lecturer won't notice or
care, then go back to kindergarten)
- Duplicates of unique data: data that should be unique, should stay unique, we should implement
  a way to detect them
- options 4-10 i haven't tested yet
- cross-reference: does the program check if the student that is trying to enroll/drop/etc even
  exist in the first place?? (i feel like this will cause a headache or three)

### features to consider
(DO NOT ADD THESE, these are just proposal changes we will talk about in the report
 they are not neccessary for our project's goals)
- Ability to delete entries into the table files (they were going to be added, but...)
- 
