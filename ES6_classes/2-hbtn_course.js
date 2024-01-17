/* eslint-disable */
export default class HolbertonCourse {
    constructor(name, length, students) {
        this._name = name;
        this._length = length;
        this._students = students;
    }

    get name() {
        return this._name;
    }

    set name(newName) {
        this._name = newName;
    }

    get length() {
        return this._length;
    }

    set length(newLength) {
        this._length = newLength;
    }

    get students() {
        return this._students;
    }

    set students(newStudents) {
        this._students = newStudents;
    }
}
