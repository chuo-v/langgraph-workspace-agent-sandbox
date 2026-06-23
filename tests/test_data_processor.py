import os
import subprocess
import sys
import unittest


class TestDataProcessor(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("🚀 Running dummy Agentic CI tests for the workspace sandbox...\n")
        cls.script_path = os.path.abspath(
            os.path.join(
                os.path.dirname(__file__), "..", "scripts", "data_processor.py"
            )
        )

    def test_default_execution(self):
        """Test 1: Basic functionality (No arguments) expected to use default multiplier."""
        result = subprocess.run(
            [sys.executable, self.script_path], capture_output=True, text=True
        )
        self.assertIn(
            "Default Result: 20",
            result.stdout,
            "Data processor failed to use default arguments.",
        )

    def test_valid_integer_argument(self):
        """Test 2: Valid integer argument (e.g., 5 * 2 = 10)."""
        result = subprocess.run(
            [sys.executable, self.script_path, "5"], capture_output=True, text=True
        )
        self.assertIn(
            "Result: 10",
            result.stdout,
            "Data processor failed to calculate the correct multiplier.",
        )

    def test_invalid_argument_handling(self):
        """Test 3: Invalid argument handling should catch ValueError gracefully."""
        result = subprocess.run(
            [sys.executable, self.script_path, "not_a_number"],
            capture_output=True,
            text=True,
        )
        self.assertIn(
            "Please provide an integer.",
            result.stdout,
            "Data processor did not output the expected error handling message.",
        )


if __name__ == "__main__":
    # unittest.main() automatically handles system exit codes (0 for success, 1 for failure),
    # which integrates perfectly with any CI/CD pipeline or your agent's evaluation nodes.
    unittest.main(verbosity=2)
