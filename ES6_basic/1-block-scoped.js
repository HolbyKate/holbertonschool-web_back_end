/* eslint-disable */
export default function taskBlock(trueOrFalse) {
    let task = false;
    let task2 = true;

    if (trueOrFalse) {
      let task = true;
      const task2 = false;
    }

    return [task, task2];
  }
