/* eslint-disable */
export default function createEmployeesObject(departmentName, employees) {
    const createEmployeesObject = {
        [departmentName]: employees,
    };

    return createEmployeesObject;
}