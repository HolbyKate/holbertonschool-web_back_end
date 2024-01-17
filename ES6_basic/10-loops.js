/* eslint-disable */
export default function appendToEachArrayValue(array, appendString) {
    for (const value of array) {
      const idx = array
      array[idx] = appendString + value;
    }
  
    return array;
  }
