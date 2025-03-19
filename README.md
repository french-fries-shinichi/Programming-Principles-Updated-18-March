## Final Project for ...
can't bother to finish the rest.

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

### errors resolved:
- No age range verification (ie not allowing any integers; for example a baby can't be a student!)
- names (for add_course func) accepts symbol characters, is this intented?
  and do we limit all or some symbols?