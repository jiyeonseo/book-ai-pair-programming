CREATE TABLE Teachers (
    teacher_id INT PRIMARY KEY,
    name VARCHAR(100),
    subject VARCHAR(50)
);

CREATE TABLE Classes (
    id INT PRIMARY KEY,
    grade INT,
    class INT,
    teacher_id INT,
    FOREIGN KEY (teacher_id) REFERENCES Teachers(id)
);

CREATE TABLE Students (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    grade INT,
    class INT,
    FOREIGN KEY (grade, class) REFERENCES Classes(grade, class)
);

CREATE TABLE Subjects (
    id INT PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE Grades (
    student_id INT,
    subject_id INT,
    grade INT,
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (subject_id) REFERENCES Subjects(subject_id),
    PRIMARY KEY (student_id, subject_id)
);
