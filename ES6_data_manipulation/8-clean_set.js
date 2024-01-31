/* eslint-disable */
export default function cleanSet(set, startString) {
  if (!startString || typeof startString !== 'string') {
    return '';
  }
    const arr = [];
    for (const item of set) {
      if (item && item.startsWith(startString)) {
        arr.push(item.slice(startString.length));
      }
    }
  return arr.join('-');
}
