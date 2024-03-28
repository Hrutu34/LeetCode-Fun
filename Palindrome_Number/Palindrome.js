/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    if (x < 0) {
        return false;
    }
    let x1 = x;
    let x2 = 0;
    while (x > 0) {
        x2 = x2 * 10 + x % 10;
        x = Math.floor(x / 10);
    }
    return x1 === x2;
};