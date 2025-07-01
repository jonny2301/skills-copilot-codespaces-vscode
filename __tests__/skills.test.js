const { calculateNumbers } = require('../skills');

test('adds two numbers', () => {
  expect(calculateNumbers(1, 2)).toBe(3);
});
