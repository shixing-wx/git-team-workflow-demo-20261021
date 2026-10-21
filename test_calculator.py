"""Behavior tests for calculator operations and CLI errors."""
import subprocess
import sys
import unittest
from pathlib import Path

from calculator import calculate


class CalculatorTests(unittest.TestCase):
    def test_arithmetic_regression(self):
        cases = [(8, 2, "add", 10), (8, 2, "subtract", 6),
                 (8, 2, "multiply", 16)]
        for left, right, operation, expected in cases:
            with self.subTest(operation=operation):
                self.assertEqual(calculate(left, right, operation), expected)

    def test_division(self):
        self.assertEqual(calculate(8, 2, "divide"), 4)
        self.assertEqual(calculate(-9, 2, "divide"), -4.5)

    def test_zero_divisors(self):
        for divisor in (0, 0.0, -0.0):
            with self.subTest(divisor=divisor):
                with self.assertRaisesRegex(ValueError, "Cannot divide by zero"):
                    calculate(8, divisor, "divide")

    def test_cli_zero_divisor(self):
        result = subprocess.run(
            [sys.executable, str(Path(__file__).with_name("calculator.py")),
             "8", "0", "divide"], capture_output=True, text=True,
        )
        self.assertEqual(result.returncode, 2)
        self.assertIn("Cannot divide by zero", result.stderr)
        self.assertNotIn("Traceback", result.stderr)

    def test_cli_division(self):
        result = subprocess.run(
            [sys.executable, str(Path(__file__).with_name("calculator.py")),
             "8", "2", "divide"], capture_output=True, text=True,
        )
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), "4.0")


if __name__ == "__main__":
    unittest.main()
