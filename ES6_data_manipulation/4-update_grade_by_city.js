/* eslint-disable */
export default function updateStudentGradeByCity(students, city, newGrades) {
  if (!Array.isArray(students)) {
    return [];
  }
  return students.filter((student) => student.location === city).map((student) => {
    const grade = newGrades.filter((grade) => grade.studentId === student.id)[0];
    return newGrades
  });
}