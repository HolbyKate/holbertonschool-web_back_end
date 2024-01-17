/* eslint-disable */
import ClassRoom from './0-classroom.js';

export default function initializeRooms() {
    const classroom1 = 19;
    const classroom2 = 20;
    const classroom3 = 34;

    return [
        new ClassRoom(classroom1),
        new ClassRoom(classroom2),
        new ClassRoom(classroom3)
    ];
}
